import pandas as pd

#Step 1: Opining excel as df, defining input and output file names and positions columns to be removed 
input_file = "10128_OpenEnd.xlsx"
output_file = input_file.replace('.xlsx', '_Updated.xlsx')

df = pd.read_excel(input_file)
result_array = []
name_array = []
StartCol = 4                        #update this value with start position 
EndCol = len(df.columns) - 1
j = 1

#Step 2: Finding diffrence in column / questions 
for i in range(StartCol, len(df.columns)-1):
    current_col_name = df.columns[i]
    previous_col_name = df.columns[i + 1]
    
    current_col = current_col_name[:4]        #Update 7 here with the number of chara to be kept
    previous_col = previous_col_name[:4]
    #print(str(i) + " " + current_col +" & " + previous_col)        

    if current_col != previous_col and "A4v1" in current_col_name:
        result_array.append(i-9)
        result_array.append(i)
        name_array.append(current_col + "_" + str(j))
        name_array.append(current_col + "_" + str(j))
        j = j + 1

print(result_array)        
print(name_array)

df[name_array[0]] = df.iloc[:, result_array[0]:result_array[1]].apply(lambda row: ' || '.join(filter(lambda x: pd.notna(x) and x.strip() != '' and str(x).lower() != 'nan', map(str, row))), axis=1)
df[name_array[2]] = df.iloc[:, result_array[2]:result_array[3]].apply(lambda row: ' || '.join(filter(lambda x: pd.notna(x) and x.strip() != '' and str(x).lower() != 'nan', map(str, row))), axis=1)
df[name_array[4]] = df.iloc[:, result_array[4]:result_array[5]].apply(lambda row: ' || '.join(filter(lambda x: pd.notna(x) and x.strip() != '' and str(x).lower() != 'nan', map(str, row))), axis=1)
df[name_array[6]] = df.iloc[:, result_array[6]:result_array[7]].apply(lambda row: ' || '.join(filter(lambda x: pd.notna(x) and x.strip() != '' and str(x).lower() != 'nan', map(str, row))), axis=1)
df[name_array[8]] = df.iloc[:, result_array[8]:result_array[9]].apply(lambda row: ' || '.join(filter(lambda x: pd.notna(x) and x.strip() != '' and str(x).lower() != 'nan', map(str, row))), axis=1)
df[name_array[10]] = df.iloc[:, result_array[10]:result_array[11]].apply(lambda row: ' || '.join(filter(lambda x: pd.notna(x) and x.strip() != '' and str(x).lower() != 'nan', map(str, row))), axis=1)
df[name_array[12]] = df.iloc[:, result_array[12]:result_array[13]].apply(lambda row: ' || '.join(filter(lambda x: pd.notna(x) and x.strip() != '' and str(x).lower() != 'nan', map(str, row))), axis=1)

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



# Iterate over A7_1 to A7_7 columns
for i in range(1, 8):  # Assuming A7_1 to A7_7, change as needed
    A7B_col_prefix = f'A7B_{i}'

    for j in range(1, 11):  # Assuming values from 1 to 11, change as needed
            A7B_col = f'{A7B_col_prefix}_{j}'
            df[A7B_col] = ''

# Assign values to the new columns based on the logic
for i in range(1, 8):  # Assuming A7_1 to A7_7, change as needed
    A7_col = f'A7_{i}'
    A7B_col_prefix = f'A7B_{i}'

    for j in range(1, 11):  # Assuming values from 1 to 10, change as needed
        A7B_col = f'{A7B_col_prefix}_{j}'
        df.loc[df[A7_col] == j, A7B_col] = df[A7B_col_prefix]

