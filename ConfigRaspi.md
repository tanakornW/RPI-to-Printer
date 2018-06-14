# RPI-Config

- Download Ubuntu MATE (version 16.04.2) เพื่อติดตั้งไว้บน raspberry pi 3
https://ubuntu-mate.org/download/

- update ไฟล์บน pi โดยพิมพ์คำสั่งดังนี้
    `$ sudo apt-get update`   [ ถ้า update ไม่สำเร็จหรือเกิด Error ให้ใช้คำสั่ง  (`$ sudo apt-get update --fix-missing`) ]

- ติดตั้ง library barcode ให้กับ pi 3 โดยพิมพ์คำสั่งดังนี้
    `$ pip3 install python-barcode`

- ติดตั้ง library docx ให้กับ pi 3 โดยพิมพ์คำสั่งดังนี้
    `$ sudo pip3 install --pre python-docx`

- ติดตั้ง โปรแกรม CUPS โดยพิมพ์คำสั่งดังนี้
    `$ sudo apt-get install cups`
    
- และติดตั้ง driver ที่โปรแกรม CUPS ต้องการดังนี้
    
    `$ sudo apt-get install autoconf` 
    
    `$ sudo apt-get install automake`
    
    `$ sudo apt-get install gcc`
    
    `$ sudo apt-get install ghostscript`
    
    `$ sudo apt-get install glibc-devel`
    
    `$ sudo apt-get install netpbm`
    
    `$ sudo apt-get install netpbm-progs`
    
    `$ sudo apt-get install poppler-utils`

- ตามที่โปรแกรมกำหนดมาให้ User group ที่สามารถเข้าถึงโปรแกรม CUPS คือ lpadmin แต่ในระบบปฏิบัติการ Ubuntu ที่ติดตั้งบน Raspberry Pi มีชื่อยูสเซอร์คือ
(ตามที่ตั้งไว้ตอน บูทเครื่อง คือ .. "srichand1") เพื่อให้ยูสเซอร์ srichand1 มีสิทธิการใช้โปรแกรม โดยพิมพ์คำสั่งดังนี้
    `$ sudo usermod -a -G lpadmin srichand1`

- แก้ไขคอนฟิกเกอเรชั่นไฟล์ cupsd.conf โดยพิมพ์คำสั่งดังนี้ และจะปรากฏดังรูปข้างล่างนี้ 
    `$ sudo nano /etc/cups/cupsd.conf`

![](http://fa.lnwfile.com/_/fa/_raw/x0/xx/99.png)

    //.. ค้นหาและลบบรรทัด Listen localhost:631 แล้วพิมพ์ Port 631 (8) เข้าไปแทนที่
    
    //.. เพิ่มบรรทัด Allow from 192.168.1.* เข้าไปในไฟล์ตรงจุดที่ (9), (10) และ (11) ดังรูปข้างบนนี้ แล้วบันทึก(Save)การเปลี่ยนแปลง 
    โดยให้กดปุ่ม Ctrl+O เมื่อปรากฏชื่อไฟล์ กดปุ่ม Enter แล้วกดปุ่ม Ctrl+X 

- รีรันโปรแกรม CUPS ใหม่ โดยป้อนคำสั่ด้านล่าง แล้วกดปุ่ม Enter หรือจะบูทเครื่องใหม่ก็ได้ โดยป้อนคำสั่ง sudo reboot แล้วกดปุ่ม Enter
    `$ sudo /etc/init.d/cups restart`
    หรือ
    `$ sudo reboot`
    
- ให้ Download ไฟล์ cupsdriver-1.2.56.tgz
    `https://na7.salesforce.com/sfc/p/#00000000SK3U/a/A0000000HbxO/katIjx1MXpgfJXlRnfiDHMXoyM9FaIshofWuAfKK63w`
![](https://www.picz.in.th/images/2018/06/14/4gI31t.png)

- เมื่อได้ไฟล์มาแล้วให้ทำการ Extract ไฟล์ออกมา (`cd` ไปที่pathไฟล์นั้นอยู่ และตามด้วย `cd cupsdriver-1.2-56`) จากนั้นพิมพ์คำสั่ง `sudo ./build.sh`

- บนเครื่องที่ติดตั้งระบบปฏิบัติการ ให้เรียกโปรแกรมบราวเซอร์ แล้วป้อน IP Address ของ RaspberryPi และ Port ของเครื่องพิมพ์ CUPS ในตัวอย่างนี้คือ `http://192.168.1.4:631` จะแสดงดังรูป
![](https://www.picz.in.th/images/2018/06/14/4i4zXa.png)

- เปิดเครื่องพิมพ์ที่เสียบสาย USB เข้ากับ Raspberry Pi แล้วคลิกแถบคำสั่ง Administration (1) และเพิ่มเครื่องพิมพ์ ให้ติ๊กเครื่องหมายถูกบน Share printers connected to this system (2) แล้วคลิกปุ่ม Add Printer (3) จะปรากฏดังรูปข้างล่างนี้
![](https://www.picz.in.th/images/2018/06/14/4ifnbV.png)

- โปรแกรมเตือนว่าให้เข้าเข้าโหมด Admin รอสักครู่ หน้าเวบเพจจะเปลี่ยนไปยังหน้าล็อคอิน หากไม่เปลี่ยนคลิกลิงค์ (4) เพื่อไปยังหน้าล็อคอิน จะปรากฏดังรูปข้างล่างนี้
![](https://www.picz.in.th/images/2018/06/15/4itJyq.png)

- คลิกลิงค์ Advanced (5) และคลิ๊ก proceed to 192.168.1.4(unsafe) เพื่อไปยังหน้าล็อคอิน จะปรากฏดังรูปข้างล่างนี้
![](https://www.picz.in.th/images/2018/06/15/4itMUu.png)





![](https://www.picz.in.th/images/2018/06/14/4ifnbV.png)
![](https://www.picz.in.th/images/2018/06/14/4ifnbV.png)



