#Para el Proyecto 1:
Fecha:
  Semana 4 a Semana 7
  Jueves 13 de marzo a Jueves 3 de Abril

## Funciones del sistema:
### Para qué sirve
Este sistema se dirige a una cadena de restaurantes internacionales. Donde la informacion para  las compras se gfuarda en arcchivos de varios tipos.
Estos archivos se cargan automáticamente al iniciar el programa.
El usuario podra hacer varias cosas:
- [Insertar](#opcion-1-insercion-)
- [Buscar](#opcion-2-buscar)
- [Modificar](#opcion-3-modificar)
- [Crear Reportes](#opcion-4-reportes)

# Documentación
## Para el usuario:

### Tabla de contenidos
- [Instalación](#instalación-)
- [Cómo usar](#cómo-usar)
- [Insertar](#opcion-1-insercion-)
- [Buscar](#opcion-2-buscar)
- [Modificar](#opcion-3-modificar)
- [Crear Reportes](#opcion-4-reportes)
- [Para el programador](#para-el-programador)
- [Lisencia](#license)

##  Instalación 
> [!IMPORTANT]
> Simplemente descargue el archivo comprimido: "Proyecto_1.zip" y guárdelo en una carpeta donde todos los archivos estén en
una sola carpeta. No mueva ni modifique ningun archivo.

Abra el archivo "Proyecto_1.py" con el entorno que guste, de preferencia Python IDLE, PyCharm, VSCode.

## Cómo usar
Al abrir el programa este se ejecutara de manera automatica.

![pyIDLE](https://github.com/user-attachments/assets/3027cf75-4433-46aa-bc22-6fc0297709e7)

Se le presentara una serie de opciones, que veremos a continuacion.

El programa podrá verificar que no hayan códigos repetidos, si existe alguno al momento de leer los archivos, éste los descartará.

Existen 4 opciones principales: Insercion, Busqueda, Modificacion y Reportes.
### Opcion 1: Insercion    
Si selecciona la opcion 1, ingresara al menu de inserciones, donde podra registrar algo nuevo, como un pais, un producto o un cliente nuevo.
Aquí entrará en un submenú, que le mostrará 7 opciones:

      1. Insertar un nuevo país
      2. Insertar una nueva ciudad
      3. Insertar un nuevo restaurante
      4. Insertar un nuevo menú
      5. Insertar un nuevo producto
      6. Insertar un nuevo cliente
      7. Registrar compra
      8. Volver al menu principal`

Para cada opcion, usted debe ingresar los datos requeridos. Por ejemplo, para insertar un pais, solamente es necesario digitar el codigo y su nombre, luego darle "Enter" para registrar la insercion.
Sin embargo, para un restaurante, necesitara primero haber ingresado un pais y luego una ciudad.

Este programa trabaja de manera que verifica todos los datos anteriores, si quiere ingresar un restaurante nuevo, tendra que hacerlo en un pais y ciudad que existan. SI no existen, puede usar las funciones de insertar pais e insertar ciudad para hacerlo.

### Opcion 2: Buscar
Aquí entrará en un submenú, que le mostrará 7 opciones:

         1. Buscar por Páis
         2. Buscar por Ciudad
         3. Buscar por Restaurante
         4. Buscar por Menú
         5. Buscar por Producto
         6. Buscar por Cliente
         7. Volver al menu principal`

Estas opciones usted podrá buscarlas por codigo. 
Por ejemplo, si quiere buscar un restaurante con codigo 1:
![{FF232B0F-CF93-4DBC-A568-29B1D6E3BBB1}](https://github.com/user-attachments/assets/3ac6cc19-31db-4841-86c7-a139e700e441)
- Se le despliega el menu
- Escoge 3 para buscar un restaurante
- Se le devuelve los restaurantes que hayan con ese codigo asignado
El codigo se va a buscar en toda la lista, todos los restaurantes con codigo 1 de diferentes paises y/o ciudades.

### Opcion 3: Modificar

         1. Modificar un país
         2. Modificar una ciudad
         3. Modificar un restaurante
         4. Modificar un menú
         5. Modificar un producto
         6. Modificar un cliente
         
Usted puede buscar el elemento a modificar por su codigo y otorgarle un nuevo nombre o caracteristica.
Por ejemplo, si quisiera cambiarle el nombre a un producto desde donde quedamos en el ejemplo anterior:

- Primero, escoges la opcion 7 para regresar al menu de mantenimiento
- Luego, escoger la opcion 4 para entrar al menu de modificaciones
- Escoges la opcion 5 para modificar un producto
- escoges el pais, ciudad, restaurante y menu donde se encuentra el producto
- Escoges el codigo especifico del producto y le otorgas un nuevo nombre. Como son productos, te dara la opcion de cambiarle el precio y las calorias, o puedes dejar en blanco para no hacer cambios.

![{4FF3BAE5-D16C-4B1F-A7C2-4346E5CE5241}](https://github.com/user-attachments/assets/960161e4-7a02-4bab-bcfc-d62e34c6ba3d)

### Opcion 4: Reportes

         1. Para crear reporte de los países existentes
         2. Para crear reporte de las ciudades existentes
         3. Para crear reporte de los restaurantes
         4. Para crear reporte de los menús
         5. Para crear reporte de los productos
         6. Para crear reporte de los clientes
         7. Para crear reporte de las compras de un cliente
         8. Para crear reporte del restaurante más buscado
         9. Para crear reporte del menú más buscado
         10. Para crear reporte del producto más comprado
         11. Para crear reporte de la factura de mayor monto
         12. Para crear reporte de la factura de menor monto
         13. Para consultar el precio de un producto
         14. Para consultar el descuento aplicado


### Opcion 5: Salir

## Dentro de Insertar
### Para registrar una compra
Para registrar una compra de un cliente tiene que ir al menu de inserciones. Para esto, en el menu principal preisone 1. Luego presione la opcion 8 'Registrar Compra'

A este punto se le mostrara la lista de paises disponibles (Para registrar un nuevo pais o cualquier otro codigo necesario: vease ()) . Luego se le mostrara la lista de ciudades disponibles dentro de ese pais, asi, hasta llegar a productos disponibles.

Debe ingresar:
1. El codigo de un pais valido, existente.
2. El codigo de una ciudad valdia, existente.
3. El codigo de un restaurante valido, existente.
![Reg Compra 1](https://github.com/user-attachments/assets/5f5f825c-f7c0-42b5-848e-b2f75f256649)

Al llegar a la opcion de ingresar el codigo del producto, se le mostrara la opcion de ingresar la cedula del cliente. Digitela y si existe, se le mostrara el nombre del cliente. Debe indicar si la orden es para llevar tecleando 'llevar' o para comer en el restaurante 'aqui'. Luego de esto se le deslpegara el resumen de la compra del cliente, la cual usted podra modificar, escribiendo 'S' o 'N' en la consola.

![Reg Compra 2](https://github.com/user-attachments/assets/56b3b2e5-74bb-45b1-9bd8-0f217a27b3a9)

Para modificarla, ingrese 'S' o 's' y se le desplegara el menu de modificaciones. Escoga el que quiera modificar y haga los cambios respectivos.

![Reg Compra 3](https://github.com/user-attachments/assets/d68deedd-e944-4f51-9d44-f076a69c54cf)

Para terminar teclee 'N' para seguir con la factura.

Teclee 'S' para confirmar la compra.

Se creara un archivo con el siguiente nombre: "Factura_#Cedula_#Secuencia.txt"

Ademas, se enviara la informacion al archivo 'registro_compras.txt' donde se tendra la informacion de todas las facturas que vaya a tener.

![Reg Compra 4](https://github.com/user-attachments/assets/b6b708d1-a102-4025-b828-54c158353478)

### Reportes
Si quisiera obtener algun tipo de reporte, en el menu principal,  escriba '4' para entrar en el menu de reportes. Escriba '6' por ejemplo, para obtener los reportes de la cantidad de facturas de un cliente. Seguido de esto ingrese la cedula para el cual quiere obtener informacion y, si el cliente ha hecho compras, se enviara a 'reportes.txt'

![Reportes de un cliente](https://github.com/user-attachments/assets/930ae5dc-d6fb-4be7-931b-8ead7dd9f754)

Para ver el archivo de reportes, dirigase a la ruta o carpeta donde tenga el programa y busque el archivo 'reportes.txt' abralo con su editor de texto preferido.
Ejemplo de formato:

![Reportes](https://github.com/user-attachments/assets/a1595862-b6b2-4f41-8c42-3c17b8404296)


    Para salir completamente del programa. 
## Para el programador:
### Para correr este proyecto:
Se recomienta python 3.10 para correr este proyecto, además de haber hecho la instalación debida, si no existen los archivos .txt el programa no funcionará

Paises.txt

   `cod_pais;nombre`

Ciudades.txt

`cod_pais;cod_ciudad;nombre`

Restaurantes.txt

`cod_pais;cod_ciudad;cod_restaurante;nombre`

Menu.txt

`cod_pais;cod_ciudad;cod_restaurante;cod_menu;nombre`

Productos.txt 

`cod_pais;cod_ciudad;cod_restaurante;cod_menu;cod_producto;nombre`

Clientes.txt

`cedula;nombre`
