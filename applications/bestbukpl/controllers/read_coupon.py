# -*- coding: utf-8 -*-
# spróbój czegos takiego jak
#read_coupon_fortuna_wo_sql=local_import('read_coupon_fortuna_wo_sql_27')
#from read_coupon_fortuna_wo_sql local_import read_coupon
import subprocess
import re
from collections import defaultdict
def index(): return dict(message="hello from read_coupon.py")

def test():
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
    db = DAL('sqlite://db.sqlite')
    db_name=db._uri
    bookies=['db_fortuna','db_sts','db_iforbet','db_lvbet','db_totolotek']
    for bookie in bookies:
        db.define_table(bookie, Field('home'),Field('away'),Field('game_1'),Field('game_0'),Field('game_2'),Field('game_10'),Field('game_02'),Field('game_12'),Field('data'),Field('Sport'),Field('League'),Field('country'),Field('dnb_1'),Field('dnb_2'),Field('o_05'),Field('o_15'),Field('o_25'),Field('o_35'),Field('o_45'),Field('o_55'),Field('o_65'),Field('o_75'),Field('o_85'),Field('o_95'),Field('u_05'),Field('u_15'),Field('u_25'),Field('u_35'),Field('u_45'),Field('u_55'),Field('u_65'),Field('u_75'),Field('u_85'),Field('u_95'),Field('ht_ft_11'),Field('ht_ft_1x'),Field('ht_ft_x1'),Field('ht_ft_22'),Field('ht_ft_x2'),Field('ht_ft_2x'),Field('ht_ft_xx'),Field('ht_ft_12'),Field('ht_ft_21'),Field('first_half_1'),Field('first_half_x'),Field('first_half_2'),Field('first_half_10'),Field('first_half_02'),Field('first_half_12'),Field('eh_min_1_1'),Field('eh_min_1_x2'),Field('u_25_1'),Field('o_25_1'),Field('u_25_x'),Field('o_25_x'),Field('u_25_2'),Field('o_25_2'),Field('first_goal_1'),Field('first_goal_2'),Field('first_goal_0'),Field('o_35_x'),Field('u_35_2'),Field('o_35_2'),Field('u_35_1'),Field('o_35_1'),Field('u_35_x'),Field('hour'),Field('update_time'),Field('btts_1'),Field('btts_2'),Field('btts_x'),Field('btts_no_x'),Field('btts_no_1'),Field('btts_no_2'),Field('u_15_1'),Field('u_15_x'),Field('u_15_2'),Field('o_15_x'),Field('o_15_1'),Field('o_15_2'),Field('eh_min_1_2'),Field('eh_min_1_x1'),Field('eh_plus_1_1'),Field('eh_plus_1_x2'),Field('eh_plus_1_2'),Field('eh_plus_1_x1'),Field('eh_plus_1_x'),Field('eh_min_1_x'),Field('btts_yes'),Field('btts_no'), migrate=False)
    wynik=defaultdict(str)
    for i in range(0,len(home_list)):
        for bookie in bookies:
            if bookie not in wynik.keys():
                wynik[bookie]=[]
        #wynik[bookie].append(db((db[bookie].home=='Leicester') & (db[bookie].away=='Watford')).select())

            wynik[bookie].append(db((db[bookie].home==home_list[i]) & (db[bookie].away==away_list[i])).select())
    for i in range(0,len(home_list)):
        for bookie in bookies:
            if len(wynik[bookie][i])==0:
                wynik[bookie][i]=db((db[bookie].home=='Test') & (db[bookie].away=='Test')).select()
            #wynik2=db((db.bookie.home=='Leicester') & (db.bookie.away=='Watford')).select()
            #wynik=[wynik1,wynik2]
        #else
        #    wynik = wynik&
    wynik_temp=db(((db.db_fortuna.home=='Barcelona'))).select()
    #q = (home=='Leicester' & away=='Watford')
    #s=db(q)
    #for i in range(0,len(home_list)):
    #    rows=db((home==home_list[i]) & (away==away_list[i])).select()
    cos=typ_list[1]    #rows = db((home=='Leicester') & (away=='Watford')).select()
    ff=wynik['db_fortuna'][0]
    #select distinct db_sts.home, db_sts.away, db_sts.data, db_sts.game_1 as sts_1, db_fortuna.game_1 as fortuna_1 from db_sts JOIN db_fortuna on (db_sts.home=db_fortuna.home and db_sts.away=db_fortuna.away)
