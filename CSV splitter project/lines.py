import csv

filename = "output.csv"
num_lines = 5000  # Extract 'n' lines
input=open(r"C:\Users\chira\OneDrive\Desktop\python.csv", "r")
reader = csv.reader(input)
value = len(list(reader))
key=value/num_lines
print(key)


with open(r"C:\Users\chira\OneDrive\Desktop\python.csv", "r") as input_file, open(filename, "w", newline="") as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    for i in range(num_lines):
        if i<2:
            row = next(reader)
            writer.writerow(row)
        elif i>2:
            print("done")
            break

