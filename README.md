# Python  &nbsp; <a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>

### [1.&nbsp;) &nbsp;&nbsp; Introduction 🔗](https://realpython.com/)
-  &nbsp; Python ใช้ทำอะไรได้บ้าง ?

        1.  ใช้ทำโปรแกรมแบบมี GUI  :  ใช้ library เช่น Tkinter , PyGTK , PyQT , JPython , Kivy , wxPython , ...
        2.  ใช้ทำเกม  :  ใช้ library เช่น pygame
        3.  ใช้ในงานสาย Data Science  :  ใช้ library เช่น pandas , Numpy , seaborn , mathplotlib
        4.  ใช้ในงานสาย IoT (Internet of Thing)  :  Arduino , ทำ Robot , Raspberry pi
        5.  ใช้ทำ web  :  ใช้ library เช่น Django , Flask

- &nbps; เริ่มใช้ Python ยังไง ?

        1.  install python  :  คือ โปรแกรมแปลภาษาไพธอนเป็นภาษาเครื่อง เราก็จะสามารถเขียนไพธอนด้วย editor/IDE
            แล้วรันดูผลลัพธ์ได้
  
        2.  install editor  :  มีให้เลือกใช้เยอะมาก เช่น vscode (นิยมใช้สำหรับผู้เริ่มต้น), pycharm , Google colab
            (นิยมใช้สำหรับผู้เริ่มต้น สะดวกมากใช้บนเว็บได้เลย แค่มีบัญชี Google ), sublimetext (สำหรับคนใช้ mac) ,
            Jupyter (นิยมใช้ในงาน data science) , Spyder (อาจารย์ชอบใช้สอนตามมหาลัยสาย data science ทำ ML)

        โดยภาษา Python จะสามารถ Run ได้ 2 แบบ
        1.  Interpreter  :  การรันแบบ interpret คือการ run ที่ละบรรทัด เหมาะใช้ในงาน Data science
        2.  Compliler  :  การรันแบบ compile คือการที่เราเขียนเป็นไฟล์แล้ว run ทั้งหมดทีเดียว

<br/><br/>

