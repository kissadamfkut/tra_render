#!/bin/python

from os import sys
from matplotlib import pyplot as plt
import pandas as pd

tra = pd.read_csv(sys.argv[1])
plt.plot(tra["Frequency(Hz)"], tra["Amplitude(dBm)"])
plt.xlabel("Frequency(Hz)")
plt.ylabel("Amplitude(dBm)")

plt.show()
