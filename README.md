# Palette
A Python utility to create color palettes based off of an image. Uses k-means clustering to generate eight different RGB shades based off of the predominant colors of the source image.

Tested for Python 3.7, but should work for Python 3.2+

# How To Use

Download/clone somewhere on your computer and download the requirements in the [Pipfile](https://pipenv.readthedocs.io/en/latest/). Put the source image in the same directory and then run the program with python. Run it with the following command line arguments:

```
usage: palette.py [-h] [-s [image source]] [-n [number of colors]]

Generate a color palette based on a source image.

optional arguments:
  -h, --help            show this help message and exit
  -s [image source], --src [image source]
                        Path to the source image (default: None)
  -n [number of colors], --number [number of colors]
                        Number of colors in the palette (default: 8)
```

If an image source isn't provided in a command line argument, the program will ask you for one upon invocation.

Using values of *n* greater than ~16 will produce mediocre results. The suggested (and default) value is 8, but play around with the number depending on your source image.

In a few seconds it will display the palette, which you can then save wherever.
