from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)


# Generic Relationship (3 lines needed)
class TagItem(models.Model):
    # what tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # ------- For defining a generic relationship, 3 lines are needed -------
    # Generic Type (product, video, article, ...)
    # Object ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # when querying, we want to get the actual object of this content
    content_object = GenericForeignKey()