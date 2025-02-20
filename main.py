codeFile = open("code.py", "r")
code = codeFile.read()
codeFile.close()
print(code)

code = """low_variable = 10
high_variable = 10
method = "all"
character = 'c'
#// # # Method Character
#// 1 10 all !

print("enter your command on one line, space between each element")
print("please use the format: lowerNum HigherNum Method Character")
command = input("Enter Command here: ")
low_variable, high_variable, method, character = command.split()
a = int(low_variable)
b = int(high_variable)
i = a - 1
for num in range (a, b + 1):
  i = i + 1
  if "all" in method:
    if i%2 == 0:
      print(i," is even", " ", end = '')
      print(character*i, end = '')
      print("")
    else:
      print(i," is odd", " ", end = '')
      print(character*i, end = '')
      print("")
  elif "even" in method:
    if i%2 == 0:
      print(i," is even", " ", end = '')
      print(character*i, end = '')
      print("")
  elif "odd" in method:
    if i%2 != 0:
      print(i," is odd", " ", end = '')
      print(character*i, end = '')
      print("")
  else:
    print("please try again")

"""

print(code)