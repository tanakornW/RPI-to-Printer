# RPI-to-Printer หมายเหตุ python code ชุดนี้ เขียนบน windows os บางฟังก์ชัน หรือบาง โมดูล อาจทำงานไม่ได้บน linux และ ubuntu

  funtion barcode (ใช้สำหรับ สร้าง barcode จากข้อมูล text สามารถ เลือกชนิดของ barcode ได้)
``` python
import barcode
from barcode.writer import ImageWriter
ean = barcode.get('code128', '1234567tanakotnjhy', writer=ImageWriter())
filename = ean.save('testbarcode')
print (ean)
```
ใน funtion จะบันทึก barcode ที่สร้างได้เป็น รูปภาพ นามสกุล .PNG

  funtion docx (ใช้สำหรับ สร้างไฟล์ docx เพื่อรอพิมพ์ )
``` python
from docx import Document
from docx.shared import Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

document = Document()
a="ธนากร วังทอง 12345"

#changing the page margins
sections = document.sections
for section in sections:
    section.page_height = Cm(5)
    section.page_width = Cm(10)
    section.top_margin = Cm(0)
    section.bottom_margin = Cm(0)
    section.left_margin = Cm(0.5)
    section.right_margin = Cm(0.5)


document.add_heading(a,0)
p = document.add_paragraph()
r = p.add_run()
r.add_text(loaded_r['title'])
my_image = document.add_picture('testbarcode.png',height=Cm(1.3)) 
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
document.save('demo.docx')
```

funtion Print (ใช้สั่งพิมพ์เอกสาร)
``` python
import os
os.startfile("demo.docx", "print")
```
