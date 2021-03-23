from django.db import models

# Create your models here.
class VideoData(models.Model):
    video_id = models.CharField(max_length=100, unique=True)
    video_title = models.CharField(max_length=500)
    video_description = models.CharField(max_length=500)
    video_publishing_datetime = models.DateTimeField(db_index=True)
    video_thumbnails = models.CharField(max_length=500)
    video_channel_id = models.CharField(max_length=500)
    video_channel_title = models.CharField(max_length=500)

    class Meta:
        indexes = [models.Index(fields=['-video_publishing_datetime']),]

