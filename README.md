# Parsing a CSV file in Python

Use the built-in [Python CSV module](https://docs.python.org/3/library/csv.html "Read Docs")

``` python
import csv
```

Using the **csv.DictReader** class will read the CSV file and parse it into a list of dictionaries

Each row of the CSV file will be represented as a dictionary with the column headers as keys and the values as values

``` python
csv.DictReader()
```

To get the output as an array of comma-separated dictionaries in a JSON-like format, use the json module to dump the list of dictionaries to a JSON string

``` python
import json
```

The result will be a JSON array of comma-separated dictionaries, where each dictionary represents a row in the CSV file

Run **python app.py** in the terminal to view the output

``` python
python app.py

[
  {
    "Date": "2021-05-15",
    "ID": "43",
    "Make": "Gudereit",
    "Model": "EC-5",
    "Price": "899",
    "UserID": "434"
  },
  {
    "Date": "2021-05-03",
    "ID": "44",
    "Make": "Diamant",
    "Model": "Beryll",
    "Price": "2100",
    "UserID": "512"
  },
  {
    "Date": "2021-07-15",
    "ID": "46",
    "Make": "Diamant",
    "Model": "Juna",
    "Price": "1100",
    "UserID": "432"
  },
  {
    "Date": "2021-07-13",
    "ID": "51",
    "Make": "Gudereit",
    "Model": "EC-5",
    "Price": "700",
    "UserID": "534"
  },
  {
    "Date": "2021-06-20",
    "ID": "56",
    "Make": "Gudereit",
    "Model": "ET-9 evo",
    "Price": "1600",
    "UserID": "431"
  },
  {
    "Date": "2021-07-01",
    "ID": "61",
    "Make": "Diamant",
    "Model": "BERYLL",
    "Price": "900",
    "UserID": "412"
  },
  {
    "Date": "2021-06-28",
    "ID": "66",
    "Make": "AwesomeBikes",
    "Model": "Dirt Drifter3000",
    "Price": "1900",
    "UserID": "399"
  },
  {
    "Date": "2021-07-04",
    "ID": "67",
    "Make": "Kettler",
    "Model": "Velossi",
    "Price": "1800",
    "UserID": "532"
  },
  {
    "Date": "2021-07-03",
    "ID": "78",
    "Make": "Gudereit",
    "Model": "ec-5",
    "Price": "1200",
    "UserID": "416"
  },
  {
    "Date": "2021-04-11",
    "ID": "81",
    "Make": "Gudereit",
    "Model": "EC 5",
    "Price": "850",
    "UserID": "498"
  },
  {
    "Date": "2021-05-20",
    "ID": "97",
    "Make": "AwesomeBikes",
    "Model": "Dirt-Drifter-3000",
    "Price": "1600",
    "UserID": "387"
  },
  {
    "Date": "2021-07-15",
    "ID": "121",
    "Make": "Gudereit",
    "Model": "ET 9 evo",
    "Price": "1900",
    "UserID": "434"
  },
  {
    "Date": "2021-06-27",
    "ID": "178",
    "Make": "Diamant",
    "Model": "beryll",
    "Price": "2600",
    "UserID": "488"
  },
  {
    "Date": "2021-07-17",
    "ID": "190",
    "Make": "Diamant",
    "Price": "999",
    "UserID": "420"
  }
]
```



