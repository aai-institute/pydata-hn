import pandas as pd
import lakefs_spec

fs = lakefs_spec.LakeFSFileSystem()

df = pd.read_csv("developer-stats.csv")
df.to_csv("lakefs://pydata-hb/main/developer-stats.csv")