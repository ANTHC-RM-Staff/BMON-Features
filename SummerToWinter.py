import sqlite3  
import settings

conn = sqlite3.connect(settings.BMON_SQLITE_PATH)  
  
cursor = conn.cursor()  
  
cursor.execute('UPDATE bmsapp_building SET [current_mode_id] = 1')  
  
print(f"Updated {cursor.rowcount} rows")  
  
conn.commit()  
conn.close
