import sqlite3  
  
conn = sqlite3.connect('/PATH-TO-FILE/bmon.sqlite')  
  
cursor = conn.cursor()  
  
cursor.execute('UPDATE bmsapp_building SET [current_mode_id] = 1')  
  
print(f"Updated {cursor.rowcount} rows")  
  
conn.commit()  
conn.close
