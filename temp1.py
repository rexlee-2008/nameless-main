암혼천심자, 방산수
minecraft\:normal
dlckdrmsrexlee2008@naver.com
dlckdrmsrexlee9228@gmail.com


from collections import deque
n=int(input())
m=int(input())
arr=[]
temp=[]
for i in range(n):
   t1=[]
   t2=[]
   for j in input():
      t1.append(j)
      t2.append(0)
   arr.append(t1)
   temp.append(t2)
for k in range(m):
   l=temp
   print()
   for q in l:
      print(q)
   print()
   for q in range(len(arr)):
      for p in range(len(arr[q])):
         l[q][p]=arr[n-p-1][q]
   print()
   for q in l:
      print(q)
   print()
   arr=[]
   for i in range(len(l)):
      if l[i]!=["."]*n:
         flag=0
         for j in range(len(l[i])-1,-1,-1):
            if l[i][j]!=".":
               d=deque(l[i])
               d.rotate(j+1)
               arr.append(list(d))
               flag=1
               break
         if flag==0:
            arr.append(l[i])
      else:
         arr.append(l[i])
      #print(list(d))
   for q in arr:
      print(q)
   print()
#or i in l:
   #print(i)
'''
7
2
.......
.......
...A...
...B...
..ACA..
..BBB..
.AAAAA.
'''