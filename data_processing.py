import pandas as pd

def load_dataset_from_csv(ticker_name):
    df = pd.read_csv("./data/{}.csv".format(ticker_name))
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors='coerce')  # Allow mixed formats
    df.index = df['Date']

    data = df.sort_index(ascending=True, axis=0)
    new_data = pd.DataFrame(index=range(0, len(df)), columns=['Date', 'Close'])

    for i in range(0, len(data)):
        new_data["Date"][i] = data['Date'][i]
        new_data["Close"][i] = data["Close"][i]

    new_data.index = new_data.Date
    new_data.drop("Date", axis=1, inplace=True)
    return new_data.values, new_data
