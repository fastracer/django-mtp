## Django Packages
from django.contrib.gis.db import models
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from datetime import datetime
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator
## Python Packages
import uuid
from lib.functions import *
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.core.files import File
from urllib.request import urlretrieve
from colorful.fields import RGBColorField

UserModel = get_user_model()

def image_directory_path(instance, filename):
    path = 'sequence/{}/{}/{}.jpg'.format(instance.username, instance.seq_key, filename)
    print("image path: ", path)
    return path

class Icon(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    font_awesome = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed for Username.')
    name = models.CharField(max_length=50, unique=True, null=True, validators=[alphanumeric])
    description = models.TextField(default=None, blank=True, null=True)
    is_actived = models.BooleanField(default=True)

    def __str__(self):
        return self.name

def getAllTags():
    items = Tag.objects.filter(is_actived=True)
    itemsTuple = ()
    for item in items:
        itemsTuple = itemsTuple + ((item.pk, item.name),)
    print(itemsTuple)
    return itemsTuple

class TransType(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.name + ' - ' + self.name

    def getFullName(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.name + ' - ' + self.name

    def getPK(self):
        return self.pk

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'Transport Type'

class LabelType(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(blank=True, null=True)
    # type is one of "point" and "polygon"
    # type = models.CharField(max_length=50, choices=(('point', 'point'), ('polygon', 'polygon'),), default='point')
    type = models.CharField(max_length=50, choices=(('polygon', 'polygon'),), default='polygon')
    color = RGBColorField(default='#ffffff')


    def __str__(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.name + '--' + self.name

    def getKey(self):
        if self.parent is None:
            key = self.name
        else:
            key = self.parent.name + '--' + self.name
        key = key.replace(' ', '-')
        key = key.lower()
        return key

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'Image Label Type'

def getAllCaptureType():
    items = TransType.objects.all()
    itemsTuple = ()
    for item in items:
        itemsTuple = itemsTuple + ((item.pk, item.name),)
    return itemsTuple

class CameraMake(models.Model):
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

class CameraModel(models.Model):
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

class Sequence(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    camera_make = models.ForeignKey(CameraMake, on_delete=models.CASCADE, null=True, blank=True)
    captured_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    seq_key = models.CharField(max_length=100, null=True, blank=True, verbose_name="Mapillary Sequence Key",)
    pano = models.BooleanField(default=False)
    user_key = models.CharField(max_length=100, null=True, blank=True, verbose_name="Mapillary User Key",)
    username = models.CharField(max_length=100, null=True, blank=True, verbose_name="Mapillary Username",)
    geometry_coordinates = models.LineStringField(null=True, blank=True)
    geometry_coordinates_ary = ArrayField(ArrayField(models.FloatField(default=1)), null=True, blank=True)
    coordinates_cas = ArrayField(models.FloatField(default=0), null=True, blank=True)
    coordinates_image = ArrayField(models.CharField(default='', max_length=100), null=True, blank=True)
    is_uploaded = models.BooleanField(default=False)
    is_privated = models.BooleanField(default=False)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    name = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    transport_type = models.ForeignKey(TransType, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tag)

    image_count = models.IntegerField(default=0)

    is_mapillary = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)

    google_street_view = models.BooleanField(default=False)
    strava = models.CharField(max_length=50, null=True, blank=True)

    distance = models.FloatField(null=True, blank=True)

    def getImageCount(self):
        if not self.coordinates_image is None:
            return len(self.coordinates_image)
        else:
            return 0

    def getTransportType(self):
        captureType = []
        for t in self.type:
            cType = TransType.objects.get(pk=t)
            if cType:
                captureType.append(cType.name)

        if len(captureType) > 0:
            return ', '.join(captureType)
        else:
            return ''

    def getTagStr(self):
        tags = []
        if self.tag.all().count() == 0:
            return ''
        for tag in self.tag.all():
            if tag and tag.is_actived:
                tags.append(tag.name)

        if len(tags) > 0:
            return ', '.join(tags)
        else:
            return ''

    def getTags(self):
        tags = []
        if self.tag.all().count() == 0:
            return ''
        for tag in self.tag.all():
            if tag and tag.is_actived:
                tags.append(tag.name)
        return tags

    def getShortDescription(self):
        description = self.description
        if len(description) > 100:
            return description[0:100] + '...'
        else:
            return description

    def getFirstImageKey(self):
        if len(self.coordinates_image) > 0:
            return self.coordinates_image[0]
        else:
            return ''

    def getLikeCount(self):
        liked_guidebook = SequenceLike.objects.filter(sequence=self)
        if not liked_guidebook:
            return 0
        else:
            return liked_guidebook.count()

    def getDistance(self):
        all_distance = 0
        if self.geometry_coordinates_ary is None:
            return all_distance


        if (len(self.geometry_coordinates_ary) > 0):
            first_point = self.geometry_coordinates_ary[0]
            for i in range(len(self.geometry_coordinates_ary) - 1):
                if i == 0:
                    continue
                second_point = self.geometry_coordinates_ary[i]
                d = distance(first_point, second_point)
                first_point = second_point
                all_distance += d
            all_distance = "%.3f" % all_distance
        return all_distance

    def getCoverImage(self):
        image_keys = self.coordinates_image
        if image_keys is None:
            return None
        if len(image_keys) > 0:
            return image_keys[0]
        else:
            return None

    def getFirstPointLat(self):
        if self.geometry_coordinates_ary is None:
            return None
        lat = self.geometry_coordinates_ary[0][1]
        return lat

    def getFirstPointLng(self):
        if self.geometry_coordinates_ary is None:
            return None
        lng = self.geometry_coordinates_ary[0][0]
        return lng

class Image(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    camera_make = models.ForeignKey(CameraMake, on_delete=models.CASCADE, null=True, blank=True)
    camera_model = models.ForeignKey(CameraModel, on_delete=models.CASCADE, null=True, blank=True)
    cas = models.FloatField(default=0)
    captured_at = models.DateTimeField(null=True, blank=True)
    sequence = models.ForeignKey(Sequence, on_delete=models.CASCADE, null=True, blank=True)
    seq_key = models.CharField(max_length=100, default='')
    image_key = models.CharField(max_length=100)
    pano = models.BooleanField(default=False)
    user_key = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=100, default='')
    organization_key = models.CharField(max_length=255, null=True)
    is_uploaded = models.BooleanField(default=False)
    is_privated = models.BooleanField(default=False)
    is_mapillary = models.BooleanField(default=True)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    ele = models.FloatField(default=0)
    type = models.CharField(max_length=50, default='Point')

    point = models.PointField(null=True, blank=True)

    mapillary_image = models.ImageField(upload_to=image_directory_path, null=True, blank=True)

    image_label = models.ManyToManyField(LabelType, through='ImageLabel')

    def getSequence(self):
        if self.seq_key != '':
            sequence = Sequence.objects.get(seq_key=self.seq_key)
            if sequence is None or not sequence:
                return None
            return sequence
        return None

class SequenceLike(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    sequence = models.ForeignKey(Sequence, on_delete=models.CASCADE)

class ImageViewPoint(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True, related_name='owner_id')

class ImageLabel(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    label_type = models.ForeignKey(LabelType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    point = models.PointField(null=True, blank=True)
    polygon = models.PolygonField(null=True, blank=True)
