#นายณัชพล กิตคราม รหัสนักศึกษา 6410742156

# คำอธิบาย
# โปรแกรมคำนวณอุณหภูมิระหว่าง Celsius และ Fahrenheit เมื่อเข้าโปรแกรมโปรแกรมจะเช็คหาไฟล์ชื่อhistory ถ้าไม่มีโปรแกรมจะสร้างให้เพื่อเก็บประวัติการคำนวณ
# หน้าหลักของโปรแกรมจะให้ผู้ใช้กรอกอุณหภูมิ หลังจากกรอกเสร็จกดปุ่มคำนวณโปรแกรมก็จะแปลงค่าให้หน่วยตรงข้าม แล้วแสดงผลในช่องผลคำนวณ
# โปรแกรมมีการเก็บประวัติการคำนวณไว้ และสามารถกดปุ่มดูประวัติสีเทาเพื่อดูประวัติได้ การเก็บประวัติเป็นการเก็บลงไฟล์ ประวัติจึงไม่หายแม้ปิดโปรแกรม
# ในหน้าประวัติจะสามารถกดปุ่มเพื่อล้างประวัติได้ และกดปุ่มออกจากโปรแกรมสีแดงเพื่อปิดหน้าประวัติ
# ในหน้าหลักถ้าต้องการปิดโปรแกรมจะมีปุ่มปิดโปรแกรมสีแดง ให้กดเพื่อปิดโปรแกรม จะมีกล่องข้อความยืนยันการปิดโปรแกรม หากต้องการปิดโปรแกรม กด"yes" ถ้าต้องการให้ทำงานต่อ กด"no"
# Features:  -แปลงค่าอุณหภูมิCelsius และ Fahrenheit  -ดูประวัติการคำนวณ  -เก็บข้อมูลประวัติในไฟล์ history.txt -ปุ่มปิดโปรแกรม

from tkinter import *
import tkinter
import tkinter.messagebox

#สร้างTkinter หน้าหลัก
root = Tk()
root.title("โปรแกรมคำนวณระหว่าง Celsius และ Fahrenheit")

#การใส่ icon
# img = PhotoImage(file='logotemp.png')
# root.iconphoto(False,img)

root.geometry("500x370+400+100")
root.configure(bg="#fff")
root.resizable(False,False)

statushis = 0
#-------------------------------------------------------------------------------

#function checkfile ถ้าเครื่องuser 1ยังไม่มีไฟล์historeyจะทำการสร้างใหม่
def checkfile():
    try:
        #หาไฟล์
        fr = open("History.txt","r",encoding="utf-8")
        fr.read()
        fr.close()
    except FileNotFoundError:
        #สร้างfile
        fw = open("History.txt","w",encoding="utf-8")
        fw.close()
checkfile()
#-------------------------------------------------------------------------------

