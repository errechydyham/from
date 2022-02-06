#get the file and read it 
name = input("Enter file name: ") 
text = open(name, "r")

#print the emails and count them 
count = 0 

for line in text: 
    x = line.split()

    if line.startswith("From"): 
        count += 1 
        print(x[1]) 

#print the number of emails 
print("Number of lines that starts with From is : ", count)