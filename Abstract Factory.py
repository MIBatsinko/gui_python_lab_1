from abc import ABCMeta

# Abstract Factory
class StandardFactory(object):
    def get_factory(factory):
        if factory == 'light color':
            return LightFactory()
        elif factory == 'dark color':
            return DarkFactory()

# Factory
class LightFactory(object):
    def get_light_color(self):
        return LightColor();

class DarkFactory(object):
    def get_dark_color(self):
        return DarkColor();

# Products
class LightColor(object):
    def set_color(self):
        return 'White color'

class DarkColor(object):
    def set_color(self):
        return 'Black color'

if __name__ == "__main__":
    factory = StandardFactory.get_factory('light color')
    color = factory.get_light_color()
    print(color.set_color())

    factory = StandardFactory.get_factory('dark color')
    color = factory.get_dark_color()
    print(color.set_color())
