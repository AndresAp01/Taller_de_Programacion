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
      7. Volver al menu principal`

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
