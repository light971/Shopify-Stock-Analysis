-- Example: Total sales by category
SELECT category, SUM(sales) AS total_sales
FROM sales_table
GROUP BY category
ORDER BY total_sales DESC;
