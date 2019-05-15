from django.db import models
from django.forms import ChoiceField

from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel, ObjectList, StreamFieldPanel, TabbedInterface
)
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from designsystem.utils import STANDARD_STREAMFIELD


class ComponentPage(Page):
    h1 = models.CharField(
        blank=True,
        max_length=100,
        help_text='If you want the main heading on the page to say something '
                  'other than the above title field, enter it here.'
    )
    overview = StreamField(STANDARD_STREAMFIELD, blank=True)
    usage = StreamField(STANDARD_STREAMFIELD, blank=True)
    design = StreamField(STANDARD_STREAMFIELD, blank=True)
    code = StreamField(STANDARD_STREAMFIELD, blank=True)
    accessibility = StreamField(STANDARD_STREAMFIELD, blank=True)
    status = models.CharField(
        max_length=32,
        choices=[
            ('proposed', 'Proposed'),
            ('in_progress', 'In progress'),
            ('beta', 'Beta'),
            ('released', 'Released'),
        ],
        default='proposed'
    )
    thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    overview_panels = Page.content_panels + [
        FieldPanel('h1'),
        StreamFieldPanel('overview'),
    ]
    usage_panels = [
        StreamFieldPanel('usage'),
    ]
    design_panels = [
        StreamFieldPanel('design'),
    ]
    code_panels = [
        StreamFieldPanel('code'),
    ]
    accessibility_panels = [
        StreamFieldPanel('accessibility'),
    ]
    settings_panels = Page.settings_panels + [
        FieldPanel('status'),
        ImageChooserPanel('thumbnail'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(overview_panels, heading='Overview'),
        ObjectList(usage_panels, heading='Usage'),
        ObjectList(design_panels, heading='Design'),
        ObjectList(code_panels, heading='Code'),
        ObjectList(accessibility_panels, heading='Accessibility'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(settings_panels, heading='Settings', classname='settings'),
    ])

    parent_page_types = ['components.ComponentIndexPage']


class ComponentIndexPage(Page):
    parent_page_types = ['home.HomePage']

    def get_context(self, request):
        # Include only published ComponentPages, ordered alphabetically
        context = super().get_context(request)
        componentpages = self.get_children().live().order_by('title')
        context['componentpages'] = componentpages
        return context

    class Meta:
        verbose_name = 'Component Index Page'
