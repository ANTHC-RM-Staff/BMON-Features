import sqlite3  
import settings

conn = sqlite3.connect(settings.BMON_SQLITE_PATH)  
  
cursor = conn.cursor()  

#Changed to SET [current_mode_id] = 2. 2 represents Summer
cursor.execute('UPDATE bmsapp_building SET [current_mode_id] = 2')  
  
print(f"Updated {cursor.rowcount} rows")  
  
conn.commit()  
conn.close
