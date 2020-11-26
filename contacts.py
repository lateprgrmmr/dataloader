import usaddress as us
import pandas as pd

p = pd.DataFrame(us.parse('1402 West Sandalwood Dr. Meridian, ID 83646'))
print(p)