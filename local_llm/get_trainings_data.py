import pandas as pd

df = pd.read_csv('Beispieldaten_convertiert.csv')

df = df[['TitlePlain','DeliveryContentsText','UserInstructions','SalesArgument']].dropna()
df = df.reset_index()

"String Manipulation"
df['DeliveryContentsText'] = df['DeliveryContentsText'].str.replace('<p>', '')
df['DeliveryContentsText'] = df['DeliveryContentsText'].str.replace('</p>', '')
df['DeliveryContentsText'] = df['DeliveryContentsText'].str.replace('<ul>', '')
df['DeliveryContentsText'] = df['DeliveryContentsText'].str.replace('<li>', '')
df['DeliveryContentsText'] = df['DeliveryContentsText'].str.replace('</li>', '')
df['DeliveryContentsText'] = df['DeliveryContentsText'].str.replace('</ul>', '')
df['DeliveryContentsText'] = df['DeliveryContentsText'].str.replace('<br>', '')
df['DeliveryContentsText'] = df['DeliveryContentsText'].str.replace('</br>', '')

df['UserInstructions'] = df['UserInstructions'].str.replace('<p>', '')
df['UserInstructions'] = df['UserInstructions'].str.replace('</p>', '')
df['UserInstructions'] = df['UserInstructions'].str.replace('<h2>', '')
df['UserInstructions'] = df['UserInstructions'].str.replace('</h2>', ': ')
df['UserInstructions'] = df['UserInstructions'].str.replace('<ul>', '')
df['UserInstructions'] = df['UserInstructions'].str.replace('</ul>', '')
df['UserInstructions'] = df['UserInstructions'].str.replace('<li>', '')
df['UserInstructions'] = df['UserInstructions'].str.replace('</li>', ' / ')
df['UserInstructions'] = df['UserInstructions'].str[:-3]
df['UserInstructions'] = df['UserInstructions'].str.replace('<br>', '')
df['UserInstructions'] = df['UserInstructions'].str.replace('</br>', '')

df['SalesArgument'] = df['SalesArgument'].str.replace('<p>', '')
df['SalesArgument'] = df['SalesArgument'].str.replace('</p>', '')
df['SalesArgument'] = df['SalesArgument'].str.replace('<ul>', '')
df['SalesArgument'] = df['SalesArgument'].str.replace('</ul>', '')
df['SalesArgument'] = df['SalesArgument'].str.replace('<li>', '')
df['SalesArgument'] = df['SalesArgument'].str.replace('</li>', ' / ')
df['SalesArgument'] = df['SalesArgument'].str[:-3]
df['SalesArgument'] = df['SalesArgument'].str.replace('<br>', '')
df['SalesArgument'] = df['SalesArgument'].str.replace('</br>', '')

df['DeliveryContentsText'] = df['DeliveryContentsText'].str.strip()
df['UserInstructions'] = df['UserInstructions'].str.strip()
df['SalesArgument'] = df['SalesArgument'].str.strip()


"with pd.option_context('display.max_rows', None, 'display.max_columns', None):"

print(df.head())

new_structure_df = pd.DataFrame(columns=['Prompts'])


for index, row in df.iterrows():

    string = "DescriptionLongMarketplaces für  #### " + row['TitlePlain'] + " #### Lieferumfang: " + row[
        'DeliveryContentsText'] + " #### " + row['UserInstructions'] + " #### " + row['SalesArgument']
    new_row = {'Prompts': string}

    new_structure_df.loc[len(new_structure_df)] = new_row


new_structure_df.to_csv('output.csv', index=False)

