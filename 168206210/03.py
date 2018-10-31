def Number(self):
         for num in range(100, 1000):
             geWei = num % 10
             baiWei = int(num / 100)
             shiWei = int((num - baiWei * 100) / 10)
             sum = geWei * geWei * geWei + shiWei * shiWei * shiWei + baiWei * baiWei * baiWei
             if sum == num:
                 print("%d是水仙花数" % num)
