from pandaslib import SalesHelper

Read_data = SalesHelper()
read_df = Read_data.read_csv()
region_wise_Df = Read_data.region_wise(read_df)
print(region_wise_Df)
# country_wise_Df = Read_data.country_wise(read_df)
# print(country_wise_Df)
