# RPI-to-Printer

- Download Ubuntu MATE (version 16.04.2) เพื่อติดตั้งไว้บน raspberry pi 3
https://ubuntu-mate.org/download/

- update ไฟล์บน pi โดยพิมพ์คำสั่งดังนี้
    > $ sudo apt-get update   [ ถ้า update ไม่สำเร็จหรือเกิด Error ให้ใช้คำสั่ง  ($ sudo apt-get update --fix-missing) ]

- ติดตั้ง library barcode ให้กับ pi 3 โดยพิมพ์คำสั่งดังนี้
    > $ pip3 install python-barcode

- ติดตั้ง library docx ให้กับ pi 3 โดยพิมพ์คำสั่งดังนี้
    > $ sudo pip3 install --pre python-docx

- ติดตั้ง โปรแกรม CUPS โดยพิมพ์คำสั่งดังนี้
    > $ sudo apt-get install cups

- ตามที่โปรแกรมกำหนดมาให้ User group ที่สามารถเข้าถึงโปรแกรม CUPS คือ lpadmin แต่ในระบบปฏิบัติการ Ubuntu ที่ติดตั้งบน Raspberry Pi มีชื่อยูสเซอร์คือ
(ตามที่ตั้งไว้ตอน บูทเครื่อง คือ .. "srichand1") เพื่อให้ยูสเซอร์ srichand1 มีสิทธิการใช้โปรแกรม โดยพิมพ์คำสั่งดังนี้
    > $ sudo usermod -a -G lpadmin srichand1

- แก้ไขคอนฟิกเกอเรชั่นไฟล์ cupsd.conf โดยพิมพ์คำสั่งดังนี้ และจะปรากฏดังรูปข้างล่างนี้ 
    > $ sudo nano /etc/cups/cupsd.conf

![](http://fa.lnwfile.com/_/fa/_raw/x0/xx/99.png)

    //.. ค้นหาและลบบรรทัด Listen localhost:631 แล้วพิมพ์ Port 631 (8) เข้าไปแทนที่
    
    //.. เพิ่มบรรทัด Allow from 192.168.1.* เข้าไปในไฟล์ตรงจุดที่ (9), (10) และ (11) ดังรูปข้างบนนี้ แล้วบันทึก(Save)การเปลี่ยนแปลง 
    โดยให้กดปุ่ม Ctrl+O เมื่อปรากฏชื่อไฟล์ กดปุ่ม Enter แล้วกดปุ่ม Ctrl+X 

- รีรันโปรแกรม CUPS ใหม่ โดยป้อนคำสั่ด้านล่าง แล้วกดปุ่ม Enter หรือจะบูทเครื่องใหม่ก็ได้ โดยป้อนคำสั่ง sudo reboot แล้วกดปุ่ม Enter
    > $ sudo /etc/init.d/cups restart
    หรือ
    > $ sudo reboot
    
- บนเครื่องที่ติดตั้งระบบปฏิบัติการ เรียกโปรแกรมบราวเซอร์ แล้วป้อน IP Address ของ Raspberry Pi และ Port ของเครื่องพิมพ์ CUPS ในตัวอย่างนี้คือ http://192.168.1.4:631






