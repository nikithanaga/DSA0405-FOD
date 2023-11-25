import pandas as pd


series1 = pd.Series([1, 2, 3, 4], name='Series1')
series2 = pd.Series(['A', 'B', 'C', 'D'], name='Series2')


df = pd.DataFrame({series1.name: series1, series2.name: series2})

# Display the resulting DataFrame
print(df)


