import pandas as pd
dis ={"a":[1,2,3,4,5,6],"s":[1,2,3,4,5,6],"d":[1,2,3,4,5,6]}
d=pd.DataFrame(dis)
print(d)
d.to_csv("Test_new.csv")