-- btree index

SELECT count(*) 
from users use index(btree_index)
where birth_day  between '2000-01-01' and '2018-01-31';

SELECT count(*) 
from users use index(btree_index)
where birth_day = '2005-10-10';

SELECT count(*) 
from users use index(btree_index)
where birth_day > '2005-10-10';

SELECT count(*) 
FROM users use index(btree_index)
WHERE birth_day <= now() - INTERVAL 18 YEAR and
      birth_day > now() - INTERVAL 26 YEAR ;
      
SELECT count(*) 
from users use index(btree_index)
where MONTH(birth_day) = 1 and
      DAY(birth_day) = 1;

SELECT count(*) 
FROM users use index(btree_index)
WHERE birth_day < now() - INTERVAL 18 YEAR;


-- hash index

SELECT count(*) 
from users use index(hash_index)
where birth_day  between '2000-01-01' and '2018-01-31';

SELECT count(*) 
from users use index(hash_index)
where birth_day = '2005-10-10';

SELECT count(*) 
from users use index(hash_index)
where birth_day > '2005-10-10';

SELECT count(*) 
FROM users  use index(hash_index)
WHERE birth_day <= now() - INTERVAL 18 YEAR and
      birth_day > now() - INTERVAL 26 YEAR ;
      
SELECT count(*) 
from users use index(hash_index)
where MONTH(birth_day) = 1 and
      DAY(birth_day) = 1;

SELECT count(*) 
FROM users use index(hash_index)
WHERE birth_day < now() - INTERVAL 18 YEAR;


-- no index

SELECT count(*) 
from users use index()
where birth_day  between '2000-01-01' and '2018-01-31';

SELECT count(*) 
from users use index()
where birth_day = '2005-10-10';

SELECT count(*) 
from users use index()
where birth_day > '2005-10-10';

SELECT count(*) 
FROM users  use index()
WHERE birth_day <= now() - INTERVAL 18 YEAR and
      birth_day > now() - INTERVAL 26 YEAR ;
      
SELECT count(*) 
from users use index()
where MONTH(birth_day) = 1 and
      DAY(birth_day) = 1;

SELECT count(*) 
FROM users use index()
WHERE birth_day < now() - INTERVAL 18 YEAR;

