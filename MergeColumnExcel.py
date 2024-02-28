import pandas as pd

#Step 1: Opining excel as df, defining input and output file names and positions columns to be removed 
input_file = "8970_OpenData_OEs.xlsx"
output_file = input_file.replace('.xlsx', '_Updated.xlsx')

df = pd.read_excel(input_file)
result_array = [6]
name_array = []
remov_start = 7                        #update this value with start position 
remov_end = len(df.columns) - 1

#Step 2: Finding diffrence in column / questions 
for i in range(remov_start, len(df.columns)-1):
    current_col_name = df.columns[i]
    previous_col_name = df.columns[i + 1]
    
    if "Q52a_GG" in current_col_name:
        current_col = current_col_name[:7]        #Update 7 here with the number of chara to be kept
        previous_col = previous_col_name[:7]
        print(str(i) + " " + current_col +" & " + previous_col+" GGloop")        
    elif "Q52a" in current_col_name:
        current_col = current_col_name[:8]        #Update 8 here with the number of chara to be kept
        previous_col = previous_col_name[:8]
    else:    
        current_col = current_col_name.split("_")[0]
        previous_col = previous_col_name.split("_")[0]

    if current_col != previous_col:
        result_array.append(i)
        name_array.append(current_col)
         
result_array.append(len(df.columns)-1)
print(result_array)
name_array.append(previous_col)
print(name_array)

#Step 3: Adding the new column and Concatenating 
for i in range(len(result_array)-1):
    start_pos = result_array[i]
    end_pos = result_array[i+1]
    print(str(start_pos) + " " + str(end_pos) + " " + str(df.shape[1]))

    if start_pos < df.shape[1] and end_pos < df.shape[1]:
        new_col_name = name_array[i]
        
        # Concatenating values from columns between start_pos and end_pos
        #df[new_col_name] = df.iloc[:, start_pos+1:end_pos+1].astype(str).agg(' || '.join, axis=1)
        #df[new_col_name] = df.iloc[:, start_pos+1:end_pos+1].apply(lambda row: ' || '.join(filter(lambda x: pd.notna(x) and x != '', row)), axis=1)     #main line
        #df[new_col_name] = df.iloc[:, start_pos+1:end_pos+1].apply(lambda row: ' || '.join(filter(lambda x: pd.notna(x) and x != '', map(str.strip, row))), axis=1)
        df[new_col_name] = df.iloc[:, start_pos+1:end_pos+1].apply(lambda row: ' || '.join(filter(lambda x: pd.notna(x) and x.strip() != '' and str(x).lower() != 'nan', map(str, row))), axis=1)

#Step 4: Removing unwanted OG columns and saving file 
columns_to_delete = list(range(remov_start, remov_end + 1))
df = df.drop(df.columns[columns_to_delete], axis=1)

df.to_excel(output_file, index=False)

   

