import sqlite3
import pandas as pd
import settings
from openpyxl import load_workbook

conn = sqlite3.connect(settings.BMON_SQLITE_PATH)
df = pd.read_sql_query("SELECT rowid, title FROM bmsapp_alertrecipientgroup ORDER BY title", conn)
conn.close()

with pd.ExcelWriter(settings.BUILDING_ALERT_IDS_PATH, engine='openpyxl', mode = 'a') as writer:
    df.to_excel(writer, sheet_name='AlertGroupIDs', index=False)

print("Export successful!")