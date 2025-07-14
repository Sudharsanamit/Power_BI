import pandas as pd

# Load CSV files
internet = pd.read_csv("number-of-internet-users.csv")
population = pd.read_csv("population.csv")
fixed = pd.read_csv("fixed-telephone-subscriptions-per-100-people.csv")
mobile = pd.read_csv("mobile-cellular-subscriptions-per-100-people.csv")

# Rename columns for clarity
internet.columns = ['Entity', 'Code', 'Year', 'InternetUsers']
population.columns = ['Entity', 'Code', 'Year', 'Population']
fixed.columns = ['Entity', 'Code', 'Year', 'LandlineUsersPer100']
mobile.columns = ['Entity', 'Code', 'Year', 'MobileUsersPer100']

# Filter for last 15 years
years_to_keep = list(range(2008, 2024))
internet = internet[internet['Year'].isin(years_to_keep)]
population = population[population['Year'].isin(years_to_keep)]
fixed = fixed[fixed['Year'].isin(years_to_keep)]
mobile = mobile[mobile['Year'].isin(years_to_keep)]

# Merge datasets
df = internet.merge(population, on=['Entity', 'Code', 'Year'], how='left') \
             .merge(fixed, on=['Entity', 'Code', 'Year'], how='left') \
             .merge(mobile, on=['Entity', 'Code', 'Year'], how='left')

# Calculate InternetUsersPer100
df['InternetUsersPer100'] = (df['InternetUsers'] / df['Population']) * 100

# Round values
df['InternetUsersPer100'] = df['InternetUsersPer100'].round(2)
df['MobileUsersPer100'] = df['MobileUsersPer100'].round(2)
df['LandlineUsersPer100'] = df['LandlineUsersPer100'].round(2)

# Drop rows with missing critical values
df.dropna(subset=['InternetUsersPer100', 'MobileUsersPer100', 'LandlineUsersPer100'], inplace=True)

# Export cleaned file
df.to_csv("cleaned_tech_adoption.csv", index=False)
print("✅ File saved as 'cleaned_tech_adoption.csv'")