#where db_sts.home like 'Leicester' and db_sts.away like 'Watford'
#http://web2py.com/books/default/chapter/42/06/warstwa-abstracji-bazy-danych

    return locals()

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
    db = DAL('sqlite://db.sqlite')
    db_name=db._uri
    bookies=['db_fortuna','db_sts','db_iforbet','db_lvbet','db_totolotek']
    for bookie in bookies:
        db.define_table(bookie, Field('home'),Field('away'),Field('game_1'),Field('game_0'),Field('game_2'),Field('game_10'),Field('game_02'),Field('game_12'),Field('data'),Field('Sport'),Field('League'),Field('country'),Field('dnb_1'),Field('dnb_2'),Field('o_05'),Field('o_15'),Field('o_25'),Field('o_35'),Field('o_45'),Field('o_55'),Field('o_65'),Field('o_75'),Field('o_85'),Field('o_95'),Field('u_05'),Field('u_15'),Field('u_25'),Field('u_35'),Field('u_45'),Field('u_55'),Field('u_65'),Field('u_75'),Field('u_85'),Field('u_95'),Field('ht_ft_11'),Field('ht_ft_1x'),Field('ht_ft_x1'),Field('ht_ft_22'),Field('ht_ft_x2'),Field('ht_ft_2x'),Field('ht_ft_xx'),Field('ht_ft_12'),Field('ht_ft_21'),Field('first_half_1'),Field('first_half_x'),Field('first_half_2'),Field('first_half_10'),Field('first_half_02'),Field('first_half_12'),Field('eh_min_1_1'),Field('eh_min_1_x2'),Field('u_25_1'),Field('o_25_1'),Field('u_25_x'),Field('o_25_x'),Field('u_25_2'),Field('o_25_2'),Field('first_goal_1'),Field('first_goal_2'),Field('first_goal_0'),Field('o_35_x'),Field('u_35_2'),Field('o_35_2'),Field('u_35_1'),Field('o_35_1'),Field('u_35_x'),Field('hour'),Field('update_time'),Field('btts_1'),Field('btts_2'),Field('btts_x'),Field('btts_no_x'),Field('btts_no_1'),Field('btts_no_2'),Field('u_15_1'),Field('u_15_x'),Field('u_15_2'),Field('o_15_x'),Field('o_15_1'),Field('o_15_2'),Field('eh_min_1_2'),Field('eh_min_1_x1'),Field('eh_plus_1_1'),Field('eh_plus_1_x2'),Field('eh_plus_1_2'),Field('eh_plus_1_x1'),Field('eh_plus_1_x'),Field('eh_min_1_x'),Field('btts_yes'),Field('btts_no'), migrate=False)
    wynik=defaultdict(str)
    for i in range(0,len(home_list)):
        for bookie in bookies:
            if bookie not in wynik.keys():
                wynik[bookie]=[]
        #wynik[bookie].append(db((db[bookie].home=='Leicester') & (db[bookie].away=='Watford')).select())
            wynik[bookie].append(db((db[bookie].home==home_list[i]) & (db[bookie].away==away_list[i])).select())
    for i in range(0,len(home_list)):
        for bookie in bookies:
            if len(wynik[bookie][i])==0:
                wynik[bookie][i]=db((db[bookie].home=='Test') & (db[bookie].away=='Test')).select()
            #wynik2=db((db.bookie.home=='Leicester') & (db.bookie.away=='Watford')).select()
            #wynik=[wynik1,wynik2]
        #else
        #    wynik = wynik&
#    wynik_temp=db(((db.db_sts.home=='Leicester') & (db.db_sts.away=='Watford')) | ((db.db_fortuna.home=='Leicester') & (db.db_fortuna.away=='Watford'))).select()
    #q = (home=='Leicester' & away=='Watford')
    #s=db(q)
    #for i in range(0,len(home_list)):
    #    rows=db((home==home_list[i]) & (away==away_list[i])).select()
        cos=typ_list[1]    #rows = db((home=='Leicester') & (away=='Watford')).select()
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
