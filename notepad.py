import csv
name = input("Enter your Name: ")
print("Hello! "+name+".")
while 1:
	print("**NOTES**")
	print("1. Add Notes. ")
	print("2. Read Notes. ")
	print("3. Clear Previous. ")
	choice = input("Enter your choice(1/2/3): ")
	if choice == "1":
		file1 = open("NOTES.txt","a+")
		stl = input("Your NOTE :")
		print (stl)
		file1.writelines(stl+" ; ")
		file1.close()
	if choice == "2":
                '''
		with open("NOTES.txt","r") as csvfile :
			read = csv.reader(csvfile)
			list_d = list(read)
			for items in list_d :
				print(items)
		'''
                file1 = open("NOTES.txt","r")
                hell = file1.read()
                print(hell)
	if choice == "3":
		file1 = open("NOTES.txt","w")
		file1.write(" ")
		file1.close()
		break
