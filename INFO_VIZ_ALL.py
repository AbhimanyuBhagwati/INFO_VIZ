import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from prettytable import PrettyTable

class QUEESTION1:
    def __init__(self):
        self.fil_name = r"/Users/abhimanyubhagwati/Documents/DataVisualization/Info_VIZ_QUIZ/mnist_test.csv"
        self.df = None

    def read_data(self):
        self.df = pd.read_csv(self.fil_name)

    def a(self):
        plt.figure(figsize=(15,8))
        for i in range(100):
            plt.subplot(10,10,i+1)
            plt.imshow(self.df.iloc[i,1:].values.reshape(28,28),cmap='gray')
            plt.title(f"Digit {self.df.iloc[i,0]}")
            plt.axis('off')
        plt.tight_layout()
        plt.show()

    def b(self):
        plt.figure(figsize=(15,8))
        for i in range(100):
            plt.subplot(10,10,i+1)
            plt.imshow(self.df.iloc[i,1:].values.reshape(28,28),cmap='gray')
            plt.title(f"Digit {self.df.iloc[i,0]}")
            plt.axis('off')
        plt.tight_layout()
        plt.show()


DIMOND_DATA_SET_DF = None
class QUESTION2:
    def __init__(self):
        self.df = None

    def read_file(self):
        self.df = sns.load_dataset('diamonds')

    def chk_na_va(self):
        number_f_na = self.df.isna().sum().sum()
        if number_f_na > 0:
            print(f"Number of NA values in the dataset are {number_f_na}")
            self.df.dropna(inplace=True)
        else:
            print("No NA values in the dataset")
        global DIMOND_DATA_SET_DF
        DIMOND_DATA_SET_DF = self.df

class QUESTION3:
    def __init__(self):
        self.df = DIMOND_DATA_SET_DF

    def get_uniq_cuts(self):
        cuts = self.df['cut'].unique()
        print(f"Unique cuts in the dataset are")
        for Number,cut in enumerate(cuts):
            print(f"{Number+1} -  {cut}")

class QUESTION4:
    def __init__(self):
        self.df = DIMOND_DATA_SET_DF

    def get_uniq_colr(self):
        colors = self.df['color'].unique()
        print(f"Unique colors in the dataset are")
        for Number,color in enumerate(colors):
            print(f"{Number+1} -  {color}")
class QUESTION5:
    def __init__(self):
        self.df = DIMOND_DATA_SET_DF

    def get_uniq_clarity(self):
        clarity = self.df['clarity'].unique()
        print(f"Unique clarity in the dataset are")
        for Number,clarity in enumerate(clarity):
            print(f"{Number+1} -  {clarity}")

class QUESTION6:
    def __init__(self):
        self.df = DIMOND_DATA_SET_DF

    def h_bar_plot(self):
        cuts = self.df['cut'].unique()
        cut_sales = self.df.groupby('cut')['price'].sum()
        plt.barh(cuts,cut_sales)
        plt.title("Sales Count for each cut")
        plt.xlabel("Sales")
        plt.ylabel("Cut")
        plt.show()
        max_sales = cut_sales.max()
        max_sales_cut = cut_sales.idxmax()
        print(f"Dimond with {max_sales_cut} cut has max sales")
        min_sales = cut_sales.min()
        min_sales_cut = cut_sales.idxmin()
        print(f"Dimond with {min_sales_cut} cut has min sales")

class QUESTION7:
    def __init__(self):
        self.df = DIMOND_DATA_SET_DF

    def h_bar_plot(self):
        color = self.df['color'].unique()
        color_sales = self.df.groupby('color')['price'].sum()
        plt.barh(color,color_sales)
        plt.title("Sales count per color")
        plt.xlabel("Price")
        plt.ylabel("Color")
        plt.show()
        max_price = self.df['price'].max()
        max_price_color = self.df['color'][self.df['price'] == max_price].values[0]
        print(f"Dimond with {max_price_color} color has max sales")
        min_price = self.df['price'].min()
        min_price_color = self.df['color'][self.df['price'] == min_price].values[0]
        print(f"Dimond with {min_price_color} color has min sales")


class QUESTION8:
    def __init__(self):
        self.df = DIMOND_DATA_SET_DF

    def h_bar_plot(self):
        clarity = self.df['clarity'].unique()
        clarity_sales = self.df.groupby('clarity')['price'].sum()
        plt.barh(clarity,clarity_sales)
        plt.title("Sales count per clarity")
        plt.xlabel("Price")
        plt.ylabel("Clarity")
        plt.show()
        max_price = self.df['price'].max()
        max_price_clarity = self.df['clarity'][self.df['price'] == max_price].values[0]
        print(f"Dimond with {max_price_clarity} clarity has max sales")
        min_price = self.df['price'].min()
        min_price_clarity = self.df['clarity'][self.df['price'] == min_price].values[0]
        print(f"Dimond with {min_price_clarity} clarity has min sales")

