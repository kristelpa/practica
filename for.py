# Ejercicio 1
compras=["pollo/12/2","jugo/3/1","pan/2/5","leche/4/5","jamon/5/1","tomate/3/6"]
producto = input('Ingrese un producto: ').lower()

def buscar_producto(lst_compras, producto):
for item in compras:
    nombre,precio,cantidad = item.split('/')
    if nombre == producto:
        print(f'Precio: ${precio}')
        print(f'Cantidad: {cantidad}')
    if not nombre == producto:
        print('Producto no enontrado')

