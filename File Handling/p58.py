#Read Mode
try:
 filename=input("Enter File Name : ")
 file=open(filename,"r")
 content=file.read()
 print(content)
 file.close()
 print("Data Received From File")
except FileNotFoundError:
	print("Pagal ho kya sahi file input karo !!")