from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from base.blocks import ContentBlock  # Import shared blocks from base


class AboutPage(Page):
    max_count = 1  # Limit to a single About page
    parent_page_types = ["home.HomePage"]

    body = StreamField(ContentBlock(), use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "About Page"
