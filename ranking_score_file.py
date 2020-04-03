highest_score = 0 
scores = {}
result_f = open('./data/results.txt')
for line in result_f:
    (name,score) = line.split()
    scores[score] = name 
result_f.close()
# scores.sort(reverse=True)
#scores.sort()
#scores.reverse()
place = {
        '1':'first',
        '2':'second',
        '3':'third',
        '4':'fourth',
        '5':'fifth',
        '6':'sixth',
        '7':'seventh',
        '8':'eighth',
        '9':'nineth',
        '10':'tenth',
    }
for i,each_score in enumerate(sorted(scores.keys(),reverse=True)):
    print('Surfer ' + scores[each_score] + ' scored ' + each_score + ' is in ' + place[str(i+1)] + ' place .')



def find_details_file(id2find):
    surfers_f = open("./data/surfing_data.csv")
    for each_line in surfers_f:
        s = {}
        (s['id'],s['name'],s['country']\
        ,s['average'],s['board'],s['age']) = each_line.split(';')
        if id2find == int(s['id']):
            surfers_f.close()
            return(s)
    surfers_f.close()
    return ({})

lookup_id = int(input('Enter your id surfer (start with 101): '))
surfer = find_details_file(lookup_id)
if surfer:
    print("ID:          {}".format(surfer['id']))
    print("Name:        {}".format(surfer['name']))
    print("Country:     {}".format(surfer['country']))
    print("Average:     {}".format(surfer['average']))
    print("Board type:  {}".format(surfer['board']))
    print("Age:         {}".format(surfer['age']))

import sqlite3

def find_details_database(id2find):
    db = sqlite3.connect('./data/surfersDB.sdb')

    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("select * from surfers")
    rows = cursor.fetchall()
    for row in rows:
        if row['id'] == id2find:
            s = {}
            s['id'] = row['id']
            s['name'] = row['name']
            s['country'] = row['country']
            s['average'] = row['average']
            s['board'] = row['board']
            s['age'] = row['age']
            cursor.close()  
            return(s)
    cursor.close()
    return({})

lookup_id = int(input('Enter your id surfer (start with 101): '))
surfer = find_details_database(lookup_id)
if surfer:
    print("ID:          {}".format(surfer['id']))
    print("Name:        {}".format(surfer['name']))
    print("Country:     {}".format(surfer['country']))
    print("Average:     {}".format(surfer['average']))
    print("Board type:  {}".format(surfer['board']))
    print("Age:         {}".format(surfer['age']))
