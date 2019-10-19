def dispLeaps(syear, eyear):
    for i in range(syear, eyear+1):
        if (syear%4==0 and syear%100!=0) or (syear%400 == 0):
            print(syear, end = " ")


dispLeaps(100, 2000)
