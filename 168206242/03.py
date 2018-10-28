def printNarcissisticNumber(self, num):
        num = int(num)
        if num < 100 or num > +1000:
            print("不是水仙花数")
        else:
            geWei = num % 10
            baiWei = int(num / 100)
            shiWei = int((num - baiWei * 100) / 10)
            sum = geWei * geWei * geWei + shiWei * shiWei * shiWei + baiWei * baiWei * baiWei
            if sum == num:
                print("%d是水仙花数" % num)
            else:
                print("不是水仙花数")
def printNarcissisticNumber1(self):
        for num in range(100, 1000):
            geWei = num % 10
            baiWei = int(num / 100)
            shiWei = int((num - baiWei * 100) / 10)
   
            sum = geWei * geWei * geWei + shiWei * shiWei * shiWei + baiWei * baiWei * baiWei
            if sum == num:
                print("%d是水仙花数" % num)
