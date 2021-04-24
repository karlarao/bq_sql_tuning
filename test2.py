
from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

query = """
with cte as (
SELECT /* tst cte_query */ b.* 
FROM `example-prod-284123.dataset01.table01` a
inner join `example-dev-284123.dataset01.table01` b
on a.col1 = b.col1
)
SELECT /* now3 main_query */ b.* 
FROM `example-prod-284123.dataset01.table01` a
inner join `example-dev-284123.dataset01.table01` b
on a.col1 = b.col1
inner join cte
on a.col1 = cte.col1
inner join (SELECT /* subquery */ b.* 
FROM `example-prod-284123.dataset01.table01` a
inner join `example-dev-284123.dataset01.table01` b
on a.col1 = b.col1) sq
on a.col1 = sq.col1
"""
query_job = client.query(query)  # Make an API request.

print("done")
#for row in query_job:
#    print(','.join(row))
