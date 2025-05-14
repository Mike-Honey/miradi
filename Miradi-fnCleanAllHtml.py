# 'dataset' holds the input data for this script

# Miradi-fnCleanAllHtml.py
# called from Power Query (Power BI) to clean selected columns of HTML codes
# 1. Searches the input dataset's columns for columns named "XXX - HTML"
# 2. Creates a matching column "XXX" and uses BeautifulSoup.get_text() to load it with cleaned text 

import pandas

# test harness for debugging outside Power Query. Delete this section when pasting into Power Query

dataset = pandas.read_csv("C:/Dev/Miradi/miradi-fnCleanHtml-test.csv", sep="\t")

# test harness ends

import warnings
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
warnings.filterwarnings('ignore', category=MarkupResemblesLocatorWarning)

dataset_copy = dataset.copy()
for column in dataset_copy.columns:
    if column.endswith(" - HTML"):
        column_to_clean =  column.replace(" - HTML", "")
        dataset[column_to_clean] = ""
        for i in range(0, len(dataset_copy)):
            try:
                soup = BeautifulSoup(dataset_copy.at[i, column], features="html.parser")
                for br in soup.select('br'):
                    br.replace_with(' ')
                dataset.at[i, column_to_clean] = soup.get_text().strip()
            except:
                dataset.at[i, column_to_clean] = ""

# test harness for debugging outside Power Query. Delete this section when pasting into Power Query

        print(dataset[column_to_clean]) 

# test harness ends
