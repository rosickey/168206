def seach(seq ,number  ):
    lower=0
    upper=len(seq )-1     
    mid=(seq [lower]+seq [upper])//2
    if number==seq [mid]:
        return mid
    elif number>seq [mid]:
        lower=mid+1
        return seach(seq , number)
    elif number<seq [mid]:
        upper=mid
        return seach(seq , number)
    else:
        return False
seq=range(0,100)
print(seach(seq ,33))。
