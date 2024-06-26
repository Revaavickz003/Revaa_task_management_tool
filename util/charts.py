weeks = [
    "Monday", "Tuesday", "Wednesday", "Tuesday",
    "Friday", "Saturday", "Sunday"
]
colorPalette = ["#55efc4", "#81ecec", "#a29bfe", "#ffeaa7", "#fab1a0", "#ff7675", "#fd79a8"]
colorPrimary, colorSuccess, colorDanger = "#092C74", colorPalette[0], colorPalette[5]


def get_week_dict():
    week_dict = dict()

    for week in weeks:
        week_dict[week] = 0
    return week_dict


def generate_color_palette(amount):
    palette = []

    i = 0
    while i < len(colorPalette) and len(palette) < amount:
        palette.append(colorPalette[i])
        i += 1
        if i == len(colorPalette) and len(palette) < amount:
            i = 0

    return palette