# -*- coding: utf-8 -*-
from datetime import date
from django.db import models
from sorl.thumbnail import ImageField


def get_file_name(instance, filename):
        url = "%s/%s/%s" % (instance.__class__.__name__,
                            date.today().strftime("%Y_%m_%d"),
                            filename)
        return url

class Estate(models.Model):
    pageid = models.IntegerField(u'PageId')
    title = models.CharField(u'ProjectName', max_length=500)
    status = models.CharField(u'Status', max_length=50)
    area = models.CharField(u'Area', max_length=100)
    url = models.URLField(u'URL')
    image = ImageField(u'Image', upload_to=get_file_name)
    is_publish = models.BooleanField(u'IsPublish', default=True)

    def __unicode__(self):
        return u'{} - {}'.format(self.title, self.area)

    class Meta:
        verbose_name = u'Estate Object'
        verbose_name_plural = u'Estate Objects'