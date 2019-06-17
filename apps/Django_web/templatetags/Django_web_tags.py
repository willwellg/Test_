#!/usr/bin/env python
# encoding: utf-8


from django import template
from Django_web.models import Tag

register = template.Library()

@register.inclusion_tag('Django_web/tags/cloud.html')
def load_cloud():
    """
    显示标签云
    :return:
    """
    clouds = Tag.objects.all()
    return {'clouds': clouds}
