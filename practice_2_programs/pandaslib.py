import pandas as pd
from settings import engine


class SalesHelper:
    def read_csv(self):
        filepath = "C:\\Users\\venka\\Downloads\\50000 Sales Records.csv"
        df = pd.read_csv(filepath)
        return df

    def region_wise(self, df):
        regionwise_df = df[df['Region'].str.contains(input('please Enter Region:'))]
        options = input('do you want to save Data-yes/no:')
        save_data = 'yes' or 'Yes' or 'YES'
        read_data = 'no' or 'No' or 'NO'
        if options == save_data:
            print("please provide file name without any'.csv'extension")
            file_name = input('file name:')
            regionwise_df.to_csv(r"E:\\csv\\%s.csv" % file_name)
            print('file saved successfully')
        elif options == read_data:
            options = input("do you want to save data freme in database yes/no:")
            save_to_db = "yes" or "Yes" or "YES"
            read_data = "no" or "No" or "NO"
            if options == save_to_db:
                regionwise_df.to_sql(input("enter table name:"), engine)
            elif options == read_data:
                print("data not saved to DB")
            else:
                print('invalid detailes')
        return regionwise_df

    def country_wise(self, df):
        country = df[df['Country'].str.contains(input('please Enter Country:'))]
        options = input('Do you want to save Data=yes/no:')
        save_date = 'yes' or 'Yes' or 'YES'
        read_data = 'no' or 'No' or 'NO'
        if options == save_date:
            print("please provide file name without any'.csv 'extension")
            file_name = input('file_name')
            country.to_csv(r"E:\\csv\\%s.csv" % file_name)
            print('File saved successfully')
        elif options == read_data:
            options = input("Do you want save data frame in database-yes/no:")
            save_to_db = "yes" or "Yes" or "YES"
            read_data = "no" or "No" or "NO"
            if options == save_to_db:
                country.to_sql(input("enter table name:"), engine)
            elif options == read_data:
                print('data not saved to db')
        else:
            print('invalid detailes')
        return country



