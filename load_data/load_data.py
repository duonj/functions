import os

import pandas as pd


def load_data(context, data_driver, data_filename):

    # Assume data_driver is going to access data from elsewhere and provide it
    df = pd.read_csv(os.path.join(data_driver, data_filename))

    # Store dataset in context
    context.log_dataset('data', df=df, index=False, format='csv')
