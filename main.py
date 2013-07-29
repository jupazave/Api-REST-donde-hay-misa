
import re
import webapp2
from google.appengine.api import urlfetch
from BeautifulSoup import *
from google.appengine.ext import db
import json as simplejson
import os
from google.appengine.ext.webapp import template
from google.appengine.api import taskqueue

def gql_json_parser(query_obj):
    result = []
    for entry in query_obj:
        result.append(dict([(p, (unicode(getattr(entry, p)))) for p in entry.properties()]))
    return result
    
  
class MainHandler(webapp2.RequestHandler):
    
    def get(self):
        template_values = dict()
        path = os.path.join(os.path.dirname(__file__),'templates', 'index.html')
        self.response.out.write(template.render(path, template_values))

class PruebaHandler(webapp2.RequestHandler):
    
    def get(self):
        template_values = dict()
        path = os.path.join(os.path.dirname(__file__),'templates', 'prueba.html')
        self.response.out.write(template.render(path, template_values))
           
class RunnerHandler(webapp2.RequestHandler):
    
    def get(self):
        taskqueue.add(url='/diputado/crawl')
        self.response.write("Corriendo Task")

class DomingoHandler(webapp2.RequestHandler):
    
    def get(self,id):
        iglesias = list(dict())
        url = "http://dondehaymisa.com/ajax2.asp?op=4&d=1&m=-1&hora=0&tipo=0&cad=&col=-1&expl=1&dia=1&e=%s" % id
        content = urlfetch.fetch(url,deadline=90).content
        soup = BeautifulSoup(content)
        
        dumped = soup.find("table").findAll("tr", bgcolor="#F5F5F5")
        for iglesia in dumped:
            arquidiosesis = iglesia.findAll("td", valign="top")[1].findAll("font")[0].text
            nombre = iglesia.findAll("td", valign="top")[1].findAll("font")[1].text
            direccion = iglesia.findAll("td", valign="top")[1].findAll("font")[2].text
            misas = iglesia.findAll("td", valign="top")[1].findAll("font")[3].text
            image = iglesia.find("img")["src"]
            iglesias.append({
                "nombre": nombre,
                "arquidiosesis": arquidiosesis,
                "direccion": direccion,
                "horarios": misas,
                "imagen" : image, 
                })
            pass
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(simplejson.dumps(iglesias))

class LunesHandler(webapp2.RequestHandler):
    
    def get(self,id):
        iglesias = list(dict())
        url = "http://dondehaymisa.com/ajax2.asp?op=4&d=1&m=-1&hora=0&tipo=0&cad=&col=-1&expl=1&dia=2&e=%s" % id
        content = urlfetch.fetch(url,deadline=90).content
        soup = BeautifulSoup(content)
        
        dumped = soup.find("table").findAll("tr", bgcolor="#F5F5F5")
        for iglesia in dumped:
            arquidiosesis = iglesia.findAll("td", valign="top")[1].findAll("font")[0].text
            nombre = iglesia.findAll("td", valign="top")[1].findAll("font")[1].text
            direccion = iglesia.findAll("td", valign="top")[1].findAll("font")[2].text
            misas = iglesia.findAll("td", valign="top")[1].findAll("font")[3].text
            image = iglesia.find("img")["src"]
            iglesias.append({
                "nombre": nombre,
                "arquidiosesis": arquidiosesis,
                "direccion": direccion,
                "horarios": misas,
                "imagen" : image, 
                })
            pass
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(simplejson.dumps(iglesias))
 
class MartesHandler(webapp2.RequestHandler):
    
    def get(self,id):
        iglesias = list(dict())
        url = "http://dondehaymisa.com/ajax2.asp?op=4&d=1&m=-1&hora=0&tipo=0&cad=&col=-1&expl=1&dia=3&e=%s" % id
        content = urlfetch.fetch(url,deadline=90).content
        soup = BeautifulSoup(content)
        
        dumped = soup.find("table").findAll("tr", bgcolor="#F5F5F5")
        for iglesia in dumped:
            arquidiosesis = iglesia.findAll("td", valign="top")[1].findAll("font")[0].text
            nombre = iglesia.findAll("td", valign="top")[1].findAll("font")[1].text
            direccion = iglesia.findAll("td", valign="top")[1].findAll("font")[2].text
            misas = iglesia.findAll("td", valign="top")[1].findAll("font")[3].text
            image = iglesia.find("img")["src"]
            iglesias.append({
                "nombre": nombre,
                "arquidiosesis": arquidiosesis,
                "direccion": direccion,
                "horarios": misas,
                "imagen" : image, 
                })
            pass
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(simplejson.dumps(iglesias))

class MiercolesHandler(webapp2.RequestHandler):
    
    def get(self,id):
        iglesias = list(dict())
        url = "http://dondehaymisa.com/ajax2.asp?op=4&d=1&m=-1&hora=0&tipo=0&cad=&col=-1&expl=1&dia=4&e=%s" % id
        content = urlfetch.fetch(url,deadline=90).content
        soup = BeautifulSoup(content)
        
        dumped = soup.find("table").findAll("tr", bgcolor="#F5F5F5")
        for iglesia in dumped:
            arquidiosesis = iglesia.findAll("td", valign="top")[1].findAll("font")[0].text
            nombre = iglesia.findAll("td", valign="top")[1].findAll("font")[1].text
            direccion = iglesia.findAll("td", valign="top")[1].findAll("font")[2].text
            misas = iglesia.findAll("td", valign="top")[1].findAll("font")[3].text
            image = iglesia.find("img")["src"]
            iglesias.append({
                "nombre": nombre,
                "arquidiosesis": arquidiosesis,
                "direccion": direccion,
                "horarios": misas,
                "imagen" : image, 
                })
            pass
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(simplejson.dumps(iglesias))

class JuevesHandler(webapp2.RequestHandler):
    
    def get(self,id):
        iglesias = list(dict())
        url = "http://dondehaymisa.com/ajax2.asp?op=4&d=1&m=-1&hora=0&tipo=0&cad=&col=-1&expl=1&dia=5&e=%s" % id
        content = urlfetch.fetch(url,deadline=90).content
        soup = BeautifulSoup(content)
        
        dumped = soup.find("table").findAll("tr", bgcolor="#F5F5F5")
        for iglesia in dumped:
            arquidiosesis = iglesia.findAll("td", valign="top")[1].findAll("font")[0].text
            nombre = iglesia.findAll("td", valign="top")[1].findAll("font")[1].text
            direccion = iglesia.findAll("td", valign="top")[1].findAll("font")[2].text
            misas = iglesia.findAll("td", valign="top")[1].findAll("font")[3].text
            image = iglesia.find("img")["src"]
            iglesias.append({
                "nombre": nombre,
                "arquidiosesis": arquidiosesis,
                "direccion": direccion,
                "horarios": misas,
                "imagen" : image, 
                })
            pass
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(simplejson.dumps(iglesias))

class ViernesHandler(webapp2.RequestHandler):
    
    def get(self,id):
        iglesias = list(dict())
        url = "http://dondehaymisa.com/ajax2.asp?op=4&d=1&m=-1&hora=0&tipo=0&cad=&col=-1&expl=1&dia=6&e=%s" % id
        content = urlfetch.fetch(url,deadline=90).content
        soup = BeautifulSoup(content)
        
        dumped = soup.find("table").findAll("tr", bgcolor="#F5F5F5")
        for iglesia in dumped:
            arquidiosesis = iglesia.findAll("td", valign="top")[1].findAll("font")[0].text
            nombre = iglesia.findAll("td", valign="top")[1].findAll("font")[1].text
            direccion = iglesia.findAll("td", valign="top")[1].findAll("font")[2].text
            misas = iglesia.findAll("td", valign="top")[1].findAll("font")[3].text
            image = iglesia.find("img")["src"]
            iglesias.append({
                "nombre": nombre,
                "arquidiosesis": arquidiosesis,
                "direccion": direccion,
                "horarios": misas,
                "imagen" : image, 
                })
            pass
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(simplejson.dumps(iglesias))

class SabadoHandler(webapp2.RequestHandler):
    
    def get(self,id):
        iglesias = list(dict())
        url = "http://dondehaymisa.com/ajax2.asp?op=4&d=1&m=-1&hora=0&tipo=0&cad=&col=-1&expl=1&dia=7&e=%s" % id
        content = urlfetch.fetch(url,deadline=90).content
        soup = BeautifulSoup(content)
        
        dumped = soup.find("table").findAll("tr", bgcolor="#F5F5F5")
        for iglesia in dumped:
            arquidiosesis = iglesia.findAll("td", valign="top")[1].findAll("font")[0].text
            nombre = iglesia.findAll("td", valign="top")[1].findAll("font")[1].text
            direccion = iglesia.findAll("td", valign="top")[1].findAll("font")[2].text
            misas = iglesia.findAll("td", valign="top")[1].findAll("font")[3].text
            image = iglesia.find("img")["src"]
            iglesias.append({
                "nombre": nombre,
                "arquidiosesis": arquidiosesis,
                "direccion": direccion,
                "horarios": misas,
                "imagen" : image, 
                })
            pass
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(simplejson.dumps(iglesias))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/run', RunnerHandler),
    ('/pruebas', PruebaHandler),
    ('/lunes/(\d+)$', LunesHandler),
    ('/martes/(\d+)$', MartesHandler),
    ('/miercoles/(\d+)$', MiercolesHandler),
    ('/jueves/(\d+)$', JuevesHandler),
    ('/viernes/(\d+)$', ViernesHandler),
    ('/sabado/(\d+)$', SabadoHandler),
    ('/domingo/(\d+)$', DomingoHandler),
    ], debug=True)
