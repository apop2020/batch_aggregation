import pandas as pd
import numpy as np
from datetime import datetime, timedelta

rows_to_insert=1000000

if __name__=="__main__":
    data={} 
    data['Value']= np.random.randn(rows_to_insert)
    data['Metric']=  np.random.choice(['foo','bar','baz','temperature','hocus pocus'],rows_to_insert)
    df = pd.DataFrame(data)
    df['TimeStamp']= df.apply(lambda row: datetime.now()-timedelta(minutes=np.random.randint(low=0,high=5000)),axis=1)
    df.to_parquet('data/in/batch1.parquet')
