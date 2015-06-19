from pysimplesoap.client import SoapClient, SoapFault
from time import sleep

# create a simple consumer
client = SoapClient(
    location="http://localhost:8008/",
    action='http://localhost:8008/',  # SOAPAction
    namespace="http://example.com/sample.wsdl",
    soap_ns='soap',
    trace=True,
    ns=False)

while True:
    print '1. Create new document'
    print '2. Get document by name'
    print '3. Update document by name'
    print '4. Delete document by name'
    print '5. Finish work'
    option = raw_input()

    if option == '1':
        doc_name = raw_input("Enter document name: ")
        doc_content = raw_input("Enter document content: ")
        response = client.Create(key=doc_name, data=doc_content)
        result = response.Node
        print result

    if option == '2':
        doc_name = raw_input("Enter document name: ")
        response = client.Read(key=doc_name)
        result = response.Node
        print result

    if option == '3':
        doc_name = raw_input("Enter document name: ")
        doc_content = raw_input("Enter document new content: ")
        response = client.Update(key=doc_name, data=doc_content)
        result = response.Node
        print result

    if option == '4':
        doc_name = raw_input("Enter document name: ")
        response = client.Delete(key=doc_name)
        result = response.Node
        print result

    if option == '5':
        break

    sleep(0.5)
