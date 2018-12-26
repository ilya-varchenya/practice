class WebEl:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __get__(self, instance, owner):
        self.drv = instance.drv
        return self

    def __inner(self):
        self.drv += 1

    def outer(self):
        self.__inner()
        return self.a


class Page:
    el1 = WebEl(4, 6)

    def __init__(self, drv):
        self.drv = drv

    def click(self):
        self.el1.outer()


p = Page(6)
print(p.click())