import csv
with open('python.csv') as input:
    reader = csv.reader(input)
    value = len(list(reader))
    print("line length is " +str(value))


with open('python.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)


def toWrite(rows,low,high,num,min,max,list):
    
    filename= "output"+str(num)+".csv"
    
    with open(filename, "w", newline="") as output_file:
        writer = csv.writer(output_file)
       
        if high>max:
         #   print("high is "+str(high))
         #   print("max is "+str(max))
         #   print("low is "+str(low))
            for i in range(low,max):
                writer.writerow(rows[i])
        elif low==list[0] and high==list[0]:
            for i in range(low):
                writer.writerow(rows[i])
        else:
            for i in range(low,high):
                writer.writerow(rows[i])





list=[]

num1=value
num2=5000


i = 0
j=1
while i < num1:

  list.append(num2*j)
  j+=1

  i +=num2
print("list is")
print(list)

list_leng=len(list)
min=list[0]
max=value
zero=0
toWrite(rows,list[0],list[0],zero,min,max,list)
for j in range(list_leng-1):
    
    toWrite(rows,list[j],list[j+1],j+1,min,max,list)

