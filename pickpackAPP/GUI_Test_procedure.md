# GUI_FORM
- หมายเหตุ 
  - GUI นี้เป็นเพียง GUI เปล่าๆไม่ได้มีโปรแกรมติดต่อ API และไม่ได้มี โปรแกรมส่วนสร้าง barcode 
  - GUI อาจจะล้นขอบหรือดูไม่สมบูรณ์ เนื่องจากตั้งไว้ให้เหมาะสมกับ จอภาพ ขนาด 3.5 นิ้ว 
  
- วิธีการทดสอบ GUI ของ Pickpack bot 
  1. ติดตั้งระบบปฏิบัติการตามขั้นตอนใน ConfigRaspi.md 
  2. copy โฟลเดอร์ GUI_APP จาก https://github.com/tanakornW/RPI-to-Printer/tree/master/pickpackAPP 
    ไปไว้ที่หน้าจอของ raspberry pi 
  3. เข้าไปใน โฟลเดอร์ GUI_APP จากนั้นคลิกขวาที่ app_ppb.py แล้ว open with IDLE 3
  4. กด RUN แล้ว Run Module หรือ กด F5
  5. การใช้งานโปรแกรม
    - หน้า Work space ระบบจะบอกว่าผู้ใช้ไม่ได้เลือกช่องทางการรับข้อมูล 
    
        ![image](https://github.com/tanakornW/imagePPB/blob/master/image%20ppb/001.PNG)
        
    - เมื่อเข้ามาผู้ใช้จะต้องเลือก option menu เพื่อให้ระบบทำงานตามที่ผู้ใช้ต้องการ
    
        ![image](https://github.com/tanakornW/imagePPB/blob/master/image%20ppb/002.PNG)
        
    - เมื่อเลือกแล้ว ระบบจะแสดงหน้าต่าง เพื่อยืนยันการเลือก  ถ้าหากเลือก OK สถานะ การทำงานจะบอกว่า You are typing information from ........
    
        ![image](https://github.com/tanakornW/imagePPB/blob/master/image%20ppb/003.PNG) 
        ![image](https://github.com/tanakornW/imagePPB/blob/master/image%20ppb/004.PNG)
             
    - ถ้าหากเลือก Cancel สถานะ การทำงานจะบอกว่า Stop working
    
        ![image](https://github.com/tanakornW/imagePPB/blob/master/image%20ppb/005.PNG) 
        ![image](https://github.com/tanakornW/imagePPB/blob/master/image%20ppb/006.PNG)
        
    - หน้า Setting API เมื่อเข้ามาระบบจะแสดง URL ล่าสุดของแต่ละช่องทาง ผู้ใช้สามารถแก้ใขได้ จากนั้นกด SAVE
    
        ![image](https://github.com/tanakornW/imagePPB/blob/master/image%20ppb/007.PNG)
        
    - เมื่อกด SAVE ระบบจะแสดงหน้าต่างเพื่อยืนยันการตั้งค่า ถ้ากด OK จะแสดง สถานะว่า  Saved
    
        ![image](https://github.com/tanakornW/imagePPB/blob/master/image%20ppb/008.PNG)
        ![image](https://github.com/tanakornW/imagePPB/blob/master/image%20ppb/009.PNG)
        
    - เมื่อกด SAVE ระบบจะแสดงหน้าต่างเพื่อยืนยันการตั้งค่า ถ้ากด Cancel ระบบจะนำ URL ที่บันทึกล่าสุดมาแสดง
    
        ![image](https://github.com/tanakornW/imagePPB/blob/master/image%20ppb/010.PNG)
        ![image](https://github.com/tanakornW/imagePPB/blob/master/image%20ppb/011.PNG)
        
    - ปุ่มกด Reset Defult คือการกดเพื่อล้าง URL ที่กรอกเข้าไปใหม่แล้วแสดง URL ที่บันทึกล่าสุด
