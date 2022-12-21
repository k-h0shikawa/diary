import math
import datetime
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
 
class Plot:
    def __init__(self, x, y):
        """
        コンストラクタ
        """
        plt.plot(x, y);
        plt.show()
 