### [1.&nbsp;) &nbsp;&nbsp; Python &nbsp;Syntax 🔗](https://www.w3schools.com/python/)
-  &nbsp; PYTHON &nbsp;BASIC
  
   -  &nbsp; syntax &nbsp;:&nbsp; ```indent สำคัญมาก เพราะ ไม่ใช้ {} และ ; ในการแบ่งบล็อคโค้ดเหมือนภาษาอื่น``` <br/>&nbsp;&nbsp; ```หลังเงื่อนไข (condition) มี : (colon)เสมอ เช่น เงื่อนไข if-else , เงื่อนไข loop``` <br/>&nbsp;&nbsp; ```เป็น Dynamic Programming ไม่ต้องระบุ Data type เหมือนภาษา java```
     
   -  &nbsp; input &nbsp;:&nbsp; ```x = input('Enter your name:')```
     
   -  &nbsp; output &nbsp;:&nbsp; ```print("Hello World !")```
     
   -  &nbsp; Math &nbsp;:&nbsp; ```x = min(5, 10, 25)``` &nbsp;&nbsp; ```x = max(5, 10, 25)``` &nbsp;&nbsp; ```x = pow(4, 3)``` &nbsp;&nbsp; ```x = math.sqrt(64)``` &nbsp;&nbsp; ```x = math.pi``` <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```y = math.floor(1.4)```&nbsp;&nbsp; ```x = math.ceil(1.4)```
     
   -  &nbsp; condition &nbsp;:&nbsp; ```if b > a:``` &nbsp;&nbsp; ```elif a == b:``` &nbsp;&nbsp; ```else:``` &nbsp;&nbsp; ``` TERNARY OPERATOR : print("A") if a > b else print("B")```
     
   -  &nbsp; loop &nbsp;:&nbsp; ```while``` &nbsp;&nbsp; ```ARRAY-LOOP : for x in array:``` &nbsp;&nbsp; ```break``` &nbsp;&nbsp; ```continue```
     
   -  &nbsp; ในภาษา python มีชนิดข้อมูล (Data type) อะไรบ้าง ? &nbsp;:&nbsp;  ```String``` &nbsp;&nbsp; ```Tuple``` &nbsp;&nbsp; ```List``` &nbsp;&nbsp; ```Set``` &nbsp;&nbsp; ```Dictionary``` &nbsp;&nbsp; ```Boolean``` &nbsp;&nbsp; ```Integer```&nbsp;&nbsp; ```Double```
     
   -  &nbsp; Array &nbsp;:&nbsp; ```python ไม่มี Array แต่สามารถใช้ List เป็น Array ได้``` &nbsp;&nbsp; ```CREATE : cars = ["Ford", "Volvo", "BMW"]``` &nbsp;&nbsp; ```ACCESS : x = cars[0]``` &nbsp;&nbsp; ```ARRAY-LENGHT : x = len(cars)``` &nbsp;&nbsp; ```EDIT : cars[0] = "Toyota"``` &nbsp;&nbsp; ```INSERT : cars.append("Honda")``` <br/>&nbsp;&nbsp; ```DELETE : cars.remove("Volvo")```
     
   -  &nbsp; Tuple &nbsp;:&nbsp; ```CREATE : mytuple = ("apple", "banana", "cherry")``` &nbsp;&nbsp; ```CHECK TYPE : print(type(thistuple))``` <br/>&nbsp;&nbsp; ```ACCESS : print(thistuple[1]) OR print(thistuple[2:5])``` &nbsp;&nbsp; ```EDIT : y[1] = "kiwi"``` &nbsp;&nbsp; ```ADD : y.append("orange")``` <br/>&nbsp;&nbsp; ```DELETE : y.remove("apple")``` &nbsp;&nbsp; ```ARRAY-LOOP : for i in range(len(thistuple)):``` 
     
   -  &nbsp; List &nbsp;:&nbsp; ```CREATE : mylist = ["apple", "banana", "cherry"]``` &nbsp;&nbsp; ```ACCESS : print(thislist[1]) OR print(thislist[2:5])``` <br/>&nbsp;&nbsp; ```CHECK-IF-EXIST-IN-LIST : if "apple" in thislist: print("Yes")``` &nbsp;&nbsp; ```EDIT : thislist[1] = "blackcurrant"``` <br/>&nbsp;&nbsp; ```2LIST-CONCAT : thislist.extend(thistuple)``` &nbsp;&nbsp; ```ADD : thislist.insert(2, "watermelon") OR thislist.append("orange")``` 
  
   -  &nbsp; String &nbsp;:&nbsp; ```print(len(str))``` &nbsp;&nbsp; ```print("free" in txt)``` &nbsp;&nbsp; ```print("expensive" not in txt)``` &nbsp;&nbsp; ```SLICING : print(b[2:5])``` <br/>&nbsp;&nbsp; ```ลบ whitespacce หัวท้าย : print(a.strip())``` &nbsp;&nbsp; ```print(str.replace("H", "J"))``` &nbsp;&nbsp; ```แยกคำด้วย , : print(str.split(","))``` 
     
   -  &nbsp; lampda &nbsp;:&nbsp; ```คือฟังก์ชั่นที่ไม่ต้องประกาศชื่อ เป็นการเขียนฟังก์ชั่นแบบ shorthand คล้ายๆ arrow function ในภาษา js แต่มีได้แค่ expression เดียว``` &nbsp;&nbsp; ```รับ a,b เข้ามาหาผลคูณเก็บใน x : x = lambda a, b : a * b``` 
     
   -  &nbsp; File &nbsp;:&nbsp;

<br/>

- &nbsp; PYTHON &nbsp;OOP
  - &nbsp; Function &nbsp;:&nbsp;
  - &nbsp; Class &nbsp;:&nbsp;
  - &nbsp; Inheritance &nbsp;:&nbsp;
  - &nbsp; Polymorphism &nbsp;:&nbsp;
 
<br/>

- &nbsp; PYTHON &nbsp;DATABASE
  - &nbsp; MySQL &nbsp;:&nbsp;
  - &nbsp; MongoDB &nbsp;:&nbsp;
 
<br/>

- &nbsp; PYTHON &nbsp;GUI
  - &nbsp; TKinter &nbsp;:&nbsp;
  - &nbsp; PyQT &nbsp;:&nbsp;
 
<br/>

- &nbsp; PYTHON &nbsp;WEB
  - &nbsp; Django คืออะไร ? &nbsp;:&nbsp;
  - &nbsp; Flask คืออะไร ? &nbsp;:&nbsp;
  - &nbsp; web scrapping คืออะไร ? &nbsp;:&nbsp;
  - &nbsp; API คืออะไร ? &nbsp;:&nbsp;
 
<br/>

- &nbsp; PYTHON &nbsp;DATA &nbsp;SCIENCE
  - &nbsp; Data Sciencetist ต่างจาก AI Engineer ยังไง ? &nbsp;:&nbsp; 
  - &nbsp; Data Engineer &nbsp;:&nbsp; pandas , spark , ci-cd
  - &nbsp; Data Analyst &nbsp;:&nbsp; mathplotlib , Numpy

<br/><br/>

### 3.&nbsp;) &nbsp;&nbsp; Python &nbsp;Exercise 
- &nbsp; Beginner &nbsp;Level &nbsp;( เป็นโจทย์เหมาะสำหรับฝึกใช้คำสั่งพื้นฐานให้คล่อง ให้คุ้นเคยกับ syntax ) &nbsp;:&nbsp;
  - [w3resource](https://www.w3resource.com/python-exercises/tkinter/index-basic.php)
  - [geeksforgeeks](https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/)
  - [เกมฝึกเขียนโค้ดภาษาไพธอน](https://py.checkio.org/)

- &nbsp; Intermediate &nbsp;Level &nbsp;( เป็นโจทย์ที่ทำให้เราได้ฝึกเอาพื้นฐานมาประยุกต์ใช้สร้าง Product จริงๆ ) &nbsp;:&nbsp;
  - [practicepython](https://www.practicepython.org/)&nbsp;:&nbsp; โจทย์ส่วนมากเป็นเกม เช่น tic tac toe มีอธิบายโค้ด เหมาะใช้ฝึกอ่านทำความเข้าใจวิธีเขียนโค้ดของคนอื่น เพื่อมาประยุกต์ใช้ 
  - [hackerrank](https://www.hackerrank.com/domains/python?filters%5Bstatus%5D%5B%5D=unsolved&filters%5Bdifficulty%5D%5B%5D=medium) &nbsp;:&nbsp; เลือกระดับได้ คล้ายๆ leetcode เหมาะใช้ฝึก interview coding เตรียมตัวก่อนไปสัมภาษณ์งาน 
  - [edabit](https://edabit.com/challenge/rZToTkR5eB9Zn4zLh) &nbsp;:&nbsp; เลือกระดับได้ คล้ายๆ leetcode เหมาะใช้ฝึก interview coding เตรียมตัวก่อนไปสัมภาษณ์งาน

- &nbsp; Advanced &nbsp;Level &nbsp;( เป็นการทำ Project อาจจะ opensource ) &nbsp;:&nbsp;
  - [jetbrains](https://www.jetbrains.com/pages/academy/learn-python/?source=google&medium=cpc&campaign=13433376885&term=python%20practice&content=594036037356&gad=1&gclid=Cj0KCQjwuNemBhCBARIsADp74QRhGMr3OUYpRmbDaBxkOCLyd2tuNu0d9UJzk88bVbDyUxbtsf8dUiUaAh3AEALw_wcB) &nbsp;:&nbsp; พาทำโปรเจคน่าสนใจ เช่น Password Hacker (Python) แต่ไม่ฟรี
