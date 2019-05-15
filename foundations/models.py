from django.db import models

from wagtail.core.models import Page


class FoundationPage(Page):
    parent_page_types = ['foundations.FoundationIndexPage']


class FoundationIndexPage(Page):
    pass
