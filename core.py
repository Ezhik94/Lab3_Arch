
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer
from operations import Base

b = Base()

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location="http://localhost:8008/",
    action='http://localhost:8008/',  # SOAPAction
    namespace="http://example.com/sample.wsdl", prefix="ns0",
    trace=True,
    ns=True)

# register the user functions
dispatcher.register_function('Create', b.create,
    returns={'Node': str},
    args={'key': str, 'data': str})

dispatcher.register_function('Read', b.read,
    returns={'Node': str},
    args={'key': str})

dispatcher.register_function('Update', b.update,
    returns={'Node': str},
    args={'key': str, 'data': str})

dispatcher.register_function('Delete', b.delete,
    returns={'Node': str},
    args={'key': str})

print "Starting server at 8008..."
httpd = HTTPServer(("", 8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()
