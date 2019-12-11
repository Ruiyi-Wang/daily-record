import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
def testpd():
	df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")
	#df_rank = df.grouby(['rank'])
	#print(df_rank.mean())
	'''
	df_sub = df[ df['salary'] > 120000 ]
	print(df_sub)
	df_f = df[df['sex'] == 'female']
	print(df_f)
	'''
	#ax = df.plot.bar(x=)
	#print(df)
	#print(df.head())
	#print(df.dtypes)
	#print(df.columns)
	#print(df.ndim)
	#print(df.size)
	#print(df.shape)
	'''
	print(df.describe())   #描述性统计
	print(df['service'].std())
	print(df[['service','salary']].std())
	print(df.head(50)['salary'].mean())
	'''
def testtime():
	
	idx = pd.date_range('2018-01-01', periods=5, freq='H')
	print(idx)
	ts = pd.Series(range(len(idx)), index=idx)
	print(ts)
	ts.plot()
	plt.show()
	
	s = pd.Series([1,3,5,np.nan,6,8])
	print(s)
	dates = pd.date_range('20130101', periods=6)
	print(dates)
	df = pd.DataFrame(np.random.randn(6,4),index=dates, columns=list('ABCD'))
	print(df)



def main():
	testpd()
	testtime()

if __name__ == '__main__':
	main()
