input_of_the_user = str(input("Please input something that we all would like to hear: "))


openfile = open('names.txt', 'w')
openfile.write(input_of_the_user)
openfile.close()

openfile = open('names.txt', 'r')
print(openfile.readlines())
openfile.close()