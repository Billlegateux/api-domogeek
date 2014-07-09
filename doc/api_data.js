define({ api: [
  {
    "type": "get",
    "url": "/holiday/:date/:responsetype",
    "title": "Holiday Status Request",
    "name": "GetHoliday",
    "group": "Domogeek",
    "description": "Ask to know if :date is a holiday",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "field": "now",
            "optional": false,
            "description": "Ask for today."
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "all",
            "optional": false,
            "description": "Ask for all entry."
          },
          {
            "group": "Parameter",
            "type": "Datetime",
            "field": "D-M-YYYY",
            "optional": false,
            "description": "Ask for specific date."
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "responsetype",
            "optional": true,
            "description": "Specify Response Type (raw by default or specify json, only for single element)."
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "   HTTP/1.1 200 OK\n   Jour de Noel\n    HTTP/1.1 200 OK\n   no\n"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "   HTTP/1.1 400 Bad Request\n   400 Bad Request\n"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "   curl http://api.domogeek.fr/holiday/now\n   curl http://api.domogeek.fr/holiday/now/json\n   curl http://api.domogeek.fr/holiday/all\n   curl http://api.domogeek.fr/holiday/25-12-2014/json\n"
      }
    ],
    "version": "0.0.0",
    "filename": "./apidomogeek.py"
  },
  {
    "type": "get",
    "url": "/schoolholiday/:zone/:daterequest/:responsetype",
    "title": "School Holiday Status Request",
    "name": "GetSchoolHoliday",
    "group": "Domogeek",
    "description": "Ask to know if :daterequest is a school holiday (UTF-8 response)",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "field": "zone",
            "optional": false,
            "description": "School Zone (A, B or C)."
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "daterequest",
            "optional": false,
            "description": "Ask for specific date {now | all | D-M-YYYY}."
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "responsetype",
            "optional": true,
            "description": "Specify Response Type (raw by default or specify json, only for single element)."
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "   HTTP/1.1 200 OK\n   Vacances de la Toussaint \n    HTTP/1.1 200 OK\n   False\n"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "   HTTP/1.1 400 Bad Request\n   400 Bad Request\n"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "   curl http://api.domogeek.fr/schoolholiday/A/now\n   curl http://api.domogeek.fr/schoolholiday/A/now/json\n   curl http://api.domogeek.fr/schoolholiday/A/all\n   curl http://api.domogeek.fr/schoolholiday/A/25-12-2014/json\n"
      }
    ],
    "version": "0.0.0",
    "filename": "./apidomogeek.py"
  },
  {
    "type": "get",
    "url": "/tempoedf/:date/:responsetype",
    "title": "Tempo EDF color Request",
    "name": "GetTempo",
    "group": "Domogeek",
    "description": "Ask the EDF Tempo color",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "field": "now",
            "optional": false,
            "description": "Ask for today."
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "tomorrow",
            "optional": false,
            "description": "Ask for tomorrow."
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "responsetype",
            "optional": true,
            "description": "Specify Response Type (raw by default or specify json, only for single element)."
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\nContent-Type: application/json\nTransfer-Encoding: chunked\nDate: Thu, 03 Jul 2014 17:16:47 GMT\nServer: localhost\n{\"tempocolor\": \"bleu\"}\n"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 400 Bad Request\n400 Bad Request\n"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "   curl http://api.domogeek.fr/tempoedf/now\n   curl http://api.domogeek.fr/tempoedf/now/json\n   curl http://api.domogeek.fr/tempoedf/tomorrow\n   curl http://api.domogeek.fr/tempoedf/tomorrow/json\n"
      }
    ],
    "version": "0.0.0",
    "filename": "./apidomogeek.py"
  },
  {
    "type": "get",
    "url": "/weekend/:daterequest/:responsetype",
    "title": "Week-end Status Request",
    "name": "GetWeekend",
    "group": "Domogeek",
    "description": "Ask to know if :daterequest is a week-end day",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "field": "daterequest",
            "optional": false,
            "description": "Ask for specific date {now | tomorrow | D-M-YYYY}."
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "responsetype",
            "optional": true,
            "description": "Specify Response Type (raw by default or specify json, only for single element)."
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "   HTTP/1.1 200 OK\n   True\n    HTTP/1.1 200 OK\n   False\n"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "   HTTP/1.1 400 Bad Request\n   400 Bad Request\n"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "   curl http://api.domogeek.fr/weekend/now\n   curl http://api.domogeek.fr/weekend/tomorrow\n   curl http://api.domogeek.fr/weekend/now/json\n   curl http://api.domogeek.fr/weekend/16-07-2014/json\n"
      }
    ],
    "version": "0.0.0",
    "filename": "./apidomogeek.py"
  }
] });