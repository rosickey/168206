def b_s(alist,value):
      n=len(alist)
      mid=n//2
      if n>0:
         if alist[mid]==value:
          return mid
        elif alist[mid]>value:
          return b_s(alist[:mid],value)
        else:
          return b_s(alist[mid+1:],value)
      else:
        return False
      alist=[12,45,46,54,55,67]
      print(b_s(alist,58)
