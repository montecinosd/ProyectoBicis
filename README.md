## Problemática:

- Una pizzeria (PizzaYA) no cuenta con una plataforma web la cual le permita a sus usuarios realizar pedidos.

## Descripción de la solución
- Desarrollo de la plataforma web, la cual es desarrollada en django, con models tales como: Ingredientes, Masa, Cliente, Pizza, Orden, Direccion

### Explicacion de los models:

1. Ingredientes: se contemplan los ingredientes que se puede usar en la pizza, cada ingrediente tiene un valor extra.
2. Masa: se contemplan las masas que se puede usar en la pizza, cada masa tiene un valor extra.
3. Pizza: Esta constituida por sus Ingredientes y su Masa, tiene un precio Total.
4. Cliente: posee los usuarios que pueden pedir pizzas.
5. Direccion: Se hace este model ya que no necesariamente la direccion del cliente es la misma del despacho.
4. Orden: La Orden tiene una Pizza y una Direccion (de despacho)

## Pasos a seguir para revisión:

1. 127.0.0.1/pizza redirecciona al login, se puede acceder como super usuario o cliente
2. Si entra como super usuario tendra privilegios tales como: CRUD Ingrediente, CRUD Masa, CRUD cliente
3. Si entra como cliente, será redireccionado a un index de usuario, el cual tendra la opcion de armar la pizza, seleccionando la masa que desea y sus ingredientes. Además, podrá ver sus ordenes realizadas.
