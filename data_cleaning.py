
#Filter out groups who have less than the specificed amounts of entries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def remove_small_groupings(df,column,size):
    group_counts = df.groupby(column).size()
    filtered_df = pd.DataFrame
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
def remove_unwanted_columns(df, columns):
    df = df.drop(columns= columns)
    return df

def remove_empty_data(df, columns = None):
    if columns == None:
        df = df.dropna()

    else:
        df = df.dropna(columns=columns)
    return df



### NEEDS TO BE PUT INTO FUNCTIONS
# pd.set_option('display.float_format', lambda x: '%.2f' % x)
# pd.options.mode.chained_assignment = None  # default='warn'
# housing = pd.read_csv("assignments\\midterm\\nashville-housing\\data\\nashville-housing.csv")

# #Filter out Land Use Categories with less than 10 entries
# filtered_landuse = remove_small_groupings(housing,"LandUse",10)


# t_housing = remove_unwanted_columns(filtered_landuse,['OwnerName','OwnerAddress','LegalReference'])
# t_housing = filtered_landuse.dropna(subset=['Acreage', 'TaxDistrict','LandValue','BuildingValue',"SalePrice"])
# t_housing['SalePrice'] = pd.to_numeric(t_housing.loc[:,'SalePrice'],errors='coerce')


# #Create pie chart
# pie_group = t_housing.groupby("LandUse").count()['UniqueID'].head(5)
# pie_group.sort_values(ascending=False)
# pie_group.plot(kind='pie',title="Nashville Land Use Percentages", figsize=(16,9),ylabel=" " )

# #Create New Value Columns
# t_housing['AcreageToCost'] = t_housing['LandValue']/ t_housing["Acreage"]
# t_housing['SaleDifference'] = t_housing['SalePrice'] - t_housing["TotalValue"]

# #Find the averages by Land Use
# average_cost = t_housing.groupby(["LandUse"]).mean().sort_values(by = "SaleDifference", ascending=False)
# average_cost = average_cost.drop("UniqueID", axis=1)
# average_cost = average_cost.fillna(0)

# #Create Histogram breaking down Land Value, Building Value, and Total Value
# average_cost_chart = average_cost[["LandValue","SalePrice","BuildingValue","TotalValue","SaleDifference"]].sort_values(by='TotalValue',ascending=True)
# average_cost_chart = average_cost_chart[average_cost_chart['TotalValue'] != 0]
# fig, ax = plt.subplots(figsize=(15,15))

# # Plotting the Total Value as a line plot
# average_cost_chart['TotalValue'].plot(kind="barh",ax=ax, color='red')
# # Plotting the mean values of Land Value and Building Value as horizontal stacked bars
# average_cost_chart[['LandValue', 'BuildingValue']].plot(kind='barh', stacked=True, ax=ax, color=['green','blue'])
# ax.legend(["Total Value","Land Value", "Building Value"])
# plt.xlabel('Mean Cost')
# plt.ylabel('Land Use')
# plt.title('Mean Cost Breakdown of Land by Land Use')

# #Create boxplot
# th_filtered = dc.filter_outliers(t_housing, 'SalePrice')
# ax =th_filtered.boxplot("SaleDifference", 
#                   by="LandUse", 
#                 figsize=(16,16), 
#                 showfliers = False, 
#                 vert = False, patch_artist=True, 
#                 boxprops = dict(facecolor = "grey"),
#                 medianprops = dict(color = "red", linewidth = 1.5),
#                 whiskerprops = dict(linewidth = 2),
#                 capprops = dict(linewidth = 2))
# ax.ticklabel_format(style='plain', axis='x')
# ax.set_title("Price Ranges Per Land Use Category")
# ax.set_ylabel("Land Use Groups")
# ax.set_xlabel("Sold Price")

