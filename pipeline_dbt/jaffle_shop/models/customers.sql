select count(distinct customer_id) as cnt_customers from {{ ref("stg_customers") }}
