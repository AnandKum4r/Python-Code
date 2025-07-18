sentence=input("Enter a sentence : ")
word=input("Enter word which you wants to find from sentence : ")
if(sentence.find(word)==-1):
      print("Word is not found in sentence !")
else:
      print("Word is in sentence!")