class QUESTION9:
    def __init__(self):
        self.df = DIMOND_DATA_SET_DF

    def make_subplot(self):
        plt.figure(figsize=(15,8))
        plt.subplot(1,3,1)
        cuts = self.df['cut'].unique()
        cut_sales = self.df.groupby('cut')['price'].sum()
        plt.barh(cuts, cut_sales)
        plt.title("Sales Count for each cut")
        plt.xlabel("Sales")
        plt.ylabel("Cut")
        plt.subplot(1,3,2)
        color = self.df['color'].unique()
        color_sales = self.df.groupby('color')['price'].sum()
        plt.barh(color, color_sales)
        plt.title("Dimond color vs price")
        plt.xlabel("Price")
        plt.ylabel("Color")
        plt.subplot(1,3,3)
        clarity = self.df['clarity'].unique()
        clarity_sales = self.df.groupby('clarity')['price'].sum()
        plt.barh(clarity, clarity_sales)
        plt.title("Dimond clarity vs price")
        plt.xlabel("Price")
        plt.ylabel("Clarity")
        plt.tight_layout()
        plt.suptitle("Diamond dataset story telling", fontsize=16, y = 1, x = 0.5)
        plt.show()

class QUESTION10:
    def __init__(self):
        self.df = DIMOND_DATA_SET_DF

    def make_piechart_per(self, dim_type):
        plt.figure(figsize=(15,8))
        cuts = self.df[dim_type].unique()
        _explode = tuple([0.03] * len(cuts))
        cut_sales = self.df.groupby(dim_type)['price'].sum()
        plt.pie(cut_sales,labels=cuts,autopct='%1.1f%%', explode=_explode)
        plt.title(f"Sales Count for each {dim_type.upper()}")
        plt.show()
        max_sales = cut_sales.max()
        max_sales_cut = cut_sales.idxmax()
        max_sales_per = (max_sales / cut_sales.sum()) * 100
        print(f"Dimond with {max_sales_cut} {dim_type.upper()} has max sales with {max_sales_per.round(2)}%")
        min_sales = cut_sales.min()
        min_sales_cut = cut_sales.idxmin()
        min_sales_per = (min_sales / cut_sales.sum()) * 100
        print(f"Dimond with {min_sales_cut} {dim_type.upper()} has min sales with {min_sales_per.round(2)}%")

class QUESTION13:
    def __init__(self):
        self.df = DIMOND_DATA_SET_DF

    def get_table(self):
        _df = self.df[self.df['clarity'] == 'VS1']
        _df.drop(['carat', 'clarity', 'table', 'x', 'y', 'z', 'depth'],axis=1,inplace=True)
        _df = _df.groupby(['cut','color'])['price'].mean().unstack()
        _df_ = pd.DataFrame()
        new_max = _df.idxmax(axis=0)
        new_min = _df.idxmin(axis=0)
        _df_['min_price'] = _df.idxmin(axis=1)
        _df_['max_price'] = _df.idxmax(axis=1)
        _df = pd.concat([_df,_df_],axis=1)
        new_max = pd.DataFrame(new_max,columns=['MAX'])
        new_min = pd.DataFrame(new_min,columns=['MIN'])
        new_max = new_max.T
        new_min = new_min.T
        _df = pd.concat([_df,new_max,new_min],axis=0)
        import tabulate
        print(tabulate.tabulate(_df, headers='keys', tablefmt='psql'))












if __name__ == '__main__':
    """
    print("__________________Question 1___________________________")
    q1_obj = QUEESTION1()
    q1_obj.read_data()
    q1_obj.a()
    q1_obj.b()
    """
    print("__________________Question 2___________________________")
    q2_obj = QUESTION2()
    q2_obj.read_file()
    q2_obj.chk_na_va()
    print(q2_obj.df.head())
    print("__________________Question 3___________________________")
    q3_obj = QUESTION3()
    q3_obj.get_uniq_cuts()
    print("__________________Question 4___________________________")
    q4_obj = QUESTION4()
    q4_obj.get_uniq_colr()
    print("__________________Question 5___________________________")
    q5_obj = QUESTION5()
    q5_obj.get_uniq_clarity()
    print("__________________Question 6___________________________")
    q6_obj = QUESTION6()
    q6_obj.h_bar_plot()
    print("__________________Question 7___________________________")
    q7_obj = QUESTION7()
    q7_obj.h_bar_plot()
    print("__________________Question 8___________________________")
    q8_obj = QUESTION8()
    q8_obj.h_bar_plot()
    print("__________________Question 9___________________________")
    q9_obj = QUESTION9()
    q9_obj.make_subplot()
    print("__________________Question 10___________________________")
    q10_obj = QUESTION10()
    q10_obj.make_piechart_per('cut')
    print("__________________Question 11___________________________")
    q10_obj.make_piechart_per('color')
    print("__________________Question 12___________________________")
    q10_obj.make_piechart_per('clarity')
    print("__________________Question 13___________________________")
    q13_obj = QUESTION13()
    q13_obj.get_table()
