CREATE TABLE clientes (
 id_cliente int,
 nombre varchar(30),
 apellido varchar(40),
 email varchar(50),
 telefono int
 );

CREATE TABLE ventas (
    id_venta int,
    id_cliente int,
    fecha date,
    total int
);

CREATE TABLE detalle_ventas (
    id_detalle int,
    id_venta int,
    id_libro int,
    cantidad int,
    subtotal int
);

CREATE TABLE detalle_ventas (
    id_libro int,
    titulo varchar(50),
    autor varchar(80),
    precio int,
    stock int,
    editorial varchar(90),
);