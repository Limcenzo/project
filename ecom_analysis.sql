CREATE DATABASE ecom_analysis;
USE ecom_analysis;

-- 1	What is the total revenue generated?	

SELECT * FROM ecom_analysis;

SELECT ROUND(SUM(revenue),2) AS total_revenue FROM ecom_analysis;

-- 2	How many unique orders and customers are recorded?

SELECT COUNT(DISTINCT order_id) AS total_orders,COUNT(DISTINCT customer_id) AS total_customers
FROM ecom_analysis;	

-- 3	What is the average, maximum, and minimum order revenue?	

SELECT ROUND(AVG(revenue),2) AS avg_revenue, MAX(revenue) AS max_revenue,MIN(revenue) AS min_revenue
FROM ecom_analysis;

-- 4	Which product categories generate the most revenue?	

SELECT product_category, ROUND(SUM(revenue),2) AS total_revenue 
FROM ecom_analysis
GROUP BY product_category
ORDER BY total_revenue;

-- 5	Which 10 products have the highest revenue?	

SELECT product_name,ROUND(SUM(revenue),2) AS total_revenue
FROM ecom_analysis
GROUP BY product_name; 

-- 6	Which categories have revenue above a chosen threshold?	

SELECT product_category, SUM(revenue) AS total_revenue
FROM ecom_analysis
GROUP BY product_category;

-- 7	What is the revenue contribution percentage of each category?

SELECT product_category, (SUM(revenue) * 100)/(SELECT SUM(revenue) FROM ecom_analysis) AS pct_contribution
FROM ecom_analysis
GROUP BY product_category;

-- 8	Which cities generate the highest revenue?	

SELECT shipping_city, SUM(revenue) AS total_revenue
FROM ecom_analysis
GROUP BY shipping_city;

-- 9	Which countries have more than a specified number of orders?

WITH country_orders AS (
    SELECT 
        country,
        COUNT(DISTINCT order_id) AS order_count
    FROM ecom_analysis 
    GROUP BY country 
)
SELECT 
    country,
    order_count 
FROM country_orders
WHERE order_count > (SELECT AVG(order_count) FROM country_orders);

-- 10	Which payment method generates the highest average order revenue?

SELECT payment_method, ROUND(SUM(revenue)/COUNT(DISTINCT order_id),2) AS average_order_revenue
FROM ecom_analysis
GROUP BY payment_method
ORDER BY average_order_revenue DESC
LIMIT 1;
	
-- 11	How do order counts and revenue vary by order status?	

SELECT order_status,ROUND(SUM(revenue),2) AS total_revenue, COUNT(DISTINCT order_id) AS order_count
FROM ecom_analysis
GROUP BY order_status;

-- 12	What is the monthly revenue and order count?	

SELECT DATE_FORMAT(order_date,'%Y-%m') AS month_, ROUND(SUM(revenue),2) AS monthly_revenue, COUNT(DISTINCT order_id) AS order_count 
FROM ecom_analysis
GROUP BY month_;

-- 13	Which month has the highest revenue in each year?	

WITH MonthlyRevenue AS (SELECT DATE_FORMAT(order_date,'%Y-%m') AS month_, ROUND(SUM(revenue),2) AS monthly_revenue,
DENSE_RANK () OVER (PARTITION BY YEAR(order_date)
ORDER BY ROUND(SUM(revenue),2) DESC) AS rank_
FROM ecom_analysis
GROUP BY DATE_FORMAT(order_date, '%Y-%m'), YEAR(order_date)
)
SELECT month_,monthly_revenue
FROM MonthlyRevenue
WHERE rank_ = 1
ORDER BY month_;

-- 14	How does monthly revenue compare with the previous month?

WITH monthly_revenue AS (
    SELECT
        DATE_FORMAT(order_date, '%Y-%m') AS month_,
        SUM(revenue) AS total_revenue
    FROM ecom_analysis
    WHERE order_date IS NOT NULL
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
),
revenue_comparison AS (
    SELECT
        month_,
        total_revenue,
        LAG(total_revenue) OVER (ORDER BY month_) AS previous_month_revenue
    FROM monthly_revenue
)
SELECT
    month_,
    total_revenue,
    previous_month_revenue,
    total_revenue - previous_month_revenue AS revenue_change
FROM revenue_comparison;

	
-- 15	What is the cumulative revenue over time?	

WITH MonthlyRevenue AS (
    SELECT 
        DATE_FORMAT(order_date, '%Y-%m') AS month_,
        ROUND(SUM(revenue), 2) AS monthly_revenue
    FROM ecom_analysis
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT 
    month_, 
    monthly_revenue,
    SUM(ROUND(monthly_revenue,2)) OVER (ORDER BY month_) AS cumulative_revenue
FROM MonthlyRevenue
ORDER BY month_;

-- 16	Which products have above-average revenue?	

WITH ProductRevenue AS (SELECT product_name, ROUND(SUM(revenue),2) AS total_revenue
FROM ecom_analysis
GROUP BY product_name)
SELECT product_name, total_revenue
FROM ProductRevenue
WHERE total_revenue > (SELECT AVG(revenue) FROM ecom_analysis)
GROUP BY product_name;

-- 17	Which products have an average customer rating below the overall average?	

WITH avg_rating AS (SELECT product_name, SUM(customer_rating)
FROM ecom_analysis
GROUP BY product_name)
SELECT product_name, customer_rating
FROM avg_rating
WHERE customer_rating < (SELECT AVG(customer_rating) FROM ecom_analysis);

-- 18	Which product category has the highest average customer rating in each country?	

WITH CategoryRatings AS (SELECT product_category, country, ROUND(AVG(customer_rating),2) AS avg_rating,
DENSE_RANK () OVER (
PARTITION BY country 
ORDER BY ROUND(AVG(customer_rating), 2) DESC) AS rank_
FROM ecom_analysis
GROUP BY product_category, country)
SELECT product_category, country, avg_rating
FROM CategoryRatings
WHERE rank_ = 1;


-- 19	What percentage of orders are cancelled or returned?

SELECT order_status , COUNT(DISTINCT order_id) * 100/(SELECT COUNT(DISTINCT order_id) FROM ecom_analysis) AS pct_contribution
FROM ecom_analysis
WHERE order_status IN ('cancelled', 'returned')
GROUP BY order_status;	

-- 20	Which products have high revenue but low customer ratings?	

WITH revenue_high_low_rating AS (SELECT product_name, ROUND(SUM(revenue),2) AS total_revenue, ROUND(AVG(customer_rating),2) AS avg_rating 
FROM ecom_analysis
GROUP BY product_name)
SELECT  product_name, total_revenue, avg_rating 
FROM revenue_high_low_rating
WHERE total_revenue > (SELECT AVG(revenue) FROM ecom_analysis) AND avg_rating < (SELECT AVG(customer_rating) FROM ecom_analysis)
GROUP BY product_name;
