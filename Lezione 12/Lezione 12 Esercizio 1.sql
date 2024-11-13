-- Si vuole recuperare il numero di città per nazione dal database "world" mostrando anche il nome della nazione
-- ordinando il risultato in base al numero di città.


select country.Name, country.Code, count(city.Name) as "Numero di città" from country left outer join city on country.Code = city.COuntryCode group by country.Code;
-- a quanto pare esistono nel db paesi senza città


-- Si vuole conoscere la lista di repubbliche con aspettativa di vita maggiore dei 70 anni

select distinct country.Name from country where country.GovernmentForm like "%Republic%" and country.LifeExpectancy >= 70

-- qui escono 143 paesi con nome o forma di governo che contengono "epublic"
select country.GovernmentForm, count(country.Code) from country where country.name like "%epublic%" or country.GovernmentForm like "%epublic%" group by country.GovernmentForm;


-- Si vuole recuperare dal database WORLD le lingue parlate per nazione con la rispettiva percentuale di utilizzo;
-- crea vista sulla query


create or replace view showlanguages as
select country.Name, country.Code, countrylanguage.Language, countrylanguage.Percentage
from country join countrylanguage on country.Code = countrylanguage.CountryCode
order by country.Name asc, countrylanguage.Percentage desc