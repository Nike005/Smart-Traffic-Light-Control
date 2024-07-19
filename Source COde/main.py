import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator
from keras_preprocessing import image
import numpy as np
import easygui
from keras.models import load_model
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import serial
import time
import tensorflow


my_w = tk.Tk()
sw=my_w.winfo_screenwidth()
sh=my_w.winfo_screenheight()
w=sw-10
print(sw,sh)
my_w.geometry('%dx%d' %(w,sh))  
my_w.title('Traffic Detetction')
my_font1=('times', 18, 'bold')

bg = ImageTk.PhotoImage(file='background2.png')
bgLabel = Label(my_w, image=bg)
bgLabel.place(x=0, y=0)
bgLabel.pack(fill=BOTH,expand=YES)


xl=sw/4
x1=20
print(x1)
x2=(xl*1)+x1
x2=int(x2)
print(x2)
x3=(xl*2)+x1
x3=int(x3)
print(x3)
x4=(xl*3)+x1
x4=int(x4)
print(x4)




b1 = tk.Button(my_w, text='Upload Images', 
   width=20,command = lambda:result(),font=my_font1, activebackground='#22228B', bg='black',fg='yellow')
b1.place(x=x1,y=470, width=250, height=40)
b2 = tk.Button(my_w, text='Upload Images', 
   width=20,command = lambda:result1(),font=my_font1, activebackground='#22228B', bg='black',fg='yellow')
b2.place(x=x2,y=470, width=250, height=40)
b3 = tk.Button(my_w, text='Upload Images', 
   width=20,command = lambda:result2(), font=my_font1,activebackground='#22228B', bg='black',fg='yellow')
b3.place(x=x3,y=470, width=250, height=40)
b4 = tk.Button(my_w, text='Upload Images', 
   width=20,command = lambda:result3(), font=my_font1, activebackground='#22228B', bg='black',fg='yellow')
b4.place(x=x4,y=470, width=250, height=40)

print(tf.__version__)


#lb1 = tk.Button(text = '  ')
#lb1.config(bg = 'black')
#lb1.place(x=140,y=58,height=40,width=30)





get_result=[]

def showresult():
   solution=''
   print(get_result)
   print(len(get_result))
   try:
      if len(get_result)==4:
         if(get_result[0]=="No Traffic"):
            l1="d"
         elif(get_result[0]=="Low Traffic"):
            l1="c"
         elif(get_result[0]=="Medium Traffic"):
            l1="b"
         elif(get_result[0]=="High Traffic"):
            l1="a"


         if(get_result[1]=="No Traffic"):
            l2="d"
         elif(get_result[1]=="Low Traffic"):
            l2="c"
         elif(get_result[1]=="Medium Traffic"):
            l2="b"
         elif(get_result[1]=="High Traffic"):
            l2="a"


         if(get_result[2]=="No Traffic"):
            l3="d"
         elif(get_result[2]=="Low Traffic"):
            l3="c"
         elif(get_result[2]=="Medium Traffic"):
            l3="b"
         elif(get_result[2]=="High Traffic"):
            l3="a"

         if(get_result[3]=="No Traffic"):
            l4="d"
         elif(get_result[3]=="Low Traffic"):
            l4="c"
         elif(get_result[3]=="Medium Traffic"):
            l4="b"
         elif(get_result[3]=="High Traffic"):
            l4="a"

         print(l1,l2,l3,l4)

         
         if(l1=="a" and l2=="a" and l3=="a" and l4=="a"):
            print("a b c d")
            
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"abcd")
            time.sleep(1)
            SerialObj.close()

         
         elif(l1=="a" and l2=="a" and l3=="a" and (l4=="b" or l4=="c" or l4=="d")):
            print("a b c d")

            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"abcd")
            time.sleep(1)
            SerialObj.close()
            

         elif((l1=="a" and l2=="a" and l4=="a") and (l3=="b" or l3=="c" or l3=="d") ):
            print("a b d c")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"abdc")
            time.sleep(1)
            SerialObj.close()
            

         elif((l1=="a" and l2=="a") and (l3=="b" or l3=="c" or l3=="d") and (l4=="b" or l4=="c" or l4=="d")):
            print("a b c d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"abcd")
            time.sleep(1)
            SerialObj.close()
            

         elif((l1=="a" and l3=="a" and l4=="a") and (l2=="b" or l2=="c" or l2=="d") ):
            print("a d b c")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"adbc")
            time.sleep(1)
            SerialObj.close()

         elif((l1=="a" and l3=="a") and (l2=="b" or l2=="c" or l2=="d") and (l4=="b" or l4=="c" or l4=="d")):
            print("a c b d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"acbd")
            time.sleep(1)
            SerialObj.close()


         elif((l1=="a" and l4=="a") and (l2=="b" or l2=="c" or l2=="d") and (l3=="b" or l3=="c" or l3=="d")):
            print("a c d b")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"acdb")
            time.sleep(1)
            SerialObj.close()
         

         elif((l1=="a") and (l2=="b" or l2=="c" or l2=="d") and (l3=="b" or l3=="c" or l3=="d") and (l4=="b" or l4=="c" or l4=="d")):
            print("a b c d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"abcd")
            time.sleep(1)
            SerialObj.close()
         

         elif((l1=="b" or l1=="c" or l1=="d") and (l2=="a") and (l3=="a") and (l4=="a")):
            print("d a b c")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"dabc")
            time.sleep(1)
            SerialObj.close()

         
         elif((l1=="b" or l1=="c" or l1=="d") and (l2=="a") and (l3=="a") and (l4=="b" or l4=="c" or l4=="d")):
            print("c a b d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"cabd")
            time.sleep(1)
            SerialObj.close()

         
         elif((l1=="b" or l1=="c" or l1=="d") and (l2=="a") and (l3=="b" or l3=="c" or l3=="d") and (l4=="a")):
            print("c a d b")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"cadb")
            time.sleep(1)
            SerialObj.close()


         elif((l1=="b" or l1=="c" or l1=="d") and (l2=="a") and (l3=="b" or l3=="c" or l4=="d") and (l4=="b" or l4=="c" or l4=="d")):
            print("b a c d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"bacd")
            time.sleep(1)
            SerialObj.close()


         elif((l1=="b" or l1=="c" or l1=="d") and (l2=="b" or l2=="c" or l2=="d") and (l3=="a") and (l4=="a")):
            print("c d a b")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"cdab")
            time.sleep(1)
            SerialObj.close()


         elif((l1=="b" or l1=="c" or l1=="d") and (l2=="b" or l2=="c" or l2=="d") and (l3=="a") and (l4=="b" or l4=="c" or l4=="d")):
            print("b c a d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"bcad")
            time.sleep(1)
            time.sleep(1)
            SerialObj.close()


         elif((l1=="b" or l1=="c" or l1=="d") and (l2=="b" or l2=="c" or l2=="d") and (l3=="b" or l3=="c" or l3=="d") and (l4=="a")):
            print("b c d a")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"bcda")
            time.sleep(1)
            SerialObj.close()


         elif((l1=="b" or l1=="c" or l1=="d") and (l2=="b" or l2=="c" or l2=="d" ) and (l3=="b" or l3=="c" or l3=="d" ) and (l4=="b" or l4=="c" or l4=="d")):
            print("a b c d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"abcd")
            time.sleep(1)            
            SerialObj.close()
#-------------------------------------------Medium-----------------------------------------------------------------
         elif(l1=="b" and l2=="b" and l3=="b" and l4=="b"):
            print("a b c d")
            
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"abcd")
            time.sleep(1)
            SerialObj.close()
         
         elif(l1=="b" and l2=="b" and l3=="b" and (l4=="c" or l4=="d")):
            print("a b c d")

            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"abcd")
            time.sleep(1)
            SerialObj.close()


         elif((l1=="b" and l2=="b" and l4=="b") and (l3=="c" or l3=="d") ):
            print("a b d c")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"abdc")
            time.sleep(1)
            SerialObj.close()
         

         elif((l1=="b" and l2=="b") and (l3=="c" or l3=="d") and (l4=="c" or l4=="d")):
            print("a b c d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"abcd")
            time.sleep(1)
            SerialObj.close()
         

         elif((l1=="b" and l3=="b" and l4=="b") and (l2=="c" or l2=="d") ):
            print("a d b c")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"adbc")
            time.sleep(1)
            SerialObj.close()


         elif((l1=="b" and l3=="b") and (l2=="c" or l2=="d") and (l4=="c" or l4=="d")):
            print("a c b d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"acbd")
            time.sleep(1)
            SerialObj.close()
         

         elif((l1=="b" and l4=="b") and (l2=="c" or l2=="d") and (l3=="c" or l3=="d")):
            print("a c d b")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"acdb")
            time.sleep(1)
            SerialObj.close()
         

         elif((l1=="b") and (l2=="c" or l2=="d") and (l3=="c" or l3=="d") and (l4=="c" or l4=="d")):
            print("a b c d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"abcd")
            time.sleep(1)
            SerialObj.close()
         

         elif((l1=="c" or l1=="d") and (l2=="b") and (l3=="b") and (l4=="b")):
            print("d a b c")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"dabc")
            time.sleep(1)
            SerialObj.close()

         
         elif((l1=="c" or l1=="d") and (l2=="b") and (l3=="b") and (l4=="c" or l4=="d")):
            print("c a b d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"cadb")
            time.sleep(1)
            SerialObj.close()
            
         
         elif((l1=="c" or l1=="d") and (l2=="b") and (l3=="c" or l3=="d") and (l4=="b")):
            print("c a d b")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"cadb")
            time.sleep(1)
            SerialObj.close()


         elif((l1=="c" or l1=="d") and (l2=="b") and (l3=="c" or l4=="d") and (l4=="c" or l4=="d")):
            print("b a c d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"bacd")
            time.sleep(1)
            SerialObj.close()


         elif((l1=="c" or l1=="d") and (l2=="c" or l2=="d") and (l3=="b") and (l4=="b")):
            print("c d a b")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"cdab")
            time.sleep(1)
            SerialObj.close()


         elif((l1=="c" or l1=="d") and (l2=="c" or l2=="d") and (l3=="b") and (l4=="c" or l4=="d")):
            print("b c a d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"bcad")
            time.sleep(1)
            SerialObj.close()


         elif((l1=="c" or l1=="d") and (l2=="c" or l2=="d") and (l3=="c" or l3=="d") and (l4=="b")):
            print("b c d a")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"bcda")
            time.sleep(1)
            SerialObj.close()


         elif((l1=="c" or l1=="d") and (l2=="c" or l2=="d") and (l3=="c" or l3=="d" ) and (l4=="c" or l4=="d")):
            print("a b c d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"abcd")
            time.sleep(1)
            SerialObj.close()
   





         else:
            print("a b c d")
            SerialObj = serial.Serial('COM3')
            SerialObj.baudrate = 9600
            SerialObj.bytesize = 8
            SerialObj.parity   ='N'
            SerialObj.stopbits = 1
            SerialObj.write(b"abcd")
            time.sleep(1)
            SerialObj.close()

                        



         

         
         


            #else:
            #  pass
            
      else:
         messagebox.showerror('Error','Upload All Files')

      
      
   except Exception as e:
      pass



titleLabel = Label(my_w, text='Traffic Detetction', font=('italic', 22, 'bold '), bg='black',
                   fg='white', )
titleLabel.place(x=0, y=5, width=sw, height=50)



show_result=Button(my_w,text="Show Result", font='italic 17 bold',fg='red',bg='#FFFF45',command=showresult)
show_result.place(x=xl+120, y=580, width=220)

#model1 = load_model('model/Class1/model_Class1.h5')
#model2 = load_model('model/Class2/model_Class2.h5')
#model3 = load_model('model/Class3/model_Class3.h5')


model1 = tensorflow.keras.models.load_model('model/Class1/model_Class1.h5',compile=False)
model1.compile()


model2 = tensorflow.keras.models.load_model('model/Class2/model_Class2.h5',compile=False)
model2.compile()

model3 = tensorflow.keras.models.load_model('model/Class3/model_Class3.h5',compile=False)
model3.compile()



def result():
   try:
      get_result.pop(0)
   finally:
      filename =upload_file1()
      test_image2 = image.load_img(filename, target_size = (64, 64))
      test_image2 = image.img_to_array(test_image2)
      test_image2 = np.expand_dims(test_image2, axis = 0)   
      # cnn prediction on the test image
      result1 = model1.predict(test_image2)
      print(result1)
      result2 = model2.predict(test_image2)
      print(result2)
      result3 = model3.predict(test_image2)
      print(result3)
  

      if result1[0][0] == 0:
         prediction2="No Traffic"
      elif result2[0][0]==0:
         prediction2="Low Traffic"
      elif result3[0][0]==0:
         prediction2="Medium Traffic"
      else:
         prediction2="High Traffic"      
      print(prediction2)
      prediction=prediction2
      get_result.insert(0,prediction)
      return filename
   
def result1():
   try:
      get_result.pop(1)
   finally:
      filename1 =upload_file2()
      test_image2 = image.load_img(filename1, target_size = (64, 64))
      test_image2 = image.img_to_array(test_image2)
      test_image2 = np.expand_dims(test_image2, axis = 0)   
      result1 = model1.predict(test_image2)
      print(result1)
      result2 = model2.predict(test_image2)
      print(result2)
      result3 = model3.predict(test_image2)
      print(result3)

      if result1[0][0] == 0:
         prediction2="No Traffic"
      elif result2[0][0]==0:
         prediction2="Low Traffic"
      elif result3[0][0]==0:
         prediction2="Medium Traffic"
      else:
         prediction2="High Traffic"

      print(prediction2)
      prediction=prediction2
      get_result.insert(1,prediction)
      return filename1
   
def result2():
   try:
      get_result.pop(2)
   finally:
      filename2 =upload_file3()
      test_image2 = image.load_img(filename2, target_size = (64, 64))
      test_image2 = image.img_to_array(test_image2)
      test_image2 = np.expand_dims(test_image2, axis = 0)   
      result1 = model1.predict(test_image2)
      print(result1)
      result2 = model2.predict(test_image2)
      print(result2)
      result3 = model3.predict(test_image2)
      print(result3)
      if result1[0][0] == 0:
         prediction2="No Traffic"
      elif result2[0][0]==0:
         prediction2="Low Traffic"
      elif result3[0][0]==0:
         prediction2="Medium Traffic"
      else:
         prediction2="High Traffic"
      print(prediction2)
      prediction=prediction2
      get_result.insert(2,prediction)
      return filename2
   
def result3():
   try:
      get_result.pop(3)
   finally:
      filename3 =upload_file4()
      test_image2 = image.load_img(filename3, target_size = (64, 64))
      test_image2 = image.img_to_array(test_image2)
      test_image2 = np.expand_dims(test_image2, axis = 0)   
      result1 = model1.predict(test_image2)
      print(result1)
      result2 = model2.predict(test_image2)
      print(result2)
      result3 = model3.predict(test_image2)
      print(result3)
      
      if result1[0][0] == 0:
         prediction2="No Traffic"
      elif result2[0][0]==0:
         prediction2="Low Traffic"
      elif result3[0][0]==0:
         prediction2="Medium Traffic"
      else:
         prediction2="High Traffic"

      print(prediction2)
      prediction=prediction2
      get_result.insert(3,prediction)
      return filename3
   
def upload_file1():
    filename=easygui.fileopenbox()
    img=Image.open(filename) # read the image file
    img=img.resize((200,140)) # new width & height
    img=ImageTk.PhotoImage(img)
    e1 =tk.Label(my_w)
    e1.place(x=x1, y=180, width=240, height=250)
    e1.image = img
    e1['image']=img
    return filename
   
def upload_file2():
    filename=easygui.fileopenbox()
     
    img=Image.open(filename) # read the image file
    img=img.resize((200,140)) # new width & height
    img=ImageTk.PhotoImage(img)
    e1 =tk.Label(my_w)
    e1.place(x=x2, y=180, width=240, height=250)
    e1.image = img
    e1['image']=img
    return filename
   
def upload_file3():
    filename=easygui.fileopenbox()     
    img=Image.open(filename) # read the image file
    img=img.resize((200,140)) # new width & height
    img=ImageTk.PhotoImage(img)
    e1 =tk.Label(my_w)
    e1.place(x=x3, y=180, width=240, height=250)
    e1.image = img
    e1['image']=img
    return filename
   
def upload_file4():
    filename=easygui.fileopenbox() 
    img=Image.open(filename) # read the image file
    img=img.resize((200,140)) # new width & height
    img=ImageTk.PhotoImage(img)
    e1 =tk.Label(my_w)
    e1.place(x=x4, y=180, width=240, height=250)
    e1.image = img
    e1['image']=img
    return filename
   
my_w.mainloop()
