# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# app configuration made easy. Look inside private/appconfig.ini
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['all'])
    db1 = DAL('sqlite://db.sqlite',pool_size=10,lazy_tables=True)
    list_of_fields=[Field('id'),Field('home'),Field('away'),Field('sts_update_time'),Field('fortuna_update_time'),Field('lvbet_update_time'),Field('iforbet_update_time'),Field('totolotek_update_time'),Field('sts_game_1'),Field('sts_game_0'),Field('sts_game_2'),Field('sts_game_10'),Field('sts_game_02'),Field('sts_game_12'),Field('data'),Field('Sport'),Field('League'),Field('country'),Field('sts_dnb_1'),Field('sts_dnb_2'),Field('sts_o_05'),Field('sts_o_15'),Field('sts_o_25'),Field('sts_o_35'),Field('sts_o_45'),Field('sts_o_55'),Field('sts_o_65'),Field('sts_o_75'),Field('sts_o_85'),Field('sts_o_95'),Field('sts_u_05'),Field('sts_u_15'),Field('sts_u_25'),Field('sts_u_35'),Field('sts_u_45'),Field('sts_u_55'),Field('sts_u_65'),Field('sts_u_75'),Field('sts_u_85'),Field('sts_u_95'),Field('sts_ht_ft_11'),Field('sts_ht_ft_1x'),Field('sts_ht_ft_x1'),Field('sts_ht_ft_22'),Field('sts_ht_ft_x2'),Field('sts_ht_ft_2x'),Field('sts_ht_ft_xx'),Field('sts_ht_ft_12'),Field('sts_ht_ft_21'),Field('sts_first_half_1'),Field('sts_first_half_x'),Field('sts_first_half_2'),Field('sts_first_half_10'),Field('sts_first_half_02'),Field('sts_first_half_12'),Field('sts_eh_min_1_1'),Field('sts_eh_min_1_x2'),Field('sts_u_25_1'),Field('sts_o_25_1'),Field('sts_u_25_x'),Field('sts_o_25_x'),Field('sts_u_25_2'),Field('sts_o_25_2'),Field('sts_first_goal_1'),Field('sts_first_goal_2'),Field('sts_first_goal_0'),Field('sts_o_35_x'),Field('sts_u_35_2'),Field('sts_o_35_2'),Field('sts_u_35_1'),Field('sts_o_35_1'),Field('sts_u_35_x'),Field('hour'),Field('sts_btts_1'),Field('sts_btts_2'),Field('sts_btts_x'),Field('sts_btts_no_x'),Field('sts_btts_no_1'),Field('sts_btts_no_2'),Field('sts_u_15_1'),Field('sts_u_15_x'),Field('sts_u_15_2'),Field('sts_o_15_x'),Field('sts_o_15_1'),Field('sts_o_15_2'),Field('sts_eh_min_1_2'),Field('sts_eh_min_1_x1'),Field('sts_eh_plus_1_1'),Field('sts_eh_plus_1_x2'),Field('sts_eh_plus_1_2'),Field('sts_eh_plus_1_x1'),Field('sts_eh_plus_1_x'),Field('sts_eh_min_1_x'),Field('sts_btts_yes'),Field('sts_btts_no'),Field('sts_corners_o_65'),Field('sts_corners_o_75'),Field('sts_corners_o_85'),Field('sts_corners_o_95'),Field('sts_corners_o_105'),Field('sts_corners_o_115'),Field('sts_corners_o_125'),Field('sts_corners_o_135'),Field('sts_corners_o_145'),Field('sts_corners_o_155'),Field('sts_corners_o_165'),Field('sts_corners_o_175'),Field('sts_corners_u_65'),Field('sts_corners_u_75'),Field('sts_corners_u_85'),Field('sts_corners_u_95'),Field('sts_corners_u_105'),Field('sts_corners_u_115'),Field('sts_corners_u_125'),Field('sts_corners_u_135'),Field('sts_corners_u_145'),Field('sts_corners_u_155'),Field('sts_corners_u_165'),Field('sts_corners_u_175'),Field('fortuna_game_1'),Field('fortuna_game_0'),Field('fortuna_game_2'),Field('fortuna_game_10'),Field('fortuna_game_02'),Field('fortuna_game_12'),Field('fortuna_Sport'),Field('fortuna_League'),Field('fortuna_country'),Field('fortuna_dnb_1'),Field('fortuna_dnb_2'),Field('fortuna_o_05'),Field('fortuna_o_15'),Field('fortuna_o_25'),Field('fortuna_o_35'),Field('fortuna_o_45'),Field('fortuna_o_55'),Field('fortuna_o_65'),Field('fortuna_o_75'),Field('fortuna_o_85'),Field('fortuna_o_95'),Field('fortuna_u_05'),Field('fortuna_u_15'),Field('fortuna_u_25'),Field('fortuna_u_35'),Field('fortuna_u_45'),Field('fortuna_u_55'),Field('fortuna_u_65'),Field('fortuna_u_75'),Field('fortuna_u_85'),Field('fortuna_u_95'),Field('fortuna_ht_ft_11'),Field('fortuna_ht_ft_1x'),Field('fortuna_ht_ft_x1'),Field('fortuna_ht_ft_22'),Field('fortuna_ht_ft_x2'),Field('fortuna_ht_ft_2x'),Field('fortuna_ht_ft_xx'),Field('fortuna_ht_ft_12'),Field('fortuna_ht_ft_21'),Field('fortuna_first_half_1'),Field('fortuna_first_half_x'),Field('fortuna_first_half_2'),Field('fortuna_first_half_10'),Field('fortuna_first_half_02'),Field('fortuna_first_half_12'),Field('fortuna_eh_min_1_1'),Field('fortuna_eh_min_1_x2'),Field('fortuna_u_25_1'),Field('fortuna_o_25_1'),Field('fortuna_u_25_x'),Field('fortuna_o_25_x'),Field('fortuna_u_25_2'),Field('fortuna_o_25_2'),Field('fortuna_first_goal_1'),Field('fortuna_first_goal_2'),Field('fortuna_first_goal_0'),Field('fortuna_o_35_x'),Field('fortuna_u_35_2'),Field('fortuna_o_35_2'),Field('fortuna_u_35_1'),Field('fortuna_o_35_1'),Field('fortuna_u_35_x'),Field('fortuna_hour'),Field('fortuna_btts_1'),Field('fortuna_btts_2'),Field('fortuna_btts_x'),Field('fortuna_btts_no_x'),Field('fortuna_btts_no_1'),Field('fortuna_btts_no_2'),Field('fortuna_u_15_1'),Field('fortuna_u_15_x'),Field('fortuna_u_15_2'),Field('fortuna_o_15_x'),Field('fortuna_o_15_1'),Field('fortuna_o_15_2'),Field('fortuna_eh_min_1_2'),Field('fortuna_eh_min_1_x1'),Field('fortuna_eh_plus_1_1'),Field('fortuna_eh_plus_1_x2'),Field('fortuna_eh_plus_1_2'),Field('fortuna_eh_plus_1_x1'),Field('fortuna_eh_plus_1_x'),Field('fortuna_eh_min_1_x'),Field('fortuna_btts_yes'),Field('fortuna_btts_no'),Field('fortuna_corners_o_65'),Field('fortuna_corners_o_75'),Field('fortuna_corners_o_85'),Field('fortuna_corners_o_95'),Field('fortuna_corners_o_105'),Field('fortuna_corners_o_115'),Field('fortuna_corners_o_125'),Field('fortuna_corners_o_135'),Field('fortuna_corners_o_145'),Field('fortuna_corners_o_155'),Field('fortuna_corners_o_165'),Field('fortuna_corners_o_175'),Field('fortuna_corners_u_65'),Field('fortuna_corners_u_75'),Field('fortuna_corners_u_85'),Field('fortuna_corners_u_95'),Field('fortuna_corners_u_105'),Field('fortuna_corners_u_115'),Field('fortuna_corners_u_125'),Field('fortuna_corners_u_135'),Field('fortuna_corners_u_145'),Field('fortuna_corners_u_155'),Field('fortuna_corners_u_165'),Field('fortuna_corners_u_175'),Field('lvbet_game_1'),Field('lvbet_game_0'),Field('lvbet_game_2'),Field('lvbet_game_10'),Field('lvbet_game_02'),Field('lvbet_game_12'),Field('lvbet_Sport'),Field('lvbet_League'),Field('lvbet_country'),Field('lvbet_dnb_1'),Field('lvbet_dnb_2'),Field('lvbet_o_05'),Field('lvbet_o_15'),Field('lvbet_o_25'),Field('lvbet_o_35'),Field('lvbet_o_45'),Field('lvbet_o_55'),Field('lvbet_o_65'),Field('lvbet_o_75'),Field('lvbet_o_85'),Field('lvbet_o_95'),Field('lvbet_u_05'),Field('lvbet_u_15'),Field('lvbet_u_25'),Field('lvbet_u_35'),Field('lvbet_u_45'),Field('lvbet_u_55'),Field('lvbet_u_65'),Field('lvbet_u_75'),Field('lvbet_u_85'),Field('lvbet_u_95'),Field('lvbet_ht_ft_11'),Field('lvbet_ht_ft_1x'),Field('lvbet_ht_ft_x1'),Field('lvbet_ht_ft_22'),Field('lvbet_ht_ft_x2'),Field('lvbet_ht_ft_2x'),Field('lvbet_ht_ft_xx'),Field('lvbet_ht_ft_12'),Field('lvbet_ht_ft_21'),Field('lvbet_first_half_1'),Field('lvbet_first_half_x'),Field('lvbet_first_half_2'),Field('lvbet_first_half_10'),Field('lvbet_first_half_02'),Field('lvbet_first_half_12'),Field('lvbet_eh_min_1_1'),Field('lvbet_eh_min_1_x2'),Field('lvbet_u_25_1'),Field('lvbet_o_25_1'),Field('lvbet_u_25_x'),Field('lvbet_o_25_x'),Field('lvbet_u_25_2'),Field('lvbet_o_25_2'),Field('lvbet_first_goal_1'),Field('lvbet_first_goal_2'),Field('lvbet_first_goal_0'),Field('lvbet_o_35_x'),Field('lvbet_u_35_2'),Field('lvbet_o_35_2'),Field('lvbet_u_35_1'),Field('lvbet_o_35_1'),Field('lvbet_u_35_x'),Field('lvbet_hour'),Field('lvbet_btts_1'),Field('lvbet_btts_2'),Field('lvbet_btts_x'),Field('lvbet_btts_no_x'),Field('lvbet_btts_no_1'),Field('lvbet_btts_no_2'),Field('lvbet_u_15_1'),Field('lvbet_u_15_x'),Field('lvbet_u_15_2'),Field('lvbet_o_15_x'),Field('lvbet_o_15_1'),Field('lvbet_o_15_2'),Field('lvbet_eh_min_1_2'),Field('lvbet_eh_min_1_x1'),Field('lvbet_eh_plus_1_1'),Field('lvbet_eh_plus_1_x2'),Field('lvbet_eh_plus_1_2'),Field('lvbet_eh_plus_1_x1'),Field('lvbet_eh_plus_1_x'),Field('lvbet_eh_min_1_x'),Field('lvbet_btts_yes'),Field('lvbet_btts_no'),Field('lvbet_corners_o_65'),Field('lvbet_corners_o_75'),Field('lvbet_corners_o_85'),Field('lvbet_corners_o_95'),Field('lvbet_corners_o_105'),Field('lvbet_corners_o_115'),Field('lvbet_corners_o_125'),Field('lvbet_corners_o_135'),Field('lvbet_corners_o_145'),Field('lvbet_corners_o_155'),Field('lvbet_corners_o_165'),Field('lvbet_corners_o_175'),Field('lvbet_corners_u_65'),Field('lvbet_corners_u_75'),Field('lvbet_corners_u_85'),Field('lvbet_corners_u_95'),Field('lvbet_corners_u_105'),Field('lvbet_corners_u_115'),Field('lvbet_corners_u_125'),Field('lvbet_corners_u_135'),Field('lvbet_corners_u_145'),Field('lvbet_corners_u_155'),Field('lvbet_corners_u_165'),Field('lvbet_corners_u_175'),Field('iforbet_game_1'),Field('iforbet_game_0'),Field('iforbet_game_2'),Field('iforbet_game_10'),Field('iforbet_game_02'),Field('iforbet_game_12'),Field('iforbet_Sport'),Field('iforbet_League'),Field('iforbet_country'),Field('iforbet_dnb_1'),Field('iforbet_dnb_2'),Field('iforbet_o_05'),Field('iforbet_o_15'),Field('iforbet_o_25'),Field('iforbet_o_35'),Field('iforbet_o_45'),Field('iforbet_o_55'),Field('iforbet_o_65'),Field('iforbet_o_75'),Field('iforbet_o_85'),Field('iforbet_o_95'),Field('iforbet_u_05'),Field('iforbet_u_15'),Field('iforbet_u_25'),Field('iforbet_u_35'),Field('iforbet_u_45'),Field('iforbet_u_55'),Field('iforbet_u_65'),Field('iforbet_u_75'),Field('iforbet_u_85'),Field('iforbet_u_95'),Field('iforbet_ht_ft_11'),Field('iforbet_ht_ft_1x'),Field('iforbet_ht_ft_x1'),Field('iforbet_ht_ft_22'),Field('iforbet_ht_ft_x2'),Field('iforbet_ht_ft_2x'),Field('iforbet_ht_ft_xx'),Field('iforbet_ht_ft_12'),Field('iforbet_ht_ft_21'),Field('iforbet_first_half_1'),Field('iforbet_first_half_x'),Field('iforbet_first_half_2'),Field('iforbet_first_half_10'),Field('iforbet_first_half_02'),Field('iforbet_first_half_12'),Field('iforbet_eh_min_1_1'),Field('iforbet_eh_min_1_x2'),Field('iforbet_u_25_1'),Field('iforbet_o_25_1'),Field('iforbet_u_25_x'),Field('iforbet_o_25_x'),Field('iforbet_u_25_2'),Field('iforbet_o_25_2'),Field('iforbet_first_goal_1'),Field('iforbet_first_goal_2'),Field('iforbet_first_goal_0'),Field('iforbet_o_35_x'),Field('iforbet_u_35_2'),Field('iforbet_o_35_2'),Field('iforbet_u_35_1'),Field('iforbet_o_35_1'),Field('iforbet_u_35_x'),Field('iforbet_hour'),Field('iforbet_btts_1'),Field('iforbet_btts_2'),Field('iforbet_btts_x'),Field('iforbet_btts_no_x'),Field('iforbet_btts_no_1'),Field('iforbet_btts_no_2'),Field('iforbet_u_15_1'),Field('iforbet_u_15_x'),Field('iforbet_u_15_2'),Field('iforbet_o_15_x'),Field('iforbet_o_15_1'),Field('iforbet_o_15_2'),Field('iforbet_eh_min_1_2'),Field('iforbet_eh_min_1_x1'),Field('iforbet_eh_plus_1_1'),Field('iforbet_eh_plus_1_x2'),Field('iforbet_eh_plus_1_2'),Field('iforbet_eh_plus_1_x1'),Field('iforbet_eh_plus_1_x'),Field('iforbet_eh_min_1_x'),Field('iforbet_btts_yes'),Field('iforbet_btts_no'),Field('iforbet_corners_o_65'),Field('iforbet_corners_o_75'),Field('iforbet_corners_o_85'),Field('iforbet_corners_o_95'),Field('iforbet_corners_o_105'),Field('iforbet_corners_o_115'),Field('iforbet_corners_o_125'),Field('iforbet_corners_o_135'),Field('iforbet_corners_o_145'),Field('iforbet_corners_o_155'),Field('iforbet_corners_o_165'),Field('iforbet_corners_o_175'),Field('iforbet_corners_u_65'),Field('iforbet_corners_u_75'),Field('iforbet_corners_u_85'),Field('iforbet_corners_u_95'),Field('iforbet_corners_u_105'),Field('iforbet_corners_u_115'),Field('iforbet_corners_u_125'),Field('iforbet_corners_u_135'),Field('iforbet_corners_u_145'),Field('iforbet_corners_u_155'),Field('iforbet_corners_u_165'),Field('iforbet_corners_u_175'),Field('totolotek_game_1'),Field('totolotek_game_0'),Field('totolotek_game_2'),Field('totolotek_game_10'),Field('totolotek_game_02'),Field('totolotek_game_12'),Field('totolotek_Sport'),Field('totolotek_League'),Field('totolotek_country'),Field('totolotek_dnb_1'),Field('totolotek_dnb_2'),Field('totolotek_o_05'),Field('totolotek_o_15'),Field('totolotek_o_25'),Field('totolotek_o_35'),Field('totolotek_o_45'),Field('totolotek_o_55'),Field('totolotek_o_65'),Field('totolotek_o_75'),Field('totolotek_o_85'),Field('totolotek_o_95'),Field('totolotek_u_05'),Field('totolotek_u_15'),Field('totolotek_u_25'),Field('totolotek_u_35'),Field('totolotek_u_45'),Field('totolotek_u_55'),Field('totolotek_u_65'),Field('totolotek_u_75'),Field('totolotek_u_85'),Field('totolotek_u_95'),Field('totolotek_ht_ft_11'),Field('totolotek_ht_ft_1x'),Field('totolotek_ht_ft_x1'),Field('totolotek_ht_ft_22'),Field('totolotek_ht_ft_x2'),Field('totolotek_ht_ft_2x'),Field('totolotek_ht_ft_xx'),Field('totolotek_ht_ft_12'),Field('totolotek_ht_ft_21'),Field('totolotek_first_half_1'),Field('totolotek_first_half_x'),Field('totolotek_first_half_2'),Field('totolotek_first_half_10'),Field('totolotek_first_half_02'),Field('totolotek_first_half_12'),Field('totolotek_eh_min_1_1'),Field('totolotek_eh_min_1_x2'),Field('totolotek_u_25_1'),Field('totolotek_o_25_1'),Field('totolotek_u_25_x'),Field('totolotek_o_25_x'),Field('totolotek_u_25_2'),Field('totolotek_o_25_2'),Field('totolotek_first_goal_1'),Field('totolotek_first_goal_2'),Field('totolotek_first_goal_0'),Field('totolotek_o_35_x'),Field('totolotek_u_35_2'),Field('totolotek_o_35_2'),Field('totolotek_u_35_1'),Field('totolotek_o_35_1'),Field('totolotek_u_35_x'),Field('totolotek_hour'),Field('totolotek_btts_1'),Field('totolotek_btts_2'),Field('totolotek_btts_x'),Field('totolotek_btts_no_x'),Field('totolotek_btts_no_1'),Field('totolotek_btts_no_2'),Field('totolotek_u_15_1'),Field('totolotek_u_15_x'),Field('totolotek_u_15_2'),Field('totolotek_o_15_x'),Field('totolotek_o_15_1'),Field('totolotek_o_15_2'),Field('totolotek_eh_min_1_2'),Field('totolotek_eh_min_1_x1'),Field('totolotek_eh_plus_1_1'),Field('totolotek_eh_plus_1_x2'),Field('totolotek_eh_plus_1_2'),Field('totolotek_eh_plus_1_x1'),Field('totolotek_eh_plus_1_x'),Field('totolotek_eh_min_1_x'),Field('totolotek_btts_yes'),Field('totolotek_btts_no'),Field('totolotek_corners_o_65'),Field('totolotek_corners_o_75'),Field('totolotek_corners_o_85'),Field('totolotek_corners_o_95'),Field('totolotek_corners_o_105'),Field('totolotek_corners_o_115'),Field('totolotek_corners_o_125'),Field('totolotek_corners_o_135'),Field('totolotek_corners_o_145'),Field('totolotek_corners_o_155'),Field('totolotek_corners_o_165'),Field('totolotek_corners_o_175'),Field('totolotek_corners_u_65'),Field('totolotek_corners_u_75'),Field('totolotek_corners_u_85'),Field('totolotek_corners_u_95'),Field('totolotek_corners_u_105'),Field('totolotek_corners_u_115'),Field('totolotek_corners_u_125'),Field('totolotek_corners_u_135'),Field('totolotek_corners_u_145'),Field('totolotek_corners_u_155'),Field('totolotek_corners_u_165'),Field('totolotek_corners_u_175')]
    db1.define_table('db_bets',*list_of_fields, migrate=False)

else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = ['*'] if request.is_local else []
# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get('forms.separator') or ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

from gluon.tools import Auth, Service, PluginManager

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=myconf.get('host.names'))
service = Service()
plugins = PluginManager()

# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.get('smtp.server')
mail.settings.sender = myconf.get('smtp.sender')
mail.settings.login = myconf.get('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)
