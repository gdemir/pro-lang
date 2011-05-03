#!/usr/bin/python
#!-*- coding:utf-8 -*-

# Code stolen from
# 	http://128.174.125.122/wiki/index.php/Python_script_for_loading_CSV_to_mySQL
#
# Original authors: Dietze Lab http://www.life.illinois.edu/dietze/
#
# Run with no args for usage instructions
#
# Notes:
#  - will probably insert duplicate records if you load the same file twice
#  - assumes that the number of fields in the header row is the same
#    as the number of columns in the rest of the file and in the database
#  - assumes the column order is the same in the file and in the database
#
# Speed: ~ 1s/MB

import sys
import os
import getpass
import MySQLdb
import csv

def main(user, db, table, csvfile):

    try:
        conn = getconn(user, db,)
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)

    cursor = conn.cursor()

    loadcsv(cursor, table, csvfile)

    cursor.close()
    conn.close()

def getconn(user, db, passwd = None):
    if passwd == None:
        passwd = getpass.getpass(prompt='%s/%s kullanıcı/veritabanı için parola?  ' % (user, db))

    # diğer ekstra tüm mysql ayarları için konfigürasyon kullanılabilir
    read_default_file = ""
    for f in (".my.cnf", "~/.my.cnf"):
        if os.path.exists(f):
            read_default_file = f
            break

    conn = MySQLdb.connect(
            host = "localhost",
            user = user,
            passwd = passwd,
            db = db,
            read_default_file = read_default_file,
    )
    conn.set_character_set('utf8')

    return conn

def nullify(L):
    """Convert empty strings in the given list to None."""

    # helper function
    def f(x):
        if(x == ""):
            return None
        else:
            return x

    return [f(x) for x in L]

def loadcsv(cursor, table, filename):

    """
    Open a csv file and load it into a sql table.
    Assumptions:
     - the first line in the file is a header
    """

    f = csv.reader(open(filename))

    header = f.next()
    numfields = len(header)

    query = buildinsertcmd(table, numfields)

    for line in f:
        vals = nullify(line)
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        cursor.execute(query, vals)
    return

def buildinsertcmd(table, numfields):

    """
    Create a query string with the given table name and the right
    number of format placeholders.

    example:
    >>> buildinsertcmd("foo", 3)
    'insert into foo values (%s, %s, %s)'
    """
    assert(numfields > 0)
    placeholders = (numfields-1) * "%s, " + "%s"
    query = ("insert into %s" % table) + (" values (%s)" % placeholders)
    return query

if __name__ == '__main__':
    # commandline execution

    args = sys.argv[1:]
    if len(args) < 4:
        sys.exit("kullanım: %s <mysql kullanıcı> <mysql db> <mysql tablo> <csv dosyası>" % sys.argv[0])

    main(*args)
