shuffled = capteurs.sample(len(capteurs))
query = """
SELECT *,
LAG(visiteurs_count) OVER(
    PARTITION BY weekday 
    ORDER BY date
    ) AS lag_visiteurs_count,
FROM shuffled
"""
df = duckdb.sql(query).df()
df