#Reorder
columns_in_new_order = ['uniqueId','respid','country','language',
                        'A4v1_1','A6_1_1','A6_2_1','A6_3_1','A6_4_1','A6_5_1','A6_6_1','A6_7_1','A6_8_1','A6_9_1','A6_10_1','A7B_1_1','A7B_1_2','A7B_1_3','A7B_1_4','A7B_1_5','A7B_1_6','A7B_1_7','A7B_1_8','A7B_1_9','A7B_1_10','A10_1',
                        'A4v1_2','A6_1_2','A6_2_2','A6_3_2','A6_4_2','A6_5_2','A6_6_2','A6_7_2','A6_8_2','A6_9_2','A6_10_2','A7B_2_1','A7B_2_2','A7B_2_3','A7B_2_4','A7B_2_5','A7B_2_6','A7B_2_7','A7B_2_8','A7B_2_9','A7B_2_10','A10_2',
                        'A4v1_3','A6_1_3','A6_2_3','A6_3_3','A6_4_3','A6_5_3','A6_6_3','A6_7_3','A6_8_3','A6_9_3','A6_10_3','A7B_3_1','A7B_3_2','A7B_3_3','A7B_3_4','A7B_3_5','A7B_3_6','A7B_3_7','A7B_3_8','A7B_3_9','A7B_3_10','A10_3',
                        'A4v1_4','A6_1_4','A6_2_4','A6_3_4','A6_4_4','A6_5_4','A6_6_4','A6_7_4','A6_8_4','A6_9_4','A6_10_4','A7B_4_1','A7B_4_2','A7B_4_3','A7B_4_4','A7B_4_5','A7B_4_6','A7B_4_7','A7B_4_8','A7B_4_9','A7B_4_10','A10_4',
                        'A4v1_5','A6_1_5','A6_2_5','A6_3_5','A6_4_5','A6_5_5','A6_6_5','A6_7_5','A6_8_5','A6_9_5','A6_10_5','A7B_5_1','A7B_5_2','A7B_5_3','A7B_5_4','A7B_5_5','A7B_5_6','A7B_5_7','A7B_5_8','A7B_5_9','A7B_5_10','A10_5',
                        'A4v1_6','A6_1_6','A6_2_6','A6_3_6','A6_4_6','A6_5_6','A6_6_6','A6_7_6','A6_8_6','A6_9_6','A6_10_6','A7B_6_1','A7B_6_2','A7B_6_3','A7B_6_4','A7B_6_5','A7B_6_6','A7B_6_7','A7B_6_8','A7B_6_9','A7B_6_10','A10_6',
                        'A4v1_7','A6_1_7','A6_2_7','A6_3_7','A6_4_7','A6_5_7','A6_6_7','A6_7_7','A6_8_7','A6_9_7','A6_10_7','A7B_7_1','A7B_7_2','A7B_7_3','A7B_7_4','A7B_7_5','A7B_7_6','A7B_7_7','A7B_7_8','A7B_7_9','A7B_7_10','A10_7',
                        'E4_1','E5_1','E6v1_2_1','E6v1_3_1','E6v1_4_1','E6v1_2_2','E6v1_3_2','E6v1_4_2']

# Reorder the columns
df = df.reindex(columns=columns_in_new_order)

column_mapping = {'uniqueId' : 'uniqueId',
'respid' : 'respid',
'country' : 'country',
'language' : 'language',
'A4v1_1' : 'A4 PADCEV (Enfortumab vedotin-ejfv) ',
'A6_1_1' : 'A6 message 1 PADCEV (Enfortumab vedotin-ejfv) ',
'A6_2_1' : 'A6 message 2 PADCEV (Enfortumab vedotin-ejfv) ',
'A6_3_1' : 'A6 message 3 PADCEV (Enfortumab vedotin-ejfv) ',
'A6_4_1' : 'A6 message 4 PADCEV (Enfortumab vedotin-ejfv) ',
'A6_5_1' : 'A6 message 5 PADCEV (Enfortumab vedotin-ejfv) ',
'A6_6_1' : 'A6 message 6 PADCEV (Enfortumab vedotin-ejfv) ',
'A6_7_1' : 'A6 message 7 PADCEV (Enfortumab vedotin-ejfv) ',
'A6_8_1' : 'A6 message 8 PADCEV (Enfortumab vedotin-ejfv) ',
'A6_9_1' : 'A6 message 9 PADCEV (Enfortumab vedotin-ejfv) ',
'A6_10_1' : 'A6 message 10 PADCEV (Enfortumab vedotin-ejfv) ',
'A7B_1_1' : 'A7B message 1 PADCEV (Enfortumab vedotin-ejfv) ',
'A7B_1_2' : 'A7B message 2 PADCEV (Enfortumab vedotin-ejfv) ',
'A7B_1_3' : 'A7B message 3 PADCEV (Enfortumab vedotin-ejfv) ',
'A7B_1_4' : 'A7B message 4 PADCEV (Enfortumab vedotin-ejfv) ',
'A7B_1_5' : 'A7B message 5 PADCEV (Enfortumab vedotin-ejfv) ',
'A7B_1_6' : 'A7B message 6 PADCEV (Enfortumab vedotin-ejfv) ',
'A7B_1_7' : 'A7B message 7 PADCEV (Enfortumab vedotin-ejfv) ',
'A7B_1_8' : 'A7B message 8 PADCEV (Enfortumab vedotin-ejfv) ',
'A7B_1_9' : 'A7B message 9 PADCEV (Enfortumab vedotin-ejfv) ',
'A7B_1_10' : 'A7B message 10 PADCEV (Enfortumab vedotin-ejfv) ',
'A10_1' : 'A10 PADCEV (Enfortumab vedotin-ejfv) ',
'A4v1_2' : 'A4 KEYTRUDA (Pembrolizumab)',
'A6_1_2' : 'A6 message 1 KEYTRUDA (Pembrolizumab)',
'A6_2_2' : 'A6 message 2  KEYTRUDA (Pembrolizumab)',
'A6_3_2' : 'A6 message 3  KEYTRUDA (Pembrolizumab)',
'A6_4_2' : 'A6 message 4  KEYTRUDA (Pembrolizumab)',
'A6_5_2' : 'A6 message 5 KEYTRUDA (Pembrolizumab)',
'A6_6_2' : 'A6 message 6  KEYTRUDA (Pembrolizumab)',
'A6_7_2' : 'A6 message 7  KEYTRUDA (Pembrolizumab)',
'A6_8_2' : 'A6 message 8  KEYTRUDA (Pembrolizumab)',
'A6_9_2' : 'A6 message 9 KEYTRUDA (Pembrolizumab)',
'A6_10_2' : 'A6 message 10  KEYTRUDA (Pembrolizumab)',
'A7B_2_1' : 'A7B message 1 KEYTRUDA (Pembrolizumab)',
'A7B_2_2' : 'A7B message 2 KEYTRUDA (Pembrolizumab)',
'A7B_2_3' : 'A7B message 3 KEYTRUDA (Pembrolizumab)',
'A7B_2_4' : 'A7B message 4 KEYTRUDA (Pembrolizumab)',
'A7B_2_5' : 'A7B message 5 KEYTRUDA (Pembrolizumab)',
'A7B_2_6' : 'A7B message 6 KEYTRUDA (Pembrolizumab)',
'A7B_2_7' : 'A7B message 7 KEYTRUDA (Pembrolizumab)',
'A7B_2_8' : 'A7B message 8f KEYTRUDA (Pembrolizumab)',
'A7B_2_9' : 'A7B message 9f KEYTRUDA (Pembrolizumab)',
'A7B_2_10' : 'A7B message 10 KEYTRUDA (Pembrolizumab)',
'A10_2' : 'A10 KEYTRUDA (Pembrolizumab)',
'A4v1_3' : 'A4 BAVENCIO (avelumab)',
'A6_1_3' : 'A6 message 1 BAVENCIO (avelumab)',
'A6_2_3' : 'A6 message 2  BAVENCIO (avelumab)',
'A6_3_3' : 'A6 message 3  BAVENCIO (avelumab)',
'A6_4_3' : 'A6 message 4  BAVENCIO (avelumab)',
'A6_5_3' : 'A6 message 5 BAVENCIO (avelumab)',
'A6_6_3' : 'A6 message 6  BAVENCIO (avelumab)',
'A6_7_3' : 'A6 message 7  BAVENCIO (avelumab)',
'A6_8_3' : 'A6 message 8  BAVENCIO (avelumab)',
'A6_9_3' : 'A6 message 9 BAVENCIO (avelumab)',
'A6_10_3' : 'A6 message 10  BAVENCIO (avelumab)',
'A7B_3_1' : 'A7B message 1 BAVENCIO (avelumab)',
'A7B_3_2' : 'A7B message 2 BAVENCIO (avelumab)',
'A7B_3_3' : 'A7B message 3 BAVENCIO (avelumab)',
'A7B_3_4' : 'A7B message 4 BAVENCIO (avelumab)',
'A7B_3_5' : 'A7B message 5 BAVENCIO (avelumab)',
'A7B_3_6' : 'A7B message 6 BAVENCIO (avelumab)',
'A7B_3_7' : 'A7B message 7 BAVENCIO (avelumab)',
'A7B_3_8' : 'A7B message 8f BAVENCIO (avelumab)',
'A7B_3_9' : 'A7B message 9f BAVENCIO (avelumab)',
'A7B_3_10' : 'A7B message 10 BAVENCIO (avelumab)',
'A10_3' : 'A10 BAVENCIO (avelumab)',
'A4v1_4' : 'A4 TECENTRIQ (atezolizumab)',
'A6_1_4' : 'A6 message 1 TECENTRIQ (atezolizumab)',
'A6_2_4' : 'A6 message 2  TECENTRIQ (atezolizumab)',
'A6_3_4' : 'A6 message 3  TECENTRIQ (atezolizumab)',
'A6_4_4' : 'A6 message 4  TECENTRIQ (atezolizumab)',
'A6_5_4' : 'A6 message 5 TECENTRIQ (atezolizumab)',
'A6_6_4' : 'A6 message 6  TECENTRIQ (atezolizumab)',
'A6_7_4' : 'A6 message 7  TECENTRIQ (atezolizumab)',
'A6_8_4' : 'A6 message 8  TECENTRIQ (atezolizumab)',
'A6_9_4' : 'A6 message 9 TECENTRIQ (atezolizumab)',
'A6_10_4' : 'A6 message 10  TECENTRIQ (atezolizumab)',
'A7B_4_1' : 'A7B message 1 TECENTRIQ (atezolizumab)',
'A7B_4_2' : 'A7B message 2 TECENTRIQ (atezolizumab)',
'A7B_4_3' : 'A7B message 3 TECENTRIQ (atezolizumab)',
'A7B_4_4' : 'A7B message 4 TECENTRIQ (atezolizumab)',
'A7B_4_5' : 'A7B message 5 TECENTRIQ (atezolizumab)',
'A7B_4_6' : 'A7B message 6 TECENTRIQ (atezolizumab)',
'A7B_4_7' : 'A7B message 7 TECENTRIQ (atezolizumab)',
'A7B_4_8' : 'A7B message 8f TECENTRIQ (atezolizumab)',
'A7B_4_9' : 'A7B message 9f TECENTRIQ (atezolizumab)',
'A7B_4_10' : 'A7B message 10 TECENTRIQ (atezolizumab)',
'A10_4' : 'A10 TECENTRIQ (atezolizumab)',
'A4v1_5' : 'A4 OPDIVO (nivolumab)',
'A6_1_5' : 'A6 message 1 OPDIVO (nivolumab)',
'A6_2_5' : 'A6 message 2  OPDIVO (nivolumab)',
'A6_3_5' : 'A6 message 3  OPDIVO (nivolumab)',
'A6_4_5' : 'A6 message 4  OPDIVO (nivolumab)',
'A6_5_5' : 'A6 message 5 OPDIVO (nivolumab)',
'A6_6_5' : 'A6 message 6  OPDIVO (nivolumab)',
'A6_7_5' : 'A6 message 7  OPDIVO (nivolumab)',
'A6_8_5' : 'A6 message 8  OPDIVO (nivolumab)',
'A6_9_5' : 'A6 message 9 OPDIVO (nivolumab)',
'A6_10_5' : 'A6 message 10  OPDIVO (nivolumab)',
'A7B_5_1' : 'A7B message 1 OPDIVO (nivolumab)',
'A7B_5_2' : 'A7B message 2 OPDIVO (nivolumab)',
'A7B_5_3' : 'A7B message 3 OPDIVO (nivolumab)',
'A7B_5_4' : 'A7B message 4 OPDIVO (nivolumab)',
'A7B_5_5' : 'A7B message 5 OPDIVO (nivolumab)',
'A7B_5_6' : 'A7B message 6 OPDIVO (nivolumab)',
'A7B_5_7' : 'A7B message 7 OPDIVO (nivolumab)',
'A7B_5_8' : 'A7B message 8f OPDIVO (nivolumab)',
'A7B_5_9' : 'A7B message 9f OPDIVO (nivolumab)',
'A7B_5_10' : 'A7B message 10 OPDIVO (nivolumab)',
'A10_5' : 'A10 OPDIVO (nivolumab)',
'A4v1_6' : 'A4 PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A6_1_6' : 'A6 message 1 PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A6_2_6' : 'A6 message 2  PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A6_3_6' : 'A6 message 3  PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A6_4_6' : 'A6 message 4  PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A6_5_6' : 'A6 message 5 PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A6_6_6' : 'A6 message 6  PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A6_7_6' : 'A6 message 7  PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A6_8_6' : 'A6 message 8  PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A6_9_6' : 'A6 message 9 PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A6_10_6' : 'A6 message 10  PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A7B_6_1' : 'A7B message 1 PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A7B_6_2' : 'A7B message 2 PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A7B_6_3' : 'A7B message 3 PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A7B_6_4' : 'A7B message 4 PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A7B_6_5' : 'A7B message 5 PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A7B_6_6' : 'A7B message 6 PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A7B_6_7' : 'A7B message 7 PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A7B_6_8' : 'A7B message 8f PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A7B_6_9' : 'A7B message 9f PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A7B_6_10' : 'A7B message 10 PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A10_6' : 'A10 PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab)',
'A4v1_7' : 'A4 OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A6_1_7' : 'A6 message 1 OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A6_2_7' : 'A6 message 2  OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A6_3_7' : 'A6 message 3  OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A6_4_7' : 'A6 message 4  OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A6_5_7' : 'A6 message 5 OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A6_6_7' : 'A6 message 6  OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A6_7_7' : 'A6 message 7  OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A6_8_7' : 'A6 message 8  OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A6_9_7' : 'A6 message 9 OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A6_10_7' : 'A6 message 10  OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A7B_7_1' : 'A7B message 1 OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A7B_7_2' : 'A7B message 2 OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A7B_7_3' : 'A7B message 3 OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A7B_7_4' : 'A7B message 4 OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A7B_7_5' : 'A7B message 5 OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A7B_7_6' : 'A7B message 6 OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A7B_7_7' : 'A7B message 7 OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A7B_7_8' : 'A7B message 8f OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A7B_7_9' : 'A7B message 9f OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A7B_7_10' : 'A7B message 10 OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'A10_7' : 'A10 OPDIVO (nivolumab) + GEMCITABINE/CISPLATIN-BASED CHEMOTHERAPY',
'E4_1' : 'E4',
'E5_1' : 'E5',
'E6v1_2_1' : 'E6b PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab) ',
'E6v1_3_1' : 'E6c PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab) ',
'E6v1_4_1' : 'E6d PADCEV (enfortumab vedotin-ejfv) + KEYTRUDA (pembrolizumab) ',
'E6v1_2_2' : 'E6b OPDIVO (nivolumab) plus gemcitabine/cisplatin-based chemotherapy ',
'E6v1_3_2' : 'E6c OPDIVO (nivolumab) plus gemcitabine/cisplatin-based chemotherapy ',
'E6v1_4_2' : 'E6d OPDIVO (nivolumab) plus gemcitabine/cisplatin-based chemotherapy '}

# Renaming the columns
df = df.rename(columns=column_mapping)

 
df.to_excel(output_file, index=False)

   

