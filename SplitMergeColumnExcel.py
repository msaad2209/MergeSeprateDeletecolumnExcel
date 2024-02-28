import pandas as pd

#Step 1: Opining excel as df, defining input and output file names and positions columns to be removed 
input_file = "10128_OpenEnd_stacked.xlsx"
output_file = input_file.replace('.xlsx', '_Updated.xlsx')

df = pd.read_excel(input_file)
result_array = [5,25,25,27]
name_array = ['a4v1a6','a4v1a6','a5_other','a5_other']

print(result_array)        
print(name_array)

df[name_array[0]] = df.iloc[:, result_array[0]:result_array[1]].apply(lambda row: ' || '.join(filter(lambda x: pd.notna(x) and x.strip() != '' and str(x).lower() != 'nan', map(str, row))), axis=1)
df[name_array[2]] = df.iloc[:, result_array[2]:result_array[3]].apply(lambda row: ' || '.join(filter(lambda x: pd.notna(x) and x.strip() != '' and str(x).lower() != 'nan', map(str, row))), axis=1)

# Update the 'language' column based on the 'country' column
country_language_mapping = {
    'FRA': 'fr',
    'DEU': 'de',
    'ITA': 'it',
    'ESP': 'es',
    'GBR': 'en',
    'JPN': 'ja'
}

df['language'] = df['country'].map(country_language_mapping)

product_mapping = {
    1: 'PADCEV',
    2: 'KEYTRUDA',
    3: 'BAVENCIO',
    4: 'TECENTRIQ',
    5: 'OPDIVO',
    6: 'PADCEV + KEYTRUDA',
    7: 'OPDIVO + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY'
}

df['product_name'] = df['Product'].map(product_mapping)


A7_col = 'a7'
a7b_col_prefix = 'a7b'

for j in range(1, 11):  
    a7b_col = f'{a7b_col_prefix}_{j}'
    df.loc[df[A7_col] == str(j), a7b_col] = df[a7b_col_prefix]

#Reorder
columns_in_new_order = ['uniqueid','respid','country','language','product_name',
                        'a4v1a6','a5_other','a7b_1','a7b_2','a7b_3','a7b_4','a7b_5','a7b_6','a7b_7','a7b_8','a7b_9','a7b_10','a10',
                        'e4','e5','e6v1_2','e6v1_3','e6v1_4']

# Reorder the columns
df = df.reindex(columns=columns_in_new_order)

column_mapping = {'uniqueid' : 'uniqueId',
'respid' : 'respid',
'country' : 'country',
'language' : 'language',
'product_name' : 'Product',                  
'a4v1a6' : 'A4 + A6',
'a5_other' : 'A5 other',
'a7b_1' : 'A7B message 1',
'a7b_2' : 'A7B message 2',
'a7b_3' : 'A7B message 3',
'a7b_4' : 'A7B message 4',
'a7b_5' : 'A7B message 5',
'a7b_6' : 'A7B message 6',
'a7b_7' : 'A7B message 7',
'a7b_8' : 'A7B message 8',
'a7b_9' : 'A7B message 9',
'a7b_10' : 'A7B message 10',
'a10' : 'A10',
'e4' : 'E4',
'e5' : 'E5',
'e6v1_2' : 'E6b',
'e6v1_3' : 'E6c',
'e6v1_4' : 'E6d'}

# Renaming the columns
df = df.rename(columns=column_mapping)



 
df.to_excel(output_file, index=False)

   

