import pymysql.cursors
import sys
import datetime
# Connect to the database
def get_db_connection():
    return  pymysql.connect(host='52.70.223.35',
                             user='clinicuser',
                             password='sparky',
                             database='ClinicDB',
                             cursorclass=pymysql.cursors.DictCursor)
def when_nurse_available(last_name, date):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `nurses` WHERE `LastName` = %s"
        cursor.execute(sql, (last_name))
        nurse_id = cursor.fetchone()
        last_name = nurse_id["LastName"]
        listD = []
        word = ""
        for i in range(len(date)):
            if date[i] != "-":
                word+=date[i]
            else:
                if len(word) != 0:
                    listD.append(word)
                word = ""
        listD.append(word)
        datetime.datetime.today()
        day = datetime.datetime(int(listD[0]), int(listD[1]), int(listD[2]))
        dotw = day.weekday()
       
        if dotw > 4:
            return("Sorry, the clinic is only open from 9am-5pm Mon-Fri.")
        try:
            nurse_id = nurse_id["id"]
        except TypeError:
            return("Sorry, but we don't have a Nurse %s in this office. Make sure to look up your nurse by last name!" % last_name)
    with connection.cursor() as cursor:
        sql = "SELECT  `SlotStart`, `SlotEnd` FROM `nurse_schedule` WHERE `NurseID`=%s AND `SlotDate`=%s"
        cursor.execute(sql, (nurse_id, date))
        time = cursor.fetchone()
    try:
        return("From %s To %s" % (time["SlotStart"], time["SlotEnd"]))
    except TypeError:
        return("Sorry, Nurse %s is not available on %s" % (last_name, date))
        
if __name__ == "__main__":
    print(when_nurse_available(sys.argv[1], sys.argv[2]))

