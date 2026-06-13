try:
    file=open('task.txt','r')
    print(file.read())
    print(6/0)

except ZeroDivisionError:
    print("you cannot divide numer by 0")

except Exception as e: #make sure the logic is correct
    print(e)

finally:    #this will be executed even if their is error or not
    file.close()
print("hello")