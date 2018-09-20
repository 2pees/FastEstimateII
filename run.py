# Flask app 
'''
 file: run.py
 version: 1.0
 author: Ian Moncrieffe
 created: sunday september 2 2018
 last_update:dir
 
'''  
'''
 NOTES:
 Here, we configure our application to point SQLALCHEMY_DATABASE_URI to a specific
    location. Then, we create an object of SQLAlchemy with the name db . As the name suggests,
    this is the object that will handle all our ORM-related activities. As mentioned earlier, this
    object has a class named Model , which provides the base for creating models in Flask.
    Any class can just subclass or inherit the Model class to create models, which will act as
    database tables.
'''

import cherrypy
from paste.translogger import TransLogger
from main import app #, manager

def run_server():
    # Enable WSGI access logging via Paste
    app_logged = TransLogger(app)

    # Mount the WSGI callable object (app) on the root directory
    cherrypy.tree.graft(app_logged, '/')

    # Set the configuration of the web server
    cherrypy.config.update({
        'engine.autoreload_on': True,
        'log.screen': True,
        'server.socket_port': 8090,
        'server.socket_host': '0.0.0.0'
    })

    # Start the CherryPy WSGI web server
    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == "__main__":
    run_server()
    #manager.run(port=8087)
    #app.run(debug=True, port=8090, threaded=True)


