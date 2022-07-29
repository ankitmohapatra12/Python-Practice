# import re
# f = open('data.txt','r')
# 
# 
# # for line  in f :
# #     print(line)
# print(f.read(100))
# 
# l = (e**2 for e in [1,2,3,4]) 
# print(re.findall("[ca+t]","cat caat"))



# Ex = "we will conquer the covid-19"
# 
# l = Ex.split()
# str=""
# for i in l[::-1] :
#     str+=i+" "
# str = "Python is great and Java is also great"
# 
# list = str.split()
# list2=[]
# 
# for ch in list:
#     if ch not in list2:
#         list2.append(ch)
#     else:
#         continue
#     
# 
# 
# print(' '.join(list2))

#Expected o/p ="covid-19 the conquer will we"



# def ispalindrome(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False
# 
# 
# 
# 
# 
# if __name__ == "__main__":
#      
#     s = "ABC"
#     cnt = 0
#     flag = 0
#      
#     while(len(s) > 0):
#      
#        
#         if(ispalindrome(s)):
#             flag = 1
#             break
#          
#         else:
#             cnt += 1
#          
#             
#             s = s[:-1]
#             
#   
#     if(flag):
#         print(s)



# a=[1,3,5]
# 
# b=[2,4,0]
# l = a+b
# 
# n = len(l)
# sorted = []
# max=0
# i=0
# while i<n:
#     
#     for ch in l:
#     
#         if ch > max:
#             max=ch
#         else:
#             continue
#     
#     l.remove(max)
#     sorted.append(max)
#     i+=1
#     max=0
#     
# print(sorted[::-1])
#





a=["a","b","c"]
b=[1,2,3]
dic = {}
for i in range(3):
    dic[a[i]] = b[i]
    
print(dic)
    
        
        
        
        
        