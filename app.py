import ingestCSV

if __name__=="__main__":
    print('Starting the ingestion...')
    formatted_output = ingestCSV.transform_csv('data')

    print('The ingestion finished')