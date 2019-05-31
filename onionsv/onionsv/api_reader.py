from django.http import HttpResponse
import requests
import psycopg2
import os

connection = psycopg2.connect(user=os.environ.get('SQL_USER', 'mpire'),
                                password = os.environ.get('SQL_PASSWORD', '123456'),
                                host = os.environ.get('SQL_HOST', 'database1'),
                                port = os.environ.get('SQL_PORT', '5432'),
                                database = os.environ.get('SQL_DATABASE', 'cura8'))
cursor = connection.cursor()

def test(request):
        return HttpResponse("testing successful")

def blank(request):
        return HttpResponse("blank")

def dbping(request):
        try:

                cursor.execute("SELECT version();")
                record = cursor.fetchone()
                return HttpResponse(record)
        except (Exception, psycopg2.Error) as error :
                return HttpResponse(error)
        finally:
                if(connection):
                        cursor.close()
                        connection.close()

def createtb(request):
        try:
                id = request.GET.get('id')

                create_tb_query = '''CREATE TABLE %s (ID INT PRIMARY KEY NOT NULL,TEMP1 REAL NOT NULL,TEMP2 REAL NOT NULL,TIMESTAMP TEXT NOT NULL)''' % id
                cursor.execute(create_tb_query)
                connection.commit()
                return HttpResponse("Table %s is created" % id)
        except (Exception, psycopg2.Error) as error :
                return HttpResponse(error)

def addsinglepoint(data):
        #try:
                tb = data[0:32]

                value1 = data[32:38]
                value1_int = int(value1)

                value2 = data[38:44]
                value2_int = int(value2)

                t = data[44:54]

                #check how many rows in the table
                cmd1 = '''SELECT COUNT(*) FROM %s''' %tb
                cursor.execute(cmd1)
                resp = cursor.fetchone()

                #convert the tuple to string and plus 1 to add the new point into the table
                row_num =int(''.join(str(v) for v in resp))

                cmd2= '''INSERT INTO %s (ID, TEMP1, TEMP2, TIMESTAMP) VALUES (%s, %s, %s, %s)''' %(tb, (row_num+1), value1_int, value2_int, t)
                cursor.execute(cmd2)
                #return HttpResponse("successful adding new point")
                connection.commit()
        #except (Exception, psycopg2.Error) as error :
                #return (error)

def addManyPoints(request):
        data_name_lst=[]
        try:
                num = int(request.GET.get('num'))
                result = ''
                for i in range(0,num):
                        nm = "d" + str(i + 1)
                        data_name_lst.append(nm)
                        x = data_name_lst[i]
                        data = request.GET.get(x)
                        addsinglepoint(data)

                return HttpResponse("successful <br> adding new points")
        except (Exception, psycopg2.Error) as error :
                return HttpResponse(error)

def showtable(request):
        tbname = request.GET.get('id')
        try:
                cmd = 'SELECT * FROM %s' %tbname
                cursor.execute(cmd)
                resp=cursor.fetchall()
                return HttpResponse(resp)
        except (Exception, psycopg2.Error) as error :
                return HttpResponse(error)



