from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    hero_heading = models.CharField(max_length=100, default="")
    hero_tagline = models.TextField(default="")
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero Image",
    )
    about_me = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("hero_heading"),
        FieldPanel("hero_tagline"),
        FieldPanel("hero_image"),
        FieldPanel("about_me"),
    ]
