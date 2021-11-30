# wk8ex1.py
# Practicum 8
#
# Naam:
#

# laat deze importregel staan...
from png import *


#
# een testfunctie...
#
def test_fun():
    """ algorithmic image-creation one pixel at a time...
        this is a test function: it should output
        an image named test.png in the same directory
    """
    im = PNGImage(300, 200)  # maak een afbeelding met width=300, height = 200

    # Geneste lussen!
    for r in range(200):  # lust over de rijen met lusvariabele r
        for c in range(300):  # lust over de kolommen met c
            if c == r:
                im.plot_point(c, r, (255, 0, 0))
            # else:
            #    im.plot_point( c, r, (255,0,0))

    im.save_file()


def mult(c, n):
    """mult geeft c * n maar met gebruik van een for loop en addition

    Args:
        c (float): een float die we n keer gaan optellen
        n (int): positieve int
    """
    result = 0
    for i in range(n):
        result += c
        print(result)
    return result

assert mult(3, 5) == 15
assert mult(6, 7) == 42
assert mult(1.5, 28) == 42.0


def update(c, n):
    """update de basisstap van de mandelbrotverzameling

    Args:
        c (int): constante c
        n (int): aantal herhalingen
    """
    