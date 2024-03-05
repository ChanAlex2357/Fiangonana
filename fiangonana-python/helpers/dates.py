from datetime import datetime ,date
def  string_to_date(string):
    return datetime.strptime(string,'%Y-%m-%d').date()