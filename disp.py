from bottle import route, run, template, request, debug, install
import bottle
import bottle.ext.sqlite
from bottle_sqlite import SQLitePlugin
import bottle
from bottle.ext import sqlite

app = bottle.Bottle()
plugin = SQLitePlugin(dbfile='cwags (11).sqlite')
bottle.install(plugin)

print app 
#HOST = '192.168.47.101'

test_list = [
    {
    'protocol': 'proto1',
    'service':'s1',
    'plugin': 'plug1',
    'value':1
     },
    {
    'protocol': 'proto2',
    'service':'s2',
    'plugin': 'plug2',
    'value':2
     },
    {
    'protocol': 'proto3',
    'service':'s3',
    'plugin': 'plug3',
    'value':3
     },
]

number_of_test_cases = len(test_list)

@route('/page1')
def serve_homepage():
    return template('disp_table',rows = test_list, cases = number_of_test_cases)

@route('/new/<dumbvalue:int>', method='GET')
def add_new_get(db, dumbvalue):
    return template('add_case_post', rows = db.execute("select * from table2;").fetchall())

@route('/new/<dumbvalue:int>', method='POST')
def add_new_post(db, dumbvalue):
    names = []
    keys = {}
    rows = db.execute("select * from table2;").fetchall()
    for r in rows[0]:
            row
    print names
    p = request.forms.get('protocol')
    for name in names:
        keys[name] = request.forms.get(name)
    query = "update table2 (dog, round, result) values (?,?,?)"
    print keys
    #row = db.executemany(query, keys)
    print 'p=',p
    row= db.execute("select * from table2;").fetchall()
    if row:
        return template('add_case_post', rows = row) 



@route('/scoreevent/<id:int>', method='GET')
def add_new_get(db, id):
    return template('add_case_post', rows = db.execute("select run.id as id, run.dog as dog, run.round as round, run.result as result, dog.name as dogname, round.level as level, round.judge as judge from run, dog, round where round.id = run.round and dog.id = run.dog and run.round > :id-5 and run.round < :id order by run.round;", {"id":id}), action = id)

@route('/scoreevent/<id:int>', method='POST')
def add_new_post(db, id):
    p = request.forms.get('protocol')
    keys = request.forms.keys()
    print keys
    query = "update run set result = ? where dog = ? and round = ?"
    for key in keys:
        value = key.split(".")
        value.insert(0, request.forms.get(key))
        print value
        if len(value)<3:
           continue
        submit = db.execute(query, value)
    #row = db.executemany(query, keys)
    print 'p=',p
    rows= db.execute("select run.id as id, run.dog as dog, run.round as round, run.result as result, dog.name as dogname, round.level as level, round.judge as judge from run, dog, round where round.id = run.round and dog.id = run.dog and run.round > :id-5 and run.round < :id order by run.round;", {"id":id})
    if rows:
        return template('add_case_post', rows = rows, action = id) 


debug(True)
run(reloader=True)

#run(host=HOST, port=8080, debug=True)