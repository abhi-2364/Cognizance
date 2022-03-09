import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
sentence = ser.str.title()
for i in sentence:
    print(i, end=' ')
