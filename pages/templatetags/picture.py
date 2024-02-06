from django import template

register = template.Library()


@register.inclusion_tag("picture.html")
def picture(name, design_width, design_height, large=False, **sizes_input):
    widths = range(100, 2100, 100)
    extra_widths = range(2200, 4001, 200)
    if large:
        widths = [*widths, *extra_widths]

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

    BREAKPOINTS = {
        "xs": 0,
        "sm": 576,
        "md": 768,
        "lg": 992,
        "xl": 1200,
        "xxl": 1400,
    }

    breakpoints = {}

    for key, value in sizes_input.items():
        if key in BREAKPOINTS:
            breakpoints[key] = value

    sizes = ""

    for key, value in breakpoints.items():
        sizes += "(min-width: " + str(BREAKPOINTS[key]) + "px) " + str(value) + "px, "
    sizes += "calc(100vw - 24px)"

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
