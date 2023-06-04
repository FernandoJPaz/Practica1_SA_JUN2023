#importamos nuestra clase cliente
from src.client import Cliente

#inicializamos nuestro objeto
cliente = Cliente()
#creamos los contactos
cliente.create(name="Fernando Jose Paz", catid=201404082, published = 1)

#listamos todos los contactos con nuestro cliente en el servidor SOAP
cliente.readList()
