import pandas as pd
import glob

def get_csv(path):
    #getting  list of csv path
    csv_files = [i for i in glob.glob(path + "/*.csv")]
    li=[]
    for i in csv_files:
        df = pd.read_csv(i, index_col=None, header=0)
        li.append(df)
    print('Merging all csv data into one...')
    data = pd.concat(li, axis=0, ignore_index=True)
    return data

def transform_csv(path):
    
    df = get_csv(path)
    print('cleaning and transforming csv data...')
    #filtering the  products
    df = df[df['product'] == "pink morsel"]

    #calculate total sales with multiply quantity and price
    df['sales'] = df['quantity'].astype(int)*df['price'].str[1:].astype(float)

    #dropping the product, quantity, and price columns
    dropped = df.drop(['product', 'quantity', 'price'],axis=1)

    #output
    output = dropped[['sales', 'date', 'region']]
    output.to_csv('output.csv', index=False)
    
    return print(f'Data has been successfully cleaned and saved into {path}!' )