import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json


with open('mvswantedbezvesti_1.json', encoding='utf-8-sig') as f:
        data = json.load(f)
df = pd.DataFrame(data)

df_women = df[df['SEX'] == 'ЖІНОЧА']
df_men = df[df['SEX'] == 'ЧОЛОВІЧА']
df_men = df_men.drop(['ARTICLE_CRIM','BIRTH_DATE','CATEGORY','CONTACT','FIRST_NAME_E'
                      ,'FIRST_NAME_R','FIRST_NAME_U','LAST_NAME_E','LAST_NAME_R',
                     'LAST_NAME_U','LOST_PLACE','MIDDLE_NAME_E','MIDDLE_NAME_R',
                     'MIDDLE_NAME_U','OVD','PHOTOID','RESTRAINT'],axis=1)
df_women = df_women.drop(['ARTICLE_CRIM','BIRTH_DATE','CATEGORY','CONTACT','FIRST_NAME_E'
                      ,'FIRST_NAME_R','FIRST_NAME_U','LAST_NAME_E','LAST_NAME_R',
                     'LAST_NAME_U','LOST_PLACE','MIDDLE_NAME_E','MIDDLE_NAME_R',
                     'MIDDLE_NAME_U','OVD','PHOTOID','RESTRAINT'],axis=1)
df_men['LOST_DATE'] = df_men['LOST_DATE'].str[:4]
df_women['LOST_DATE'] = df_women['LOST_DATE'].str[:4]
df_men = df_men[(df_men['LOST_DATE'] >= '2002') & (df_men['LOST_DATE'] < '2020')]
df_women = df_women[(df_women['LOST_DATE'] >= '2002') & (df_women['LOST_DATE'] < '2020')]
df_women = df_women.groupby('LOST_DATE').count()['SEX']
df_women = df_women.to_frame()
df_men = df_men.groupby('LOST_DATE').count()['SEX']
df_men = df_men.to_frame()
df_men = df_men.rename(columns={'SEX':'MEN'})
df_women = df_women.rename(columns={'SEX':'WOMEN'})


plt.figure(figsize=(10,6))
plt.plot(df_men,c='blue',label='Men')
plt.plot(df_women,c='red',label='Women')
x_ticks = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
       2011, 2012, 2013,2014, 2015, 2016, 2017, 2018, 2019]
plt.xticks(x_ticks)
plt.title('Missing person per year in 2002-2019')
plt.legend(loc = 0, fontsize=12, frameon = False)
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='on', labelbottom='on')
plt.show()
