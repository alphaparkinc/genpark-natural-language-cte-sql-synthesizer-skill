from client import NaturalLanguageCteSqlSynthesizerClient

def main():
    client = NaturalLanguageCteSqlSynthesizerClient()
    res = client.synthesize_cte_query('Top customers by MoM revenue growth')
    print('CTE SQL Synthesizer: ' + res['synthesis_id'] + ' (' + res['target_dialect'] + ')')
    print('SQL Preview: ' + res['synthesized_sql'][:70] + '...')
    print('Valid: ' + str(res['semantic_validation_passed']) + ' | Plan URL: ' + res['query_plan_url'])

if __name__ == '__main__':
    main()
