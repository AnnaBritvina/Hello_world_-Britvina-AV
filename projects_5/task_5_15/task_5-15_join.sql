SELECT p.name AS "Название товара", pr.price AS "Цена"
FROM products p
JOIN prices pr ON p.id = pr.product_id;