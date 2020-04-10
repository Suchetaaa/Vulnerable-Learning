import pandas as pd
import os

entries = os.listdir('csv_files/')

def Insert_row_(row_number, df, row_value): 
    # Slice the upper half of the dataframe 
    df1 = df[0:row_number] 
   
    # Store the result of lower half of the dataframe 
    df2 = df[row_number:] 
   
    # Inser the row in the upper half dataframe 
    df1.loc[row_number]=row_value 
   
    # Concat the two dataframes 
    df_result = pd.concat([df1, df2]) 
   
    # Reassign the index labels 
    df_result.index = [*range(df_result.shape[0])] 
   
    # Return the updated dataframe 
    return df_result 

for y in entries:
	df = pd.read_csv("csv_files/{}".format(y))
	first_date = df.at[0, 'A']
	first_date = int(first_date.split('/')[0])

	i = 2

	for x in range(i,first_date):
		if (x < 10):
			df = Insert_row_(x-i, df, ["0{}/03/2020".format(x), 0, 0, 0, 0, 0, 0])
		else:
			df = Insert_row_(x-i, df, ["{}/03/2020".format(x), 0, 0, 0, 0, 0, 0])

	print (df)

	df.to_csv("csv_files_normalized/{}".format(y), index=False)

	df_rows = df.shape[0]
	last_date = df.at[df_rows-1, 'A']
	last_date_int = int(last_date.split('/')[0])

	j = 1

	date = first_date

	# while (date != last_date):

	# 	prev_date = df.at[j-1, 'A']
	# 	prev_month = int(prev_date.split('/')[1])
	# 	prev_date = int(prev_date.split('/')[0])


	# 	print (prev_date)
	# 	date = df.at[j, 'A']
	# 	int_month = int(date.split('/')[1])
	# 	int_date = int(date.split('/')[0])
	# 	print (int_date)

	# 	if (int_date != prev_date+1 and int_month == prev_month):
	# 		hfdshflk

	# 	elif (int_date)


	# 	j = j + 1




	
		






	