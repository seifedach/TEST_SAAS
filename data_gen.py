import seaborn as sns

# Load the tips dataset
tips_df = sns.load_dataset("tips")

tips_df[['total_bill','tip','size']].to_csv('data_test.csv')
