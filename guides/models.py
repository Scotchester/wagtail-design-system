from django.db import models

from wagtail.core.models import Page


class GuidePage(Page):
    parent_page_types = ['guides.GuideIndexPage']


class GuideIndexPage(Page):
    pass
