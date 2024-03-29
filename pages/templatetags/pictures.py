from django import template

register = template.Library()


@register.inclusion_tag("picture.html")
def get_picture(name, width):
    widths = [
        100,
        200,
        300,
        400,
        500,
        600,
        700,
        800,
        900,
        1000,
        1100,
        1200,
        1300,
        1400,
        1500,
        1600,
        1700,
        1800,
        1900,
        2000,
    ]
    avif_urls = [
        ["img/gen/" + name + "-" + str(width) + ".avif", width] for width in widths
    ]
    webp_urls = [
        ["img/gen/" + name + "-" + str(width) + ".webp", width] for width in widths
    ]
    jpeg_urls = [
        ["img/gen/" + name + "-" + str(width) + ".jpg", width] for width in widths
    ]

    return {
        "name": name,
        "width": width,
        "avif_urls": avif_urls,
        "webp_urls": webp_urls,
        "jpeg_urls": jpeg_urls,
    }
