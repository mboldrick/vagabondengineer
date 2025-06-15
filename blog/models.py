from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from base.blocks import ContentBlock  # Import shared blocks from base


class BlogPage(Page):
    intro = models.TextField(
        max_length=300, help_text="A short summary to appear on the homepage and cards."
    )
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    featured = models.BooleanField(
        default=False,
        help_text="Check this box to feature this blog post on the homepage.",
    )
    body = StreamField(ContentBlock(), use_json_field=True, verbose_name="Page body")

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("header_image"),
        FieldPanel("featured"),
        FieldPanel("body"),
    ]


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["posts"] = (
            BlogPage.objects.live().descendant_of(self).order_by("-first_published_at")
        )
        context["featured_posts"] = context["posts"].filter(featured=True)
        return context
