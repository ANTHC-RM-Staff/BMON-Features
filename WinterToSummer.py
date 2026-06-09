import sqlite3  
  
conn = sqlite3.connect('/PATH-TO-FILE/bmon.sqlite')  
  
cursor = conn.cursor()  

#Changed to SET [current_mode_id] = 2. 2 represents Summer
cursor.execute('UPDATE bmsapp_building SET [current_mode_id] = 2')  
  
print(f"Updated {cursor.rowcount} rows")  
  
conn.commit()  
conn.close
