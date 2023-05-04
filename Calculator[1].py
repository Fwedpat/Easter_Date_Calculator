#!/usr/bin/python3
import cgi, math, cgitb
cgitb.enable()
form = cgi.FieldStorage()
Year = form.getvalue("theYear")
try:
    Year = int(Year)
    ExceptionYears = [1954, 1981, 2049, 2076]
    EasterDay = 0
    MonthChecker = 0
    DateOfEasterText = ""
    a = Year % 19
    b = Year % 4
    c = Year % 7
    d = (19 * a + 24) % 30
    e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7
    if Year in ExceptionYears:
        EasterDay = (22 + d + e) - 7
    else:
        EasterDay = 22 + d + e
    if EasterDay > 31:
        EasterDay = EasterDay - 31
        EasterString = str(EasterDay)
        if EasterDay > 9:
            EasterString = EasterString[1:]
        if EasterString == "1" and EasterDay != 11:
            DateOfEasterText = "April " + str(EasterDay) + '<sup>st</sup> ' + str(Year)
        elif EasterString == "2" and EasterDay != 12:
            DateOfEasterText = "April " + str(EasterDay) + '<sup>nd</sup> ' + str(Year)
        elif EasterString == "3" and EasterDay != 13:
            DateOfEasterText = "April " + str(EasterDay) + '<sup>rd</sup> ' + str(Year)
        else:
            DateOfEasterText = "April " + str(EasterDay) + '<sup>th</sup> ' + str(Year)
    else:
        MonthChecker = 1
        EasterString = str(EasterDay)
        if EasterDay > 9:
            EasterString = EasterString[1:]
        if EasterString == "1" and EasterDay != 11:
            DateOfEasterText = "March " + str(EasterDay) + '<sup>st</sup> ' + str(Year)
        elif EasterString == "2" and EasterDay != 12:
            DateOfEasterText = "March " + str(EasterDay) + '<sup>nd</sup> ' + str(Year)
        elif EasterString == "3" and EasterDay != 13:
            DateOfEasterText = "March " + str(EasterDay) + '<sup>rd</sup> ' + str(Year)
        else:
            DateOfEasterText = "March " + str(EasterDay) + '<sup>th</sup> ' + str(Year)
    DateOfEasterText = str(DateOfEasterText)
    DateOfEasterText = DateOfEasterText.strip("(")
    DateOfEasterText = DateOfEasterText.strip(")")
    DateOfEasterText = DateOfEasterText.replace(",", "")
    DateOfEasterText = DateOfEasterText.replace("'", "")

    Format = form.getvalue("Format")



    print('Content-Type: text/html; charset=utf-8')
    print('')
    print('<!DOCTYPE html>')
    print('<html>')
    print('<link rel="stylesheet" href="../stylesheet.css">')
    print('<head> <title> Pogchamp </title> </head>')
    print('<div>')
    print('<body>')
    if Format == "Written":
        print('The Date of Easter is {0}'.format(DateOfEasterText))
    elif Format == "Numeric":
        if MonthChecker == 1:
            print(str(EasterDay) + '/03/' + str(Year))
        else:
            print(str(EasterDay) + '/04/' + str(Year))
    elif Format == "Both":
        if MonthChecker == 1:
            print(str(EasterDay) + '/03/' + str(Year) + '<br>')
            print('The Date of Easter is {0}'.format(DateOfEasterText))        
        else:
            print(str(EasterDay) + '/04/' + str(Year) + '<br>') 
            print('The Date of Easter is {0}'.format(DateOfEasterText))
    print('</body>')
    print('</div>')
    print('</html>')

except:
    print('Content-Type: text/html; charset=utf-8')
    print('')
    print('<!DOCTYPE html>')
    print('<html>')
    print('<link rel="stylesheet" href="../stylesheet.css">')
    print('<head> <title> Pogchamp </title> </head>')
    print('<div>')
    print('<body>')
    print('You did not enter a Year, Please try again!')
    print('</body>')
    print('</div>')
    print('</html>')
