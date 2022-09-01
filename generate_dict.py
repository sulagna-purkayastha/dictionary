# Q3. Write a Python script to generate and print a dictionary that contains a number (between 1
# and n) in the form (x, x*x).
# Sample input ( n = 5) :
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.

key = int(input("enter input"))
d=dict()
for i in range(1,key+1):
 d[i]=i*i
print(d) 