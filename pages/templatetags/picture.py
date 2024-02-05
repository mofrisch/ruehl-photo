from django import template

register = template.Library()


@register.inclusion_tag("picture.html")
def picture(name, design_width, design_height, sizes):
    widths = range(100, 3100, 100)
    avif_urls = [
        ["img/gen/" + name + "-" + str(width) + ".avif", width] for width in widths
    ]
    webp_urls = [
        ["img/gen/" + name + "-" + str(width) + ".webp", width] for width in widths
    ]
    jpeg_urls = [
        ["img/gen/" + name + "-" + str(width) + ".jpg", width] for width in widths
    ]
    img_url = "img/gen/" + name + "-" + str(design_width) + ".jpg"

    return {
        "name": name,
        "design_width": design_width,
        "design_height": design_height,
        "avif_urls": avif_urls,
        "webp_urls": webp_urls,
        "jpeg_urls": jpeg_urls,
        "img_url": img_url,
        "sizes": sizes,
    }
