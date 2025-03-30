#Para el Proyecto 1:
Fecha:
  Semana 4 a Semana 7
  Jueves 13 de marzo a Jueves 3 de Abril

## Funciones del sistema:
### Para que sirve
Este sistema se dirige a una cadena de restaurantes internacionales. Donde la informacion para  las compras se gfuarda en arcchivos de varios tipos.
Estos archivos se cargan automaticamente al iniciar el programa.
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

Simplemente descargue el archivo comprimido: "Proyecto_1.zip" y guárdelo en una carpeta donde todos los archivos estén en
una sola carpeta. No mueva ni modifique ningun archivo.

Abra el archivo "Proyecto_1.py" con el entorno que guste, de preferencia Python IDLE, PyCharm, VSCode.

## Cómo usar
El programa podrá verificar que no hayan códigos repetidos, si existe alguno al momento de leer los archivos, éste los descartará.
Al iniciar el programa tiene cuatro opciones:

### Opcion 1: Insercion    

Aquí entrará en un submenú, que le mostrará 7 opciones:

      1. Insertar un nuevo país
      2. Insertar una nueva ciudad
      3. Insertar un nuevo restaurante
      4. Insertar un nuevo menú
      5. Insertar un nuevo producto
      6. Insertar un nuevo cliente
      7. Volver al menu principal`

Aquí entrará en un submenú, que le mostrará 7 opciones:
### Opcion 2: Buscar

         1. Buscar por Páis
         2. Buscar por Ciudad
         3. Buscar por Restaurante
         4. Buscar por Menú
         5. Buscar por Producto
         6. Buscar por Cliente
         7. Volver al menu principal`

Estas opciones usted podrá buscarlas por nombre, para que le despliegue el código exacto que quiera utilizar. 
### Opcion 3: Modificar

         1. Modificar un país
         2. Modificar una ciudad
         3. Modificar un restaurante
         4. Modificar un menú
         5. Modificar un producto
         6. Modificar un cliente
Usted puede buscar el elemento a modificar por su codigo y otorgarle un nuevo nombre.

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
