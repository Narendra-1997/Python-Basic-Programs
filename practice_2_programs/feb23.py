import pandas as pd

#
# df = pd.read_csv("E:\\csv\\50000 Sales Records.csv")
#
# d = pd.DataFrame(df)
# print(d)
#
# d1={"name":['narendra','surendra','mani','jessi'],'marks':
#     [90,90,45,76],'total':[400,600,470,370]}
# d2=pd.DataFrame(d1)
# print(d2)
#
# d1=[(1,2,'narendra',4),(12,56,'hi',7),(12,8,'jessi',6)]
# print(d1)
# d2=pd.DataFrame(d1)
# print(d2)


# df = pd.read_csv("E:\\csv\\50000 Sales Records.csv")
#
# d = pd.DataFrame(df)
#
# print(df.head())
#
# print(df.tail())
filepath = "E:\\csv\\StudentsPerformance.csv"
df = pd.read_csv(filepath)
# print(df)

# print(df[2:5])
# print(df.describe())
# print(df.shape)
# print(df[0:90])
# print(df['reading score'])
# print(df[['reading score','writing score']])
# print(df[['reading score', 'writing score']][1:10])

# for rec in df.iterrows():
#     print(rec)
#

# print(df.loc[4,['parental level of education']])
# print(df.loc[1:9,'writing score'])
# print(df.loc[1:9,])
# print(df.loc[7])
print(df.loc[0:3,'lunch':'math score'])