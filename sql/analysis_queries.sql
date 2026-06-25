SELECT
    scheme_name,
    fund_house,
    category,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

SELECT
    AVG(amount_inr) AS average_transaction
FROM fact_transactions;

SELECT
    payment_mode,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_transactions DESC;

SELECT
    kyc_status,
    COUNT(*) AS total
FROM fact_transactions
GROUP BY kyc_status;

SELECT
    AVG(expense_ratio_pct) AS average_expense_ratio
FROM fact_performance;