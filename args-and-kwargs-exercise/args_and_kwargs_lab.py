def color_function(
    fore_color="black", back_color="white", link_color="blue", visited_color="red"
):
    colors = [fore_color, back_color, link_color, visited_color]
    print(colors)
    return colors


def color_function_2(*args, **kwargs):
    colors = list(args) + list(kwargs.values())
    print("args = ", args)
    print("kwargs = ", kwargs)
    return colors


if __name__ == "__main__":
    color_function()
    color_function_2()
