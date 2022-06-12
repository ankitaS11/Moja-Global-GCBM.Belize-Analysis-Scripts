import sqlite3
import pandas as pd

conn = sqlite3.connect("output/compiled_gcbm_output.db")

query = f"""
        SELECT years.year, COALESCE(SUM(i.flux_tc), 0) / 1e6 AS total_carbon_flux
        FROM (SELECT DISTINCT year FROM v_flux_indicators ORDER BY year) AS years
        LEFT JOIN v_flux_indicators i
            ON years.year = i.year
        GROUP BY years.year
        ORDER BY years.year
        """

df = pd.read_sql_query(query, conn)
ax = df.plot.line("year") # x-axis
ax.figure.savefig('output/total_carbon_mt.png', dpi=300)