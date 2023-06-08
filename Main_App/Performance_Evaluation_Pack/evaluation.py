import  sqlite3
conn  =  sqlite3.connect ('genzeon_bootcamp_database.db')

def calc_score(report):
    score=report.get("day_wise_score")+report.get("python_project_score")+report.get("aiml_project_score")+report.get("interact_score")
    print(score)
    return score

def calc_grade(report,score):
    if score>=80:
        report["grade"]='Excellent'
    elif score>=70:
        report["grade"]='Very Good'
    elif score>=60:
        report["grade"] = 'Good'
    else:
        report["grade"]='Average'

def get_excellence_certificate(report,grade):
    if grade == 'Excellent':
        report["qualify_for_Excellence_Certificate"]='Yes'
    else:
        report["qualify_for_Excellence_Certificate"] = 'No'

def get_excellence_records():
    records=conn.execute("select *from performance where qualify_for_Excellence_Certificate='Yes'")
    for i in records:
        print(i)


def get_data():
    report={}
    print("Welcome to the Student Performance Evaluation Software.")
    print("Enter the below registration details")
    g_id=input("Enter the GID:")
    name=input("Enter name of student:")
    mail_id=input("Enter the mail_id:")
    print("Enter the evaluation details:")
    day_wise_score=input("Enter the Day wise Colab files submissions (marks out of 20):")
    python_project_score=input("Enter Score for the Mini Project (marks out of 20):")
    AIML_project_score=input("Enter Score for the Major Project (marks out of 40):")
    interact_score=input("Enter Points for the participants Interactiveness (marks out of 20):")
    report["g_id"]=g_id
    report["name"] = name
    report["mail_id"] = mail_id
    report["day_wise_score"] = float(day_wise_score)
    report["python_project_score"] = float(python_project_score)
    report["aiml_project_score"] = float(AIML_project_score)
    report["interact_score"] = float(interact_score)
    print(report)
    report["overall_score"]=calc_score(report)
    calc_grade(report,report.get("overall_score"))
    get_excellence_certificate(report,report.get("grade"))

    conn.execute("""
    Insert into performance(g_id,name,mail_id,day_wise_score,python_project_score,aiml_project_score,interact_score,overall_score,grade,qualify_for_Excellence_Certificate)
    Values (?,?,?,?,?,?,?,?,?,?)
    """,(report.get("g_id"),report.get("name"),report.get("mail_id"),report.get("day_wise_score"),report.get("python_project_score"),report.get("aiml_project_score"),report.get("interact_score"),report.get("overall_score"),report.get("grade"),report.get("qualify_for_Excellence_Certificate")))
    conn.commit()
    print('Data entered successfully.')
    return report
