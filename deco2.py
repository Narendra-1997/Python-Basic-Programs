def str_div(div):
    def func(a, b):
        if type(a) == str and type(b) == str:
            return div(a, b)
        else:
            print("str error")
    return func


@str_div
def div(a, b):
    print(a+b)
div(20,"30")
