import sys
import os
import sqlite3, logging

# local
import constants

class DB():
    dbfile = None

    @staticmethod
    def query(sql, conn):
        data = []
        c = conn.cursor()

        try:
            res = c.execute(sql)
        except sqlite3.OperationalError as err:
            logging.error('error executing sql %s : %s', sql, err)
            return [False]

        for row in res:
            data.append(row)

        conn.commit()

        c.close()
        return data

    @classmethod
    def exec(cls, sql, dbname=None):
        if not sql: return False

        if (dbname): cls.dbfile = dbname
        conn = sqlite3.connect(cls.dbfile) 

        if (not callable( getattr(sql, 'split', None) )):
            return False;

        rowed = sql.split(';')

        res = []
        for r in rowed:
            res.append( cls.query(r, conn) )
            # try-catch block will be here

        conn.close()
        return [x for sublist in res for x in sublist] == []

    @classmethod
    def fetch(cls, sql, dbname=None):
        if not sql: return False

        if (dbname): cls.dbfile = dbname
        conn = sqlite3.connect(cls.dbfile) 

        rowed = sql.split(';')

        res = []
        for r in rowed:
            logging.debug(r)
            res.append( cls.query(r, conn) )
            # try-catch block will be here

        logging.debug(res)

        conn.close()
        return [x for sublist in res for x in sublist]

# DB.dbfile = Config.get('dbfile')
DB.dbfile = constants.DB_FILE
