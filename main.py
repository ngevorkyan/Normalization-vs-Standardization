import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

stock_file_path = 'stock.csv'
stock_df = pd.read_csv(stock_file_path)

#Plot data before changing
sns.pairplot(stock_df)
plt.show()

#Describe data before changing
print('\n------------------------------------------------')
print('Stats for original df:')
print('------------------------------------------------')
print(stock_df.describe().round(2))

#NORMALIZATION (SCALING 0 to 1)
#x' = (x - x(min))/ (x(max) - x(min))
from sklearn.preprocessing import MinMaxScaler
stock_df = pd.read_csv(stock_file_path)


scaler = MinMaxScaler()
stock_df = scaler.fit_transform(stock_df)
stock_df_normalized = pd.DataFrame(stock_df, columns = ['Interest Rates', 'Employment', 'S&P 500 Price'])

print('\n------------------------------------------------')
print('Stats for normalized df:')
print('------------------------------------------------')
print(stock_df_normalized.describe().round(2))

sns.pairplot(stock_df_normalized)
plt.show()

#STANDARDIZATION (Mean = 0 , STD = 1)
# z = x - x̄ / 𝜎


from sklearn.preprocessing import StandardScaler
stock_df = pd.read_csv(stock_file_path)

scaler = StandardScaler()
stock_df = scaler.fit_transform(stock_df)
stock_df_standardized = pd.DataFrame(stock_df, columns=['Interest Rates', 'Employment', 'S&P 500 Price'])

print('\n------------------------------------------------')
print('Stats for standardized df:')
print('------------------------------------------------')

print(stock_df_standardized.describe().round(2))
print('')

sns.pairplot(stock_df_standardized)
plt.show()
