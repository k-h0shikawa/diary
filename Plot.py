import math
import datetime
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
 
class Plot:
    def __init__(self):
        """
        コンストラクタ
        """
        # 適当にデータを生成
        time_range = 30     # 30日分
        dates = [datetime.datetime(2018,10,1) + datetime.timedelta(days=i) for i in range(time_range)]
        vals = [np.sin(2 * np.pi * i / 240) for i in range(time_range)]

        ax = plt.subplot()
        ax.plot(dates, vals)

        # Formatterでx軸の日付ラベルを月・日に設定
        xfmt = mdates.DateFormatter("%m/%d")

        # DayLocatorで間隔を日数に
        xloc = mdates.DayLocator()


        ax.xaxis.set_major_locator(xloc)
        ax.xaxis.set_major_formatter(xfmt)

        # x軸の範囲
        ax.set_xlim(datetime.datetime(2018,10,1), datetime.datetime(2018,10,10)) 
        ax.grid(True)
        plt.show()
 
    def analyze(self,text = None):
        '''
        感情分析
        Returns:
        --------
            {'label':str,'score':float}  ネガポジの結果と確率を辞書形式で返す   
       
        '''
        return self.nlp(self.document if text is None else text)

if __name__ == "__main__":
    plot = Plot()