#หน้าจอที่2 หน้าแสดงประวัติ
def openWinHis():
    global winhis
    global showhis
    global statushis
    
    winhis = Tk()
    winhis.title("โปรแกรมคำนวณระหว่าง Celsius และ Fahrenheit")
    winhis.geometry("400x400+950+100")
    winhis.configure(bg="#fff")
    winhis.resizable(False,False)

    statushis = 1

    #สร้างframe ในหน้าที่2
    frame = Frame(winhis,width=380,height=370,bg='white')
    frame.place(x=10,y=15)
        
    #Label ประวัติ ตรงหัว
    heading = Label(frame,text='ประวัติ',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',18,'bold'))
    heading.place(x=140,y=5)

    #function ให้อ่านไฟล์history แล้วโชว์ประวัติ
    def showhis():
        global labelHis
        fr = open("History.txt","r",encoding="utf-8")
        labelHis = Label(winhis,text=fr.read(),fg='black',bg='white',font=('Microsoft Yahei UI Light',11),pady=5,justify=LEFT).place(y=50,x=15)
        #run function showhis
    showhis()

    #function exit program ใช้ปิดโปรแกรม
    def exitProgram2():
        global statushis
        statushis = 0
        #หน้านี้ไม่ต้องถามuser ว่าจะปิดไหม เพราะเป็นหน้าเสริม
        winhis.destroy()

    #function Clear History กดเคลียร์ข้อมูลให้history
    def clearHis():
        fw = open("History.txt","w",encoding="utf-8")
        fw.close()
        frame = Frame(winhis,width=400,height=253,bg='white')
        frame.place(x=5,y=50)

    Button(frame,width=15,pady=7,text='ล้างประวัติ',bg='#C0C0C0',fg='black',border=0,cursor='hand2',font=('Microsoft Yahei UI Light',9),command=clearHis).place(x=265,y=290)
    Button(frame,width=15,pady=7,text='ออกจากโปรแกรม',bg='red',fg='white',border=0,cursor='hand2',font=('Microsoft Yahei UI Light',9),command=exitProgram2).place(x=265,y=330)

    #run mainloop winhis
    winhis.mainloop()
#-------------------------------------------------------------------------------

#สร้างframe พื้นที่การทำงาน
frame = Frame(root,width=480,height=350,bg='white')
frame.place(x=10,y=10)

#label แสดงโปรแกรมแปลงค่าอุณภูมิ บนหัวโปรแกรม
heading = Label(frame,text='โปรแกรมแปลงค่าอุณหภูมิ',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=65,y=5)
#-------------------------------------------------------------------------------

#บรรทัดรับค่าอุณหภูมิ
#function เวลาคลิกช่องกรอกแล้วตัวอักษรในช่องหายไปให้พร้อมกรอก ใช้ .delete เพื่อล้างค่า
def on_enter(e):
    user.delete(0,END)

# เมื่อuser ยังไม่กรอก ค่ายังว่าง เมื่อกดที่อื่นคำว่ากรอกอุณหภูมิ(ex.36C or 245F) ก็จะกลับมา ใช้ .get รับค่ามาเช็ค ถ้ายังไม่ได้ใส่อะไร ให้แสดงคำที่เซ็ตไว้เหมือนเดิม
def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0,'กรอกอุณหภูมิ(ex:36C or 245F)')

#set ค่าตัวแปรtemp ให้เป็น stringVar
temp = StringVar()

#แสดงคำว่ากรอกอุณภูมิด้วยlabel ขนาดฟอนต์13
label1 = Label(frame,text='กรอกอุณหภูมิ  :',fg='black',bg='white',font=('Microsoft Yahei UI Light',13),padx=5)
label1.place(x=10,y=80)

#ช่องรับinput จาก user ตั้งให้ตัวอักษรอยู่ตรงกลาง และไม่มีกรอบ
user = Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',12),justify='center',textvariable=temp)
user.place(x=130,y=80)

#set ค่าในช่องที่userกรอก เพื่อยกตัวอย่าง ด้วย.insert
user.insert(0,'กรอกอุณหภูมิ(ex:36C or 245F)')

#เรียกfunction เมื่อกดแล้วจะล้างตัวหนังสือให้พร้อมป้อน ด้วย.bind
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

#สร้างเส้นข้างล่างของentry ด้วยFrame
Frame(frame,width=325,height=2,bg='black').place(x=130,y=107)
#-------------------------------------------------------------------------------

#บรรทัดแสดงผลลัพธ์
#แสดงคำว่าผลการคำนวณด้วยlabel ขนาดฟอนต์13
label2 = Label(frame,text='ผลการคำนวณ :',fg='black',bg='white',font=('Microsoft Yahei UI Light',13),padx=5)
label2.place(x=10,y=125)

#สร้างช่องแสดงผลลัพธ์
display = Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',12),justify='center')
display.place(x=130,y=125)

#สร้างเส้นข้างล่างของentry ด้วยFrame
Frame(frame,width=325,height=2,bg='black').place(x=130,y=150)
#-------------------------------------------------------------------------------

#function calculate ฟังก์ชั่นสั่งคำนวณ
def calculate():
    #นำค่าที่รับมาเก็บเข้าตัวแปรด้วย.get และหน่วยเก็บเข้าunit ค่าอุณหภูมิเก็บเข้าdegree โดยการระบุindex
    input_Temp =  temp.get()
    degree = float(input_Temp[:-1]) #เลขอุณหภูมิ
    unit = input_Temp[-1].upper() #หน่วย

    #ถ้าuser ส่งCelsius มา
    if unit == "C":
        #แปลงเป็นF
        #เริ่มด้วยเซตค่าในช่องว่างให้เป็นว่าง เผื่อuser กรอกอะไรเข้าไป หรือหากuser คำนวณค่าใหม่ แล้วเก็บผลการคำนวณเข้าresult แล้วinsert ในช่องdisplay
        display.delete(0,END)
        rehis = float(degree*(9/5)+32)
        result = "{:.2f}".format(rehis)
        redis = float(result),"F(ฟาเรนไฮน์)"
        display.insert(0,redis)
        #วนลูปเพื่อเอาหน่วย
        for i in redis:
            global re
            re = i
        #ตั้งค่าตัวแปรเก็บผลลัพธ์และเก็บส่วนที่จะเก็บลงไฟล์history แล้วก็เปิดไฟล์มา เพื่อบันทึกข้อมูล แล้วก็ปิดไฟล์ทุกครั้ง
        his_1 = str(degree)+" " +"C(เซลเซียส)"+" = "+str(result)+str(i)
        fw = open("History.txt","a",encoding="utf-8")
        fw.writelines(str(his_1)+"\n")
        fw.close()
        if statushis == 1:
            showhis()
        else:
            pass
    
    #ถ้าuser ส่งFahrenheit มา
    elif unit == "F":
        #แปลงเป็นC
        #เริ่มด้วยเซตค่าในช่องว่างให้เป็นว่าง เผื่อuser กรอกอะไรเข้าไป หรือหากuser คำนวณค่าใหม่ แล้วเก็บผลการคำนวณเข้าresult เซ็ตค่าให้ผลลัพธ์ทศนิยมแค่2ตัว แล้วinsert ในช่องdisplay
        display.delete(0,END)
        rehis = float((degree-32)*(5/9))
        result = "{:.2f}".format(rehis)
        redis = float(result),"C(เซลเซียส)"
        display.insert(0,redis)
        #วนลูปเพื่อเอาหน่วย
        for i in redis:
            re = i
        #ตั้งค่าตัวแปรเก็บผลลัพธ์และเก็บส่วนที่จะเก็บลงไฟล์history แล้วก็เปิดไฟล์มา เพื่อบันทึกข้อมูล แล้วก็ปิดไฟล์ทุกครั้ง
        his_1 = str(degree)+" " +"F(ฟาเรนไฮน์)"+" = "+str(result)+str(i)
        fw = open("History.txt","a",encoding="utf-8")
        fw.writelines(str(his_1)+"\n")
        fw.close()
        if statushis == 1:
            showhis()
        else:
            pass
    #หากไม่ตรงเงื่อนไข ก็แจ้งuserว่ากรอกข้อมูลผิด

    else:
        display.delete(0,END)
        display.insert(0,"ข้อมูลไม่ถูกต้องกรุณากรอกอีกรอบ")
#-------------------------------------------------------------------------------

#function ปิดโปรแกรม ใช้destroy เช็คว่าหน้าhistoryได้เปิดไหม ถ้าเปิดเวลากดปิดก็ให้ปิดทั้ง2หน้า
def exitProgram():
    if statushis == 1:
        #ถามผู้ใช้ว่าต้องการปิดไหม ด้วยการใช้messagebox askquestion แล้วเก็บเข้าตัวแปร แล้วใช้if เช็ค
        confirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการปิดโปรแกรมหรือไม่ ?")
        if confirm == "yes":
            root.destroy()
            winhis.destroy()

    else:
        #ถามผู้ใช้ว่าต้องการปิดไหม ด้วยการใช้messagebox askquestion แล้วเก็บเข้าตัวแปร แล้วใช้if เช็ค
        confirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการปิดโปรแกรมหรือไม่ ?")
        if confirm == "yes":
            root.destroy()
#-------------------------------------------------------------------------------

#ปุ่มหน้าแรก คำนวณ ดูประวัติ และออกจากโปรแกรม
Button(frame,width=32,pady=7,text='คำนวณ',bg='#57a1f8',fg='white',border=0,cursor='hand2',font=('Microsoft Yahei UI Light',11),command=calculate).place(x=93,y=180)
Button(frame,width=32,pady=7,text='ดูประวัติ',bg='#C0C0C0',fg='black',border=0,cursor='hand2',font=('Microsoft Yahei UI Light',11),command=openWinHis).place(x=93,y=230)
Button(frame,width=32,pady=7,text='ออกจากโปรแกรม',bg='red',fg='white',border=0,cursor='hand2',font=('Microsoft Yahei UI Light',11),command=exitProgram).place(x=93,y=280)
#-------------------------------------------------------------------------------

#run mainloop mainpage
root.mainloop()