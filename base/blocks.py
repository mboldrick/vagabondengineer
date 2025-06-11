from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class AlignedImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)
    alignment = blocks.ChoiceBlock(
        choices=[
            ("left", "Float Left"),
            ("right", "Float Right"),
            ("center", "Center"),
        ],
        default="center",
    )
    width = blocks.ChoiceBlock(
        choices=[
            ("1/3", "33%"),
            ("1/2", "50%"),
            ("2/3", "66%"),
            ("full", "100%"),
        ],
        default="full",
    )

    class Meta:
        template = "blocks/aligned_image.html"
        icon = "image"
        label = "Image"


class CodeBlock(blocks.StructBlock):
    language = blocks.ChoiceBlock(
        choices=[
            ("python", "Python"),
            ("javascript", "JavaScript"),
            ("html", "HTML"),
            ("css", "CSS"),
            ("bash", "Bash"),
            ("zsh", "Zsh"),
            ("json", "JSON"),
            ("yaml", "YAML"),
            ("xml", "XML"),
            ("vba", "VBA"),
            ("sql", "SQL"),
            ("text", "Plain text"),
        ],
        default="python",
    )
    code = blocks.TextBlock()
    caption = blocks.CharBlock(required=False)

    class Meta:
        template = "blocks/code_block.html"
        icon = "code"
        label = "Code Block"


class ClearFloatBlock(blocks.StaticBlock):
    class Meta:
        label = "Clear Float"
        template = "blocks/clear_float.html"
        icon = "horizontalrule"


class YouTubeEmbedBlock(blocks.StructBlock):
    video_id = blocks.CharBlock(help_text="YouTube video ID (from URL)")

    class Meta:
        template = "blocks/youtube_embed.html"
        icon = "media"
        label = "YouTube Video"


class CalloutBlock(blocks.StructBlock):
    type = blocks.ChoiceBlock(
        choices=[
            ("info", "Info"),
            ("warning", "Warning"),
            ("success", "Success"),
        ],
        default="info",
    )
    title = blocks.CharBlock(required=False)
    body = blocks.RichTextBlock(features=["bold", "italic", "link"])

    class Meta:
        template = "blocks/callout_block.html"
        icon = "placeholder"
        label = "Callout Box"


class ContentBlock(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock(
        features=[
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "bold",
            "italic",
            "link",
            "document-link",
            "ul",
            "ol",
            "hr",
            "image",
            "blockquote",
            "superscript",
            "subscript",
            "strikethrough",
            "code",
            "embed",
            "style",
        ]
    )
    image = AlignedImageBlock()
    code = CodeBlock()
    clear = ClearFloatBlock()
    youtube = YouTubeEmbedBlock()
    callout = CalloutBlock()
