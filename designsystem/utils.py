from wagtail.core import blocks
from wagtailcodeblock.blocks import CodeBlock


STANDARD_STREAMFIELD = [
    ('rich_text', blocks.RichTextBlock(
        label='Rich Text',
        icon='pilcrow'
    )),
    ('code', CodeBlock(
        help_text='For displaying code to the reader of a page.',
        icon='code'
    )),
    ('raw_html', blocks.RawHTMLBlock(
        label='Raw HTML',
        help_text='HTML that will be rendered on the page. Use as a temporary '
                  'solution or last resort for something fancy that has not '
                  'been enabled in a proper Wagtail block yet.',
        icon='placeholder'
    )),
]
