from PIL import Image
import urllib.request as urllib



def avg_color(url):

    r = urllib.urlopen(url)
    im = Image.open(r)
    r, g, b = im.getpixel((1,2))
    pixels = list(im.getdata())
    div = len(pixels)

    for i in pixels:
        r += (i[0])
        g += (i[1])
        b += (i[2])
    print (int(r/div), int(g/div), int(b/div))
avg_color("https://maps.googleapis.com/maps/api/streetview?size=600x300&location=35.14966,-90.04894&heading=163.9308403&pitch=-10&key=AIzaSyB9HPGnQfbaV4jqtmROoeOMDO3H1A6tgtI")