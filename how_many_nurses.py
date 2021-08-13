from when_nurse import get_db_connection
import sys
import datetime
def how_many_available(date):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "SELECT `nurses`.`LastName`FROM`nurse_schedule`,`nurses`WHERE`nurse_schedule`.`SlotDate`=%s AND `nurses`.`id`=`nurse_schedule`.`NurseID`"
        cursor.execute(sql, (date))
        how_many = cursor.fetchall()
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
        if len(how_many) == 0:
            return("No nurses are available on that day")
        return("There are %s nurses available on that day" % len(how_many))

if __name__ == "__main__":
    print(how_many_available(sys.argv[1]))
