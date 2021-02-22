import pandas as pd
import numpy as np

from collections import Counter, OrderedDict
from config import filename_all

def main():
    
    df = pd.read_excel(filename_all)
    
    for i in range(1,10):
        print(i)
        draw_holder = []
        count_key = []
        filter_draw = list(df[df['Winning Numbers'].str.contains('0' + str(i))]['Winning Numbers'])
        list_split = [item.split(',') for item in filter_draw]
        for item in list_split:
            draw_holder.extend(item)
        draw_holder = list(map(int,draw_holder))
        counter = Counter(draw_holder)
        ordered_count = OrderedDict(sorted(counter.items()))
        for key, value in ordered_count.items():
            count_key.append(key)
        if len(set(list(np.linspace(1,42,num=42))).difference(set(count_key))) == 0:
            print("Equal")
        else:
            print("Unequal")
    
    for i in range(10, 43):
        print(i)
        draw_holder = []
        count_key = []
        filter_draw = list(df[df['Winning Numbers'].str.contains(str(i))]['Winning Numbers'])
        list_split = [item.split(',') for item in filter_draw]
        for item in list_split:
            draw_holder.extend(item)
        draw_holder = list(map(int,draw_holder))
        counter = Counter(draw_holder)
        ordered_count = OrderedDict(sorted(counter.items()))
        for key, value in ordered_count.items():
            count_key.append(key)
        if len(set(list(np.linspace(1,42,num=42))).difference(set(count_key))) == 0:
            print("Equal")
        else:
            print("Unequal")
    
if __name__ == "__main__":
    main()