from django.shortcuts import render
from .models import Lotto
import pandas as pd
import time
import csv,io
from IPython.display import HTML

def main_view(request):	
	lotto_result = pd.read_csv('Lotto_eng.csv',encoding = "UTF-8")
	pd.set_option('display.width', 1000)
	pd.set_option('colheader_justify', 'center')
	df = pd.DataFrame(pd.DatetimeIndex(lotto_result['date']))
	df['date'] = pd.to_datetime(df.date)
	lotto_result["week_format"] = df['date'].dt.strftime('%d/%m/%Y')
	# lotto_result["week"] = pd.DatetimeIndex(lotto_result['week_format']).week 
	# print((lotto_result[lotto_result['week']==32]))
	df = pd.DataFrame(lotto_result)	
	df = df.reset_index()
	gb = df.groupby(['1','2','3','4','5','6'],as_index=False, sort=False).size()
	gb = (gb.sort_values(['size'], ascending=[False]))
	df_f = df.filter(items=['1','2','3','4','5','6','strong','week_format'])
	df_f = df_f[df_f["strong"] <9]
	gb = gb[gb["size"] >1]
	# gb = gb.drop(['size'], axis=1)
	df3 = pd.merge(df_f, gb)
	# df3 = df3.drop(['size'])
	data_html = df3.to_html(classes=['table table-striped table-hover table-bordered'])	
	context = {'loaded_data': data_html}
	return render(request, "Lotto/main.html", context)	