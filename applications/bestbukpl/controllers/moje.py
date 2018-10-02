# -*- coding: utf-8 -*-
# spróbój czegos takiego jak
def index(): return dict(message="hello from moje.py")

def aaa(a):
    if not request.vars.a:
        request.vars.a=123
    session.id=request.vars.a
    return session.id
