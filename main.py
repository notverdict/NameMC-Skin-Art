from PIL import Image

class NameMC(object):
    def __init__(self, filename):
        self.im = Image.open(filename)
        self.currentfilename = 28

    def run(self):
        _width, _height = self.im.size
        height = _height // 3
        width = _width // 9
        for y in range(0, 3):
            for x in range(0, 9):
                box = (x * width, y * height, (x + 1) * width, (y + 1) * height)
                a = self.im.crop(box)
                background = Image.open("head.png")
                background.paste(a, (8, 8), a)
                self.currentfilename = self.currentfilename - 1
                background.save(f'{str(self.currentfilename)}.png', "PNG")
        input('Done.')

if __name__ == "__main__":
    filename = input('Filename: ')
    Run = NameMC(filename)
    Run.run()
