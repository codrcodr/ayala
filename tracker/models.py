from django.db import models
from django.conf import settings

class TrackerBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True

class AssetType(TrackerBaseModel):
    name = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=50)

class Asset(TrackerBaseModel):
    show = models.CharField(max_length=30)
    sequence = models.CharField(max_length=30)
    shot = models.CharField(max_length=30)
    asset_type = models.CharField(max_length=30)
    handle_in = models.FloatField()
    cut_in = models.FloatField()
    cut_out = models.FloatField()
    handle_out = models.FloatField()

class Document(TrackerBaseModel):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=250, unique=True)
    version = models.IntegerField()
    frame_range = models.CharField(max_length=10)
    colorspace = models.CharField(max_length=20)
    data_type = models.CharField(max_length=30)
    instance_name = models.CharField(max_length=30)
    lod = models.CharField(max_length=30)

class DocumentContainer(TrackerBaseModel):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    documents = models.ManyToManyField(Document)

class Dependency(TrackerBaseModel):
    inputs = models.ManyToManyField(Document)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)