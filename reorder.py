import pandas as pd
import os

entries = os.listdir('csv_files/')

for x in entries:
	df = pd.read_csv("csv_files/{}".format(x))
	first_date = df.at[0, 'A']
	date = int(first_date.split('/')[0])
	print (date)
	i = 0
	# while df.at[i, 'A'] == "02/03/2020":
	# 	pass