/*

Scrivete una query SQL che restituisca solo i record dalla tabella "products" con un prezzo superiore a 50

*/

select * from products where products.buyPrice >= 50


-- Scrivete una query SQL che restituisca tutti i record dalla tabella "orders" ordinati per data in ordine decrescente.

select * from orders order by orders.orderDate desc 


-- Scrivete una query SQL che aggiorni il prezzo di tutti i prodotti nella tabella"products" aumentandolo del 10%.

update products set buyPrice = buyPrice * 1.1

-- Scrivete una query SQL che inserisca un nuovo utente nella tabella" customers".
-- puoi usare describe per la signature di cosa può essere null, ecc
insert  into customers(customerNumber,customerName,contactLastName,contactFirstName,phone,addressLine1,addressLine2,city,state,postalCode,country,salesRepEmployeeNumber,creditLimit) values 
(200, "Art Attack-Ati", "Giovanni", "Muciaccia", "1234567890", "Via Dalle Palle 2", NULL, "Condrieu", NULL, "69420", "France", 1370,'21000.00')


-- Scrivete una query SQL che elimini tutti gli ordini nella tabella "orders" con hanno lo stato "Cancelled".

--delete from orders where status = "Cancelled"

--delete select orderNumber from orders where status = "Cancelled" from orders join orderdetails

delete from orderdetails where orderNumber IN
(select orderNumber from orders where status = "Cancelled");
delete from orders where status = "Cancelled"


-- Scrivete una query SQL che restituisca tutti gli utenti dalla tabella "customers" il cui nome inizia con la S e vivono in California.

select * from customers where contactFirstName like "S%" and state = "CA";


-- Si vogliono recuperare dal database "world" la lingua e la nazione di ogni città.

select city.Name, countrylanguage.Language from (country join city on country.Code = city.CountryCode) join countrylanguage on countrylanguage.CountryCode = country.Code