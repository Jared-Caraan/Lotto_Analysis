import pandas as pd

from config import filename_odd_even


def main():
    
    even = 0
    odd = 0
    zero_even = 0
    one_even = 0
    two_even = 0
    three_even = 0
    four_even = 0
    five_even = 0
    six_even = 0
    
    df = pd.read_excel(filename_odd_even)
    
    for i in range(len(df)):
        val = str(df.loc[i,"Odd_Even"])
        pattern_list = list(val.split("-"))
        
        for i in pattern_list:
            if i == "even":
                even += 1
            else:
                odd += 1
        
        if even == 0 and odd == 6:
            zero_even += 1
        elif even == 1 and odd == 5:
            one_even += 1
        elif even == 2 and odd == 4:
            two_even += 1
        elif even == 3 and odd == 3:
            three_even += 1
        elif even == 4 and odd == 2:
            four_even += 1
        elif even == 5 and odd == 1:
            five_even += 1
        else:
            six_even += 1
        
        even = 0
        odd = 0
    
    print("0 Even - 6 Odd: " + str(zero_even))
    print("1 Even - 5 Odd: " + str(one_even))
    print("2 Even - 4 Odd: " + str(two_even))
    print("3 Even - 3 Odd: " + str(three_even))
    print("4 Even - 2 Odd: " + str(four_even))
    print("5 Even - 1 Odd: " + str(five_even))
    print("6 Even - 0 Odd: " + str(six_even))

if __name__ == "__main__":
    main()