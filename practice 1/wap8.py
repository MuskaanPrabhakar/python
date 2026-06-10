#Write a program that accepts a sentence and a word from the user. Print: how many times the word appears, at what character position it first appears, and the sentence with that word replaced by "*".
sentence = input("Write a sentence: ")
ch= input("Write a word: ")
appears=0
sentence=sentence.split()
for i in range(0, len(sentence)):
    if(sentence[i]==ch):
       if(appears==0):
           print("It first appears in ", i+1)
       appears+=1
       sentence[i]="*"
sentence= " ".join(sentence)
print(sentence)