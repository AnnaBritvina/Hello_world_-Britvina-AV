SELECT * FROM products WHERE category = 'электроника';
SELECT * FROM products WHERE category = 'одежда' AND name LIKE '%женские%';
SELECT * FROM products WHERE category = 'продукты' OR category = 'книги';
SELECT * FROM products WHERE NOT category = 'бытовая техника';
SELECT * FROM products WHERE category IN ('электроника', 'одежда', 'книги');
SELECT * FROM products 
WHERE (category = 'электроника' AND name LIKE '%Samsung%') 
   OR category = 'бытовая техника';
SELECT * FROM products 
WHERE (category IN ('электроника', 'одежда', 'бытовая техника') 
       AND id BETWEEN 1 AND 15 
       AND name NOT LIKE '%Samsung%')
   OR category = 'книги';
