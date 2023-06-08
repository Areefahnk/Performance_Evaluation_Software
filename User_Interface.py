import Main_App as mp
from Main_App.Performance_Evaluation_Pack import evaluation as e
from Main_App.Reports_Display import display_reports as d
from Main_App.Reports_Display import search_reports as s
from Main_App.Update_Report import update_name as u
import sqlite3

print("-------------------WELCOME TO THE GENZEON'S BOOTCAMP EVALUATION SOFTWARE--------------------")
while True:
    print("""1.Enter Report & Store
    2.See All stored Data
    3.Search for a report with G_id
    4.Update name wrongly entered using G_id
    5.Fetch Participants who are eligible for Certificate of Excellence 
    6.Exit""")
    print("Choose any option from above menu:")
    ch = int(input())
    if ch == 1:
        print(e.get_data())
    elif ch==2:
        print(d.display())
    elif ch==3:
        id=input("Enter the Report G_id to search:")
        res=s.search((id))
    elif ch==4:
        id=input("Enter the Report G_id to update:")
        new_name=input("Enter the new name:")
        print(u.update(id,new_name))
    elif ch==5:
        e.get_excellence_records()

    else:
        break