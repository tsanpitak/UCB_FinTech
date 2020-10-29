-- 100 Highest transaction between 7 AM and 9 AM
SELECT transac_id, transac_timestamp, amount, transac.card_id, merchant_id, card.card_holder_id, card_holder_name 
FROM transactions AS transac
    LEFT JOIN credit_card AS card ON transac.card_id = card.card_id 
    LEFT JOIN card_holder AS holder ON card.card_holder_id = holder.card_holder_id
WHERE DATE_PART('hour', transac_timestamp) BETWEEN 7 AND 9
ORDER BY amount DESC
LIMIT 100;
-- The transaction id 2451 with abnormal decimal point could be fraudulent

-- Transaction < $2.00 for each card holder
SELECT COUNT(*) AS "num_small_transac", card.card_holder_id
FROM transactions AS transac
	LEFT JOIN credit_card AS card ON transac.card_id = card.card_id
WHERE amount < 2.00
GROUP BY card.card_holder_id
ORDER BY COUNT(*) DESC;
-- Credit cards could have been hacked because, some card holders has very high small transactions compare to the mean. However, further analysis is needed on whether the small transactions are the norm for the specific card holder.

-- Top 5 merchants prone to being hack
SELECT COUNT(*) AS "num_small_transac", merchant_name
FROM transactions AS transac
	LEFT JOIN merchant AS merc ON transac.merchant_id = merc.merchant_id
WHERE amount < 2.00
GROUP BY merchant_name
ORDER BY COUNT(*) DESC
LIMIT 5;
-- 141 - Wood-Ramirez
-- 145 - Hood-Philips
--  48 - Baker Inc.
-- 119 - Henderson and Sons
--  30 - Atkinson Ltd.

SELECT transac_timestamp, transac.card_id, merchant_id, card_holder_id
FROM transactions AS transac
	LEFT JOIN credit_card AS card ON transac.card_id = card.card_id
WHERE card_holder_id IN (2,18)
	AND amount <= 2;
    
-- Fraud Detection on #25
SELECT transac_timestamp, transac.card_id, transac.merchant_id, merchant_name, merchant_cat_desc, card_holder_id, amount
FROM transactions AS transac
    LEFT JOIN credit_card AS card ON transac.card_id = card.card_id
    LEFT JOIN merchant AS merc ON transac.merchant_id = merc.merchant_id
    LEFT JOIN merchant_category AS m_cat ON merc.merchant_cat_id = m_cat.merchant_cat_id
WHERE card_holder_id = 25
	AND DATE_PART('month', transac_timestamp) <= 6
	AND DATE_PART('year', transac_timestamp) = 2018;