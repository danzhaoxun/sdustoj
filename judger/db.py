#!/usr/bin/env python
#coding=utf-8

import time
import judger.config
import pymysql
import logging
import types

def run_sql(sql):
    '''执行sql语句,并返回结果'''
    con = None   #None
    while True:
        try:
            con = pymysql.connect(judger.config.db_host,judger.config.db_user,judger.config.db_password,
                                  judger.config.db_name,charset=judger.config.db_charset)
            break
        except: 
            logging.error('Cannot connect to database,trying again')
            time.sleep(1)
    cur = con.cursor()
    try:
        if type(sql) == types.StringType:
            cur.execute(sql)
        elif type(sql) == types.ListType:
            for i in sql:
                cur.execute(i)
    except pymysql.OperationalError as e:
        logging.error(e)
        cur.close()
        con.close()
        return False
    con.commit()
    data = cur.fetchall()
    cur.close()
    con.close()
    return data



