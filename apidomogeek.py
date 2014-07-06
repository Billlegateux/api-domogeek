#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Gruik coded by GuiguiAbloc
# http://blog.guiguiabloc.fr
# http://api.domogeek.fr
#

import web, sys, time
import json
from datetime import datetime
import urllib, urllib2
from Daemon import Daemon
import Holiday
import ClassTempo
import ClassSchoolCalendar

school = ClassSchoolCalendar.schoolcalendar()
dayrequest = Holiday.jourferie()
temporequest = ClassTempo.EDFTempo()

urls = (
  '/holiday/(.*)', 'holiday',
  '/tempoedf/(.*)', 'tempoedf',
  '/schoolholiday/(.*)', 'schoolholiday',
  '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        # redirect to the static file ...
        raise web.seeother('/static/index.html')


"""
@api {get} /holiday/:date/:responsetype Holiday Status Request
@apiName GetHoliday
@apiGroup Domogeek
@apiDescription Ask to know if :date is a holiday
@apiParam {String} now  Ask for today.
@apiParam {String} all  Ask for all entry.
@apiParam {Datetime} D-M-YYYY  Ask for specific date.
@apiParam {String} [responsetype]  Specify Response Type (raw by default or specify json, only for single element).
@apiSuccessExample Success-Response:
     HTTP/1.1 200 OK
     Jour de Noel

     HTTP/1.1 200 OK
     no

@apiErrorExample Error-Response:
     HTTP/1.1 400 Bad Request
     400 Bad Request

@apiExample Example usage:
     curl http://api.domogeek.fr/holiday/now
     curl http://api.domogeek.fr/holiday/now/json
     curl http://api.domogeek.fr/holiday/all
     curl http://api.domogeek.fr/holiday/25-12-2014/json

"""

class holiday:
    def GET(self,uri):
      request = uri.split('/')
      if request == ['']:
        web.badrequest()
        return "Incorrect request : /holiday/{now / date(D-M-YYYY)}\n"
      try:
        format = request[1]
      except:
        format = None
      if request[0] == "now":
        datenow = datetime.now()
        year = datenow.year
        month = datenow.month
        day = datenow.day 
        result = dayrequest.estferie([day,month,year])
        if format == "json":
          web.header('Content-Type', 'application/json')
          return json.dumps({"holiday": result})
        else:
          return result
      if request[0] == "all":
        datenow = datetime.now()
        year = datenow.year
        listvalue = []
        F, J, L = dayrequest.joursferies(year,1,'/')
        for i in xrange(0,len(F)):
          result = F[i], "%10s" % (J[i]), L[i]
          listvalue.append(result)
          response = json.dumps(listvalue)
        return response

      if request[0] != "now" and request[0] != "all":
        try:
          daterequest = request[0]
          result = daterequest.split('-') 
        except:
          web.badrequest()
          return "Incorrect date format : D-M-YYYY\n"
        try:
          day = int(result[0])
          month = int(result[1])
          year = int(result[2])
        except:
          web.badrequest()
          return "Incorrect date format : D-M-YYYY\n"
        if day > 31 or month > 12:
          web.badrequest()
          return "Incorrect date format : D-M-YYYY\n"
        result = dayrequest.estferie([day,month,year])
        if format == "json":
          web.header('Content-Type', 'application/json')
          return json.dumps({"holiday": result})
        else:
          return result

"""
@api {get} /tempoedf/:date/:responsetype Tempo EDF color Request
@apiName GetTempo
@apiGroup Domogeek
@apiDescription Ask the EDF Tempo color
@apiParam {String} now  Ask for today.
@apiParam {String} tomorrow Ask for tomorrow.
@apiParam {String} [responsetype]  Specify Response Type (raw by default or specify json, only for single element).
@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
Content-Type: application/json
Transfer-Encoding: chunked
Date: Thu, 03 Jul 2014 17:16:47 GMT
Server: localhost
{"tempocolor": "bleu"}

@apiErrorExample Error-Response:
HTTP/1.1 400 Bad Request
400 Bad Request

@apiExample Example usage:
     curl http://api.domogeek.fr/tempoedf/now
     curl http://api.domogeek.fr/tempoedf/now/json
     curl http://api.domogeek.fr/tempoedf/tomorrow
     curl http://api.domogeek.fr/tempoedf/tomorrow/json

"""

class tempoedf:
    def GET(self,uri):
      request = uri.split('/')
      if request == ['']:
        web.badrequest()
        return "Incorrect request : /tempoedf/{now | tomorrow}\n"
      try:
        format = request[1]
      except:
        format = None
      if request[0] == "now":
        result = temporequest.TempoToday()
        if format == "json":
          web.header('Content-Type', 'application/json')
          return json.dumps({"tempocolor": result})
        else:
          return result
      if request[0] == "tomorrow":
        result = temporequest.TempoTomorrow()
        if format == "json":
          web.header('Content-Type', 'application/json')
          return json.dumps({"tempocolor": result})
        else:
          return result
      web.badrequest()
      return "Incorrect request : /tempoedf/{now | tomorrow}\n"


"""
@api {get} /schoolholiday/:zone/:daterequest/:responsetype School Holiday Status Request
@apiName GetSchoolHoliday
@apiGroup Domogeek
@apiDescription Ask to know if :daterequest is a school holiday (UTF-8 response)
@apiParam {String} zone  School Zone (A, B or C).
@apiParam {String} daterequest Ask for specific date {now | all | D-M-YYYY}.
@apiParam {String} [responsetype]  Specify Response Type (raw by default or specify json, only for single element).
@apiSuccessExample Success-Response:
     HTTP/1.1 200 OK
     Vacances de la Toussaint 

     HTTP/1.1 200 OK
     False

@apiErrorExample Error-Response:
     HTTP/1.1 400 Bad Request
     400 Bad Request

@apiExample Example usage:
     curl http://api.domogeek.fr/schoolholiday/A/now
     curl http://api.domogeek.fr/schoolholiday/A/now/json
     curl http://api.domogeek.fr/schoolholiday/A/all
     curl http://api.domogeek.fr/schoolholiday/A/25-12-2014/json

"""

class schoolholiday:
    def GET(self,uri):
      request = uri.split('/')
      if request == ['']:
        web.badrequest()
        return "Incorrect request : /schoolholiday/{zone}/{now/all/date(D-M-YYYY)}\n"
      try:
        zone = request[0]
      except:
        return "Incorrect request : /schoolholiday/{zone}/{now/all/date(D-M-YYYY)}\n"
      try:
        zoneok = str(zone.upper())
      except:
        return "Wrong Zone (must be A, B or C)"
      if len(zoneok) > 1:
        return "Wrong Zone (must be A, B or C)"

      if zoneok not in ["A","B","C"]:
        return "Incorrect request : /schoolholiday/{zone}/{now/all/date(D-M-YYYY)}\n"
      try:
        daterequest = request[1]
      except:
        return "Incorrect request : /schoolholiday/{zone}/{now/all/date(D-M-YYYY)}\n"
      try:
        format = request[2]
      except:
        format = None
      datenow = datetime.now()
      year = datenow.year
      month = datenow.month
      day = datenow.day

      if daterequest == "now":
        result = school.isschoolcalendar(zoneok,day,month,year)
        if result == None :
          result = "False"
        try:
          description = result.decode('utf-8')
        except:
          description = result
        if format == "json":
          web.header('Content-Type', 'application/json')
          return json.dumps({"schoolholiday": description}, ensure_ascii=False).encode('utf8')
        else:
          return description
      if daterequest == "all":
        result = school.getschoolcalendar(zone)
        try:
          description = result.decode('unicode_escape')
        except:
          description = result
        web.header('Content-Type', 'application/json')
        return description
      if daterequest != "now" and daterequest != "all":
        try:
          result = daterequest.split('-')
        except:
          web.badrequest()
          return "Incorrect date format : D-M-YYYY\n"
        try:
          day = int(result[0])
          month = int(result[1])
          year = int(result[2])
        except:
          web.badrequest()
          return "Incorrect date format : D-M-YYYY\n"
        if day > 31 or month > 12:
          web.badrequest()
          return "Incorrect date format : D-M-YYYY\n"
        result = school.isschoolcalendar(zoneok,day,month,year)
        if result == None :
          result = "False"
        try:
          description = result.decode('utf-8')
        except:
          description = result
        if format == "json":
          web.header('Content-Type', 'application/json')
          return json.dumps({"schoolholiday": description}, ensure_ascii=False).encode('utf8')
        else:
          return description




class MyDaemon(Daemon):
        def run(self):
          app.run()

if __name__ == "__main__":

        service = MyDaemon('/tmp/apidomogeek.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        sys.argv[1] =  '80'
                        service.start()
                elif 'stop' == sys.argv[1]:
                        service.stop()
                elif 'restart' == sys.argv[1]:
                        service.restart()
                elif 'console' == sys.argv[1]:
                        sys.argv[1] =  '80'
                        service.console()

                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart|console" % sys.argv[0]
                sys.exit(2)

