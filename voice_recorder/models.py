from django.db import models


# Create your models here.
class Audio(models.Model):
    audio = models.FileField(upload_to='upload/audios')

    class Meta:
        db_table = "Audio"


class UpdatedAudio(models.Model):
    updated_audio = models.FileField(upload_to='upload/updated_audios')

    class Meta:
        db_table = "Updated_Audio"
