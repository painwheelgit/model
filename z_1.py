import math
import os
import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
f = []
x = []


def foo(perem) -> float:
    return -math.cos(perem) * math.cos(math.pi) * math.exp(-pow((perem - math.pi), 2))


data = ET.Element('data')
element1 = ET.SubElement(data, 'xdata')
element2 = ET.SubElement(data, 'ydata')
rangeNp = np.arange(-100, 100, 0.01)
for i in rangeNp:
    f.append(foo(i))
    s_elem1 = ET.SubElement(element1, 'x')
    s_elem1.text = str(i)
    s_elem2 = ET.SubElement(element2, 'y')
    s_elem2.text = str(foo(i))
    x.append(i)
b_xml = ET.tostring(data)
bs_data = BeautifulSoup(b_xml, 'xml')
filename = "results/GFG.xml"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as file:
    file.write(bs_data.prettify())
plt.plot(x, f)
plt.show()
