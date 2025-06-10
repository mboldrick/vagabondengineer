from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class AboutPage(Page):
    max_count = 1  # Limit to a single About page
    parent_page_types = ["home.HomePage"]

    body = StreamField(
        [
            ("paragraph", blocks.RichTextBlock(features=["bold", "italic", "link"])),
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
