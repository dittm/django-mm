from django.db import models

class Image(models.Model):
    image_path = models.URLField(max_length=255, blank=True, null=True)
    thumbnail_path = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.image_path

    def get_image_url(self):
        return self.image_path

    def get_thumbnail_url(self):
        return self.thumbnail_path if self.thumbnail_path else ''

class Entity(models.Model):
    CATEGORY_CHOICES = (
        ('letter', 'Letter'),
        ('poem', 'Poem'),
        ('drawing', 'Drawing'),
    )

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Letter')
    metadata = models.FileField(upload_to='uploads/metadata/', blank=True, null=True)
    xml = models.FileField(upload_to='uploads/xml/', blank=True, null=True)
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return self.name
