#!/usr/bin/env python
# coding: utf-8

# # BMI CALCULATOR 
# The Body Mass Index is calculated from weight and Height of a person

# In[1]:


Height=float(input("Enter your Height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)
if(BMI>0):
        if(BMI<=16):
                print("you are severely underweight")
        elif(BMI<=18.5):
                print("you are uderweight")
        elif(BMI<=25):
                print("you are Healthy")
        elif(BMI<=30):
                print("you are overweight")
        else: print("you are severely overweight")


# In[ ]:




