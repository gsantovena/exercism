from datetime import date, timedelta

def meetup_day(year, month, dow, pos):
    days = { 
        'Monday': 0, 
        'Tuesday': 1, 
        'Wednesday': 2, 
        'Thursday': 3, 
        'Friday': 4, 
        'Saturday': 5,
        'Sunday': 6, 
    }

    md = date(year, month, 1)
    dow_list = []

    while md.weekday() != days[dow]:
        md += timedelta(days=1)

    while md.month == month:
        dow_list.append(md)
        md += timedelta(days=7)

    if pos == 'teenth':
        if dow_list[1].day < 13:
            return dow_list[2]
        else:
            return dow_list[1]
    elif pos == 'last':
        return dow_list[-1]
    else:
        return dow_list[int(pos[0]) - 1]
    
if __name__ == '__main__':
    print meetup_day(2013, 5, 'Monday', 'teenth')
    print meetup_day(2013, 2, 'Saturday', 'teenth')
    print meetup_day(2013, 5, 'Tuesday', '1st')
    print meetup_day(2013, 4, 'Monday', '2nd')
    print meetup_day(2013, 9, 'Thursday', '3rd')
    print meetup_day(2013, 10, 'Thursday', 'last')

