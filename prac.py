# Given the following list what does the following slicing operation return [0,6]
sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)

# What is the output of the slicing [-2],[-4:-1] from following list 
sampleList = [10, 20, 30, 40, 50]
print(sampleList[-2])
print(sampleList[-4:-1])

# Add the number 60 to the list below?
sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
print(sampleList)

# Remove the last element in the list given?

sampleList = [10, 20, 30, 40, 50]
sampleList.pop()
print(sampleList)


#  Given the list below multiple each element by 2

aList = [1, 2, 3, 4, 5, 6, 7]
pow2 =  [2 * x for x in aList]
print(pow2)

# Given the following list "listOne",add "listTwo" to it to join them

listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'f', 'g']

newList = listOne + listTwo
print(newList)

# What is the output of the following number slicing operations[2:5],[:4],[3:]

aList = [10, 20, 30, 40, 50, 60, 70, 80]
print(aList[2:5])
print(aList[:4])
print(aList[3:])

# Given the variables; name="Bob", age=25,
# print the formatted sentence 
# Hi, my name is BOB. and I was am 25 years old

name="Bob"
age=25

print(f"Hi, my name is {name.upper()} and I am {age} years old")



