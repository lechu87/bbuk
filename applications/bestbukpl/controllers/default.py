# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import subprocess
import re
from collections import defaultdict
from collections import OrderedDict

def hello():
    #rows=s.select()
    #rows=s.select()
    check_id=request.vars.c_id
    #x=subprocess.call(['python3', '/home/lesinle/odds/read_coupon_fortuna_wo_sql.py',check_id])
    x=subprocess.check_output(['python3','/home/lesinle/odds/read_coupon_fortuna_wo_sql.py',check_id])
    y1=re.sub('\[','',x)
    y2=re.sub(']','',y1)
    y=y2.split("'")
    #print (y
    #y = [x for x in y if x != ['[',']']]
    #y.remove('[')
    new_list=[]
    for el in y:
        if el not in [",","[","']","['","]","[","],","],[","], ["," ","\n",", ","'",",\n",""]:
            new_list.append(el)
    home2=[]
    home_list=[]
    away_list=[]
    typ_list=[]
    typ_name_list=[]
    for i in range(0,len(new_list)-1,4):
        home_list.append(new_list[i])
        away_list.append(new_list[i+1])
        typ_list.append(new_list[i+2])
        typ_name_list.append(new_list[i+3])
    wynik=defaultdict(str)
    for i in range(0,len(home_list)):
        for bookie in bookies:
            if bookie not in wynik.keys():
                wynik[bookie]=[]
        #wynik[bookie].append(db((db[bookie].home=='Leicester') & (db[bookie].away=='Watford')).select())
            wynik[bookie].append(db1((db1[bookie].home==home_list[i]) & (db1[bookie].away==away_list[i])).select())
    for i in range(0,len(home_list)):
        for bookie in bookies:
            if len(wynik[bookie][i])==0:
                wynik[bookie][i]=db1((db1[bookie].home=='Test') & (db1[bookie].away=='Test')).select()
            #wynik2=db((db.bookie.home=='Leicester') & (db.bookie.away=='Watford')).select()
            #wynik=[wynik1,wynik2]
        #else
        #    wynik = wynik&
#    wynik_temp=db(((db.db_sts.home=='Leicester') & (db.db_sts.away=='Watford')) | ((db.db_fortuna.home=='Leicester') & (db.db_fortuna.away=='Watford'))).select()
    #q = (home=='Leicester' & away=='Watford')
    #s=db(q)
    #for i in range(0,len(home_list)):
    #    rows=db((home==home_list[i]) & (away==away_list[i])).select()
        #cos=typ_list[1]    #rows = db((home=='Leicester') & (away=='Watford')).select()
    #for bookie in bookies:
    #    if len(wynik[bookie])==0:
    #        wynik[bookie].append(db((db[bookie].home=='Test') & (db[bookie].away=='Test')).select())
    full_kurs= defaultdict(lambda:1)
    for i in range(0,len(home_list)):
        for bookie in bookies:
            if bookie not in full_kurs.keys():
                full_kurs[bookie]=1
            try:
                full_kurs[bookie]=full_kurs[bookie]*float(wynik[bookie][i][0][typ_list[i]])
            except:
                full_kurs[bookie]=full_kurs[bookie]*1

    #select distinct db_sts.home, db_sts.away, db_sts.data, db_sts.game_1 as sts_1, db_fortuna.game_1 as fortuna_1 from db_sts JOIN db_fortuna on (db_sts.home=db_fortuna.home and db_sts.away=db_fortuna.away)
#where db_sts.home like 'Leicester' and db_sts.away like 'Watford'
#http://web2py.com/books/default/chapter/42/06/warstwa-abstracji-bazy-danych
    return locals()



def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    #form=SQLFORM.factory(Field('Kupon')).process()
    #return dict(message=T('Welcome to web2py!'))
    return locals()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def get_value(x):
    if x not in None:
        return float(x)
def bets_list():
    bets={'mecz':{'name':['game_1','game_0','game_2','game_10','game_02','game_12'],'show':['1','X','2','1X','X2','12']},
          'liczba goli':{'name':['o_25','u_25','o_15','u_15','o_35','u_35','o_45','u_45'],'show':['pow. 2.5','pon. 2.5','pow. 1.5','pon. 1.5','pow. 3.5','pon. 3.5','pow. 4.5','pon. 4.5']},
         'half/end':{'name':['ht_ft_11','ht_ft_1x','ht_ft_2x','ht_ft_21','ht_ft_22','ht_ft_x1','ht_ft_x2','ht_ft_12','ht_ft_xx'],'show':['1/1','1/x','2/x','2/1','2/2','x/1','x/2','1/2','x/x']},
         'dnb':{'name':['dnb_1','dnb_2'],'show':['Remis nie ma zakładu 1','Remis nie ma zakładu - 2']},
         'btts':{'name':['btts_yes','btts_no'],'show':['Obie drużyny strzelą gola - TAK','Obie drużyny strzelą gola - NIE']},
         'btts/game':{'name':['btts_1','btts_2','btts_x','btts_no_1','btts_no_2','btts_no_x'],'show':['btts tak / 1','btts tak / 2 ','btts tak / X','btts nie / 1','btts nie / 2','btts nie / x']}}
    return bets

def bookie_list():
    bookies=['fortuna','sts','iforbet','lvbet','totolotek']
    return bookies


def kursy():
    league=request.vars.league
    if league is None:
        league='Ekstraklasa Polska'
    rows = db1((db1['db_bets'].League==league) & (db1['db_bets'].data>='2018-07-21')).select()
    bets=bets_list()
    bookies=bookie_list()
    return locals()

def mean(rows):
    bookies=bookie_list()
    bets=bets_list()
    for row in rows:
        row=1

def kursy_game():
    bets=bets_list()
    game_id=request.vars.game_id
    if game_id is None:
        game_id=429
    odd_type=request.vars.odd_type
    rows=db1((db1['db_bets'].id==game_id)).select()
    #bets=OrderedDict({'game':OrderedDict({'game_0':'0','game_1':'1','game_2':'2','game_10':'1x','game_02':'x2','game_12':'12'})})

    bookies=bookie_list()
    typ=request.vars.typ
    if typ is None:
        typ='mecz'
    return locals()

def data():
    if not session.m or len(session.m)==10: session.m=[]
    if request.vars.q: session.m.append(request.vars.q)
    session.m.sort()
    return session.m
