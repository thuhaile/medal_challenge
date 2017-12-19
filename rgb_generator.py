import urllib2
from pylab import imshow, show, get_cmap
from numpy import random
import numpy as np

class RandomGenerator():
    def __init__(self, url):
        self.url = url

    def get_randoms(self):
        response = urllib2.urlopen(self.url)
        text = response.read()
        return [int(i) for i in text.split()]

class RGBImage():
    def __init__(self, randoms, size):
        self.randoms = randoms
        self.size = size

    def to_matrix(self, l, n):
        return [l[i:i+n] for i in xrange(0, len(l), n)]

    def show(self):
        Z = np.array(self.to_matrix(self.randoms, self.size))
        imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest')
        show()

url = 'https://www.random.org/integers/?num=2500&min=1&max=50&col=50&base=10&format=plain&rnd=new'
rd = RandomGenerator(url)
rgb_image = RGBImage(rd.get_randoms(), 50)
rgb_image.show()
