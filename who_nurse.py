from when_nurse import get_db_connection
import sys
import datetime

def who_is_available(date, time):
    connection = get_db_connection()
    if any(i in sys.argv[1] for i in "x"):
        date = date
    else:
        return("Please enter the date in the format yearxmonthxday")#has to be in 2021x04x01 to work
    with connection.cursor() as cursor:
        sql = "SELECT `nurses`.`LastName`FROM`nurse_schedule`,`nurses`WHERE`nurse_schedule`.`SlotDate`=%s AND `nurse_schedule`.`SlotStart`<=%s AND `nurse_schedule`.`SlotEnd`>= %s\
 AND `nurses`.`id`=`nurse_schedule`.`NurseID`"
        cursor.execute(sql, (date, time, time))
        available = cursor.fetchall()
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
        hour = ""
        listH = []
        for j in range(len(time)):
            if time[j] != ":":
                hour+=time[j]
            else:
                if len(hour) != 0:
                    listH.append(hour)
                hour=""
        listH.append(hour)
        start = datetime.time(9,0,0)
        end = datetime.time(17,0,0)
        if not (time_in_range(start,end,datetime.time(int(listH[0]), int(listH[1]), int(listH[2])))):
            return("Sorry, the clinic is only open from 9am-5pm Mon-Fri.")
        if len(available) == 0:
            return("No nurses are avaiable at that time")
        output = "Nurses available at that time:\n";
        for nurse in available:
            output+=("Nurse %s\n" % nurse["LastName"])
        return output
def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end
    
if __name__ == "__main__":
    date = sys.argv[1].replace("x", "-")
    print(who_is_available(date,sys.argv[2]))
