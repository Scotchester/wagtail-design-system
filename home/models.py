from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    # Sets page to only be createable at the root
    parent_page_types = ['wagtailcore.Page']
