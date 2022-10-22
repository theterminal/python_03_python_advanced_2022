# 20221010 - Python - Python Advanced - Modules
# Example of usage of pandas

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# load data into a DataFrame object:
result = pd.DataFrame(data)

print(result)
