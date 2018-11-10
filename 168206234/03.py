
Skip to content
 
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 @yanglei1155
Sign out
 Watch 5
 Star 53  Fork 67 rosickey/168206
 Code  Issues 0  Pull requests 49  Projects 0  Wiki  Insights
Branch: master Find file Copy path 168206/168206209/01.py
bc116d6  3 days ago
@chenqi4547 chenqi4547 Create 01.py
1 contributor
RawBlameHistory     
33 lines (30 sloc)  680 Bytes
#!/usr/bin/python3
# -- coding: utf-8 -- 
'''二分查找，递归'''
def binary_serach(list, item):
    low=0
    high=len(list)-1
    while low<=high:
        mid=int((low+high)/2)
        guess=list[mid]
        if guess==item:
            return mid
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return None
my_list=[1,3,5,7,9]

def bs3(list,item): 
    mid=len(list)//2
    if list[mid]==item:
        return list[mid]
    if mid==0:
        return 0
    else:
        if item>list[mid]:
            return bs3(list[mid:],item)
        else:
            return bs3(list[:mid],item)
        
lis=[1,3,5,7,9,11,13,15]
print(bs3(lis,13)) 
© 2018 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
Press h to open a hovercard with more details.
