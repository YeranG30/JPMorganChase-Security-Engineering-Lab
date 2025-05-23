# import libraries for data handling and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the transaction dataset
df = pd.read_csv('transactions.csv')

# show basic structure of the data
print(df.info())

# check for missing data
print(df.isnull().sum())

# visualize transaction types
df['type'].value_counts().plot(kind='bar')
plt.title('transaction types')
plt.xlabel('type')
plt.ylabel('count')
plt.tight_layout()
plt.show()

# analyze fraudulent transactions
fraud_df = df[df['isFraud'] == 1]
sns.histplot(fraud_df['amount'], bins=50, kde=True)
plt.title('fraud amount distribution')
plt.xlabel('amount')
plt.tight_layout()
plt.show()

# calculate fraud stats
total = len(df)
fraud_total = fraud_df.shape[0]
print(f"total transactions: {total}")
print(f"fraudulent transactions: {fraud_total}")
print(f"fraud rate: {round(fraud_total / total * 100, 2)}%")
