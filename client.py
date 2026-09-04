class NaturalLanguageCteSqlSynthesizerClient:
    def synthesize_cte_query(self, business_prompt='Find top 5 customers with recurring MRR growth month-over-month', target_dialect='POSTGRESQL'):
        sql_text = 'WITH monthly_mrr AS (SELECT customer_id, DATE_TRUNC("month", transaction_date) AS m, SUM(amount) AS mrr FROM subscriptions GROUP BY 1, 2) SELECT customer_id, (mrr - LAG(mrr) OVER (PARTITION BY customer_id ORDER BY m)) AS delta FROM monthly_mrr ORDER BY delta DESC LIMIT 5;'
        return {
            'synthesis_id': 'cte_sql_8812',
            'target_dialect': target_dialect,
            'synthesized_sql': sql_text,
            'cte_layers_count': 1,
            'contains_window_functions': True,
            'semantic_validation_passed': True,
            'query_plan_url': 'https://julius.sql.genpark.ai/queries/8812.json'
        }
