import random
import string
import numpy as np
import pandas as pd
def password1():
  q1 = input("do you want your name in password Y/N  ")

  s1 = string.ascii_uppercase
  s2 = string.ascii_lowercase
  s3 = string.digits
  s4 = string.punctuation

  password = random.choice(s1)+ random.choice(s2)+ random.choice(s3)+ random.choice(s4)
  slen = len(password)

  if(q1 == "N" or q1 == "n"):
  # for non name password
      password_length = int(input("enter the length of password"))
      q2 = input("do you want to add any refrence with password")
      if(q2 == "Y" or q2 == "y" or q2 == "yes" or q2 == "Yes"):
          q3 = input("enter refrence")
          file = open('pass.txt','a+')
          file.write("\n")
          file.write(q3+"-")
          file.write("\n")
      else:
        file = open('pass.txt','a+')
        file.write("\n")
        file.write("untitled -")
        file.write("\n")
      while(slen<password_length):
          password = password +  random.choice(s1)+ random.choice(s2)+ random.choice(s3)+ random.choice(s4)
          slen = len(password)
          a5 = slen - password_length
        
      d = "".join(password[0:(slen - a5)])
      file.write(d)
      file.write("\n")
      print(d)
  elif(q1 == "Y" or q1 ==  "y"):
  # for password with name
      name = input("enter your name  ")
      name_length = len(name)
      a = random.randrange(1, name_length)
      n = 0 
      while(n<a):
          num1 = random.randrange(0, name_length)
          capital = name[num1]
          capital1 = capital.upper()
          name = name.replace(capital, capital1)
          n = n+1
      # print(replace)
      s3 = string.digits
      s4 = string.punctuation
      final_password = []

      final_password.append(name)
      final_password.append(random.choice(s3))
      final_password.append(random.choice(s3))
      final_password.append(random.choice(s3))
      final_password.append(random.choice(s4))
      final_password.append(random.choice(s4))

      random.shuffle(final_password)
      q5 = input("do you want to add any refrence with password")
      if(q5 == "Y" or q5 == "y" or q5 == "yes" or q5 == "Yes"):
          q6 = input("enter refrence")
          file = open('pass.txt','a+')
          file.write("\n")
          file.write(q6+"-")
          file.write("\n")
      else:
        file = open('pass.txt','a+')
        file.write("\n")
        file.write("untitled -")
        file.write("\n")
      c = "".join(final_password)
      print(c)
      file = open('pass.txt','a+')
      file.write(c)
      file.write("\n")
      file.close()
  else:
      print("wrong input please try again")
password1()
while(1):
  a1 = input("do you want to do it again?")
  if (a1 == "Y" or a1 == "y" or a1 == "yes" or a1 == "Yes"):
    password1()  
  else:
    print("ok bye bye")
    break

