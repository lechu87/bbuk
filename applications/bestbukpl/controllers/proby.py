# -*- coding: utf-8 -*-
# spróbój czegos takiego jak
def index(): return dict()

def kupon():
    if not session.ids:
        session.ids=[]
    else:
        session.ids.append(2)
    return request.vars.text_value

def testFunction(a):
    if not request.vars.a:
        request.vars.a=123
    session.id=request.vars.a
    return session.id

def aaa(a):
    if not request.vars.a:
        request.vars.a=123
    session.id=request.vars.a
    return session.id

def add_session():
    game_id=request.vars.game_id
    a=request.vars.game
    home=request.vars.home
    away=request.vars.away
    typ=request.vars.typ
    odd=request.vars.odd
    custom_id=game_id+odd
    kurs=request.vars.kurs
    #if request.vars.cos:
    #    session.cos=request.vars.cos
    if not session['games']:
        session['games']={}
    if custom_id in session.games:
        del(session.games[custom_id])
    elif game_id is not None:
        session.games[custom_id]={}
        session.games[custom_id]['home']=home
        session.games[custom_id]['away']=away
        session.games[custom_id]['typ']=typ
        session.games[custom_id]['odd']=odd
        session.games[custom_id]['kurs']=kurs
    return locals()

def one():
    return dict()

def echo():
    return "jQuery('#target').html(%s);" % repr(request.vars.name)

def kwota():
    try:
        cash=int(request.vars.name) * 2.05 * 1.98 * 0.88
    except:
        cash=0
    return cash

def podatek():
    try:
        tax=int(request.vars.name) * 0.12
    except:
        tax=0
    return tax

def clear_session():
    session=None
    return locals

def echo():
    return "jQuery('#target').html(%s);" % repr(session)
