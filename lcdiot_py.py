import requests as rp
import xlrd as x
wb=x.open_workbook('lcdiot.xlsx')
sh=wb.sheet_by_index(0)
URL='http://indianiotcloud.com/update1.php?id=NQUEES7HH78J9XVFDN29&field1=0&field2=0&field3=0&field4=0'
link='http://indianiotcloud.com/update1.php?id=NQUEES7HH78J9XVFDN29'
i=0
while(1):
    f1=sh.cell_value(i,0)
    f2=sh.cell_value(i+1,0)
    f3=sh.cell_value(i+2,0)
    f4=sh.cell_value(i+3,0)
    ln=link+'&field1='+str(f1)+'&field2='+str(f2)+'&field3='+str(f3)+'&field4='+str(f4)
    rp.put(ln)
    i=i+4
    time.sleep(5)
    
    
