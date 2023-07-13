import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None  # default='warn'



def load_data(file_path):
    # Loads the dataset from file path
    df = pd.read_csv(file_path)
    return df


def remove_small_groupings(df,column,size):
    # Filters out groups based on the specified number of entries
    group_counts = df.groupby(column).size()
    filtered_df = pd.DataFrame
    filtered_df = group_counts[group_counts < size].index
    filtered_df = df.groupby(column).filter(lambda x: x[column].count() >= size)
    return filtered_df


def filter_outliers(df,column,std_threshold = 3):
    # Filter outliers using the mean, std, and the threshold to filter out the data
    mean = df[column].mean()
    std = df[column].std()
    std_threshold = 3
    df_filtered = df[(np.abs(df[column] - mean) <= std_threshold * std)]
    return df_filtered


def remove_unwanted_columns(df, columns):
    # Removes unwanted columns from the dataframe
    df = df.drop(columns= columns)
    return df

def remove_empty_data(df, columns = None):
    # Removes empty entries from specified column or all columns if columns left as None
    if columns == None:
        df = df.dropna()

    else:
        df = df.dropna(columns=columns)
    return df

def create_boxplot(df,data,grouping,title,y_ax,x_ax):
    ax = df.boxplot(data, by=grouping, figsize=(16, 16), showfliers=False, vert=False,
                    patch_artist=True, boxprops=dict(facecolor="grey"),
                    medianprops=dict(color="red", linewidth=1.5),
                    whiskerprops=dict(linewidth=2),
                    capprops=dict(linewidth=2))
    plt.suptitle("")
    ax.set_title(title)
    ax.set_ylabel(y_ax)
    ax.set_xlabel(x_ax)
    return ax

if __name__ == "__main__":
    # housing = load_data('data/nashville-housing.csv')
    # # Create the df and filter out unused data
    # filtered_landuse = remove_small_groupings(housing,"LandUse",10)
    # filtered_landuse['LandUse'] = filtered_landuse['LandUse'].replace('VACANT RES LAND', 'VACANT RESIDENTIAL LAND')
    # t_housing = remove_unwanted_columns(filtered_landuse,['OwnerName','OwnerAddress','LegalReference','UniqueID'])
    # t_housing = filtered_landuse.dropna(subset=['Acreage', 'TaxDistrict','LandValue','BuildingValue',"SalePrice",])
    # t_housing['SalePrice'] = pd.to_numeric(t_housing.loc[:,'SalePrice'],errors='coerce')
    # t_housing['AcreageToCost'] = t_housing['LandValue']/ t_housing["Acreage"]
    # t_housing['SaleDifference'] = t_housing['SalePrice'] - t_housing["TotalValue"]

    # # Create pie chart
    # pie_group = t_housing['LandUse'].value_counts().head(5)
    # pie_group.plot(kind='pie',title="Nashville Land Use Percentages", figsize=(20,9),ylabel=" ",  labels=pie_group.index, autopct ="%1.1f%%" )

    # # Create Total Properties per District Bar Chart
    # tax_district= t_housing.groupby('TaxDistrict')["LandUse"].size()
    # ax = tax_district.plot.barh(title="Total Properties Per Tax District", ylabel="")
    # ax.ticklabel_format(style='plain', axis='x')
    # for i, count in enumerate(tax_district):
    #     ax.annotate(str(count), xy=(count, i), va='center')

    # # Create Bar Chart for properties types per district
    # tax_district= t_housing.groupby(["LandUse",'TaxDistrict']).size().sort_values(ascending=False).head(10)
    # tax_district= tax_district.sort_values(ascending=True)
    # ax = tax_district.plot.barh(title="Total Properties Per Tax District", ylabel="",figsize=(16,16))
    # ax.ticklabel_format(style='plain', axis='x')
    # for i, count in enumerate(tax_district):
    #     ax.annotate(str(count), xy=(count, i), va='center')

    # #Create Histogram of Total Cost
    # tax_district= t_housing.groupby(["TaxDistrict","LandUse"])["SalePrice"].mean().to_frame()
    # tax_district=tax_district.sort_values(by=["TaxDistrict","SalePrice"], ascending=False)
    # fig, ax = plt.subplots(figsize=(15,15))
    # tax_district= filter_outliers(tax_district, 'SalePrice')
    # tax_district.plot(kind='barh', stacked=True,ax=ax)
    # ax.ticklabel_format(style='plain', axis='x')
    # ax.set_title("Price Averages Per Land Use Category")
    # ax.set_ylabel("Land Use Groups")
    # ax.set_xlabel("Sale Price")

    # # Create Boxchart
    # average_cost = t_housing.groupby(["LandUse"]).mean().sort_values(by = "SaleDifference", ascending=False)
    # average_cost = average_cost.fillna(0)
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
    # plt.title('Mean Cost Breakdown of Land by Categories')

    # th_filtered = filter_outliers(t_housing, 'SaleDifference')
    # ax = create_boxplot(th_filtered,"SaleDifference","LandUse","Price Difference Ranges Per Land Use Category","Land Use Groups","Sale Price")




