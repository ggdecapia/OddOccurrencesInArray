import pandas as pd
# test_one_element_array
A = [9]
df_A = pd.DataFrame(A)
grouped_array = df_A[0].value_counts()
new_index = pd.DataFrame(grouped_array).reset_index()
new_index['mod_value'] = new_index[0] % 2
odd_num = new_index.loc[new_index['mod_value'] == 1, ['index']]
print(odd_num)