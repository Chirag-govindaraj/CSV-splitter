list=[]

num1=10
num2=3


i = 0
j=1
while i < num1:

  list.append(num2*j)
  j+=1

  i +=num2

print(list)



for j in range(len(list)-1):
    

        for i in range(list[j],list[j+1]):
            print(i)

