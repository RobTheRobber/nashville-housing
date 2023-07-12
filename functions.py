
#Filter out groups who have less than the specificed amounts of entries
import numpy as np

def remove_small_groupings(df,column,size):
    group_counts = df.groupby(column).size()
    filtered_df = group_counts[group_counts < size].index
    filtered_df = df.groupby(column).filter(lambda x: x[column].count() >= size)
    return filtered_df

#Filter outliers using the mean, std, and the threshold to filter out the data
def filter_outliers(df,column,std_threshold = 3):
    mean = df[column].mean()
    std = df[column].std()
    std_threshold = 3
    df_filtered = df[(np.abs(df[column] - mean) <= std_threshold * std)]
    return df_filtered