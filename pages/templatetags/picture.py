from django import template

register = template.Library()


@register.inclusion_tag("picture.html")
def picture(name, id, design_width, design_height, widths="", sizes=""):
    img_path = "https://imagedelivery.net/JfsbyIUZYacdu7Ymh8jh3A/"
    pic_path = img_path + id
    path = pic_path + "/w=" + str(design_width)
    if widths:
        if not sizes:
            sizes = "(max-width: 600px) 100vw, " + str(design_width) + "px"

    gen_widths = []
    if widths:
        gen_widths = widths.split(",")

    print(name + ": " + path)
    print(gen_widths)
    print("\n")
    srcset = ""
    for width in gen_widths:
        srcset += pic_path + "/w=" + width + " " + width + "w, "

    return {
        "name": name,
        "path": path,
        "design_width": design_width,
        "design_height": design_height,
        "srcset": srcset,
        "sizes": sizes,
    }
