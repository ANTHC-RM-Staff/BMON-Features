import sqlite3
import pandas as pd
import settings

df = pd.read_excel(settings.BUILDING_ALERT_IDS_PATH, sheet_name='AlertGroupAndBuildingIDs')

conn = sqlite3.connect(settings.BMON_SQLITE_PATH)
cursor = conn.cursor()

for index, row in df.iterrows():
   building_id = row['BMON Building ID']
   alert_group_id = row['AlertGroupID']
   cursor.execute("SELECT sensor_id FROM bmsapp_bldgtosensor WHERE building_id = ?", (building_id,))
   sensors = cursor.fetchall()
   for sensor in sensors:
      sensor_id = sensor[0]
      cursor.execute("SELECT bmsapp_alertcondition.rowid FROM bmsapp_alertcondition WHERE sensor_id = ?", (sensor_id,))
      alertconditions = cursor.fetchall()
      if alertconditions:
        for alertcondition in alertconditions:
            alertcondition_id = alertcondition[0]
            cursor.execute("INSERT OR IGNORE INTO bmsapp_alertcondition_recipient_groups (alertcondition_id, alertrecipientgroup_id) Values (?,?)",(alertcondition_id,alert_group_id))
            cursor.execute("SELECT sensor_id FROM bmsapp_alertcondition WHERE rowid = ?", (alertcondition_id,))
            print(cursor.fetchall())

conn.commit()
conn.close()


