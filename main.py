import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt


FILE_INFO = r"https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/CONVENIENT_global_confirmed_cases.csv"
TITANIC_DATA_SET = None

class QUESTION:
    def __init__(self):
        self.df = None

    def read_data(self) -> None:
        self.df = pd.read_csv(FILE_INFO)

    def clean_df(self) -> None:
        self.df.dropna(axis=0, inplace=True)
        global CLN_DATA_SET
        CLN_DATA_SET = self.df


class QUESTION1:
    def __init__(self):
        self.df = CLN_DATA_SET

    def get_cntry(self, cntry) -> None:
        _df = pd.DataFrame()
        cntry_col = [col for col in self.df.columns if cntry in col]
        for col in cntry_col:
            _df[col] = self.df[col].astype(float)
        self.df[cntry + " SUM"] = _df.sum(axis=1)
        print(self.df.sample(5))

class QUESTION2(QUESTION1):
    def __init__(self):
        super().__init__()


class QUESTION3(QUESTION1):
    def __init__(self):
        super().__init__()
        self.df = CLN_DATA_SET


    def plot_data(self, cntry) -> None:
        self.df["TIME"] = pd.to_datetime(self.df["Country/Region"])
        self.df.plot(x="TIME", y=cntry, kind="line", title=cntry + " Confirmed Cases Over Time")
        plt.xlabel("YEAR")
        plt.ylabel("CONFIRMED COVID19 CASES")
        plt.grid()
        plt.show()

    def plot_hist(self, cntry) -> None:
        if 'Sum' in cntry:
            cntry = cntry + " SUM"
        _df = self.df[[cntry]]
        _df["TIME"] = self.df['TIME']
        _df.plot(x="TIME", y=cntry, kind="bar", title=cntry + " Confirmed Cases Over Time")
        plt.xlabel("YEAR")
        plt.xticks(_df["TIME"].unique())
        plt.ylabel("CONFIRMED COVID19 CASES")
        plt.grid()
        plt.show()


class QUESTION4(QUESTION3):
    def __init__(self, cntry_list):
        super().__init__()
        self.df = CLN_DATA_SET
        self.cntry_list = cntry_list

    def get_info(self) -> None:
        for cntry in self.cntry_list:
            self.get_cntry(cntry)
        for ind in enumerate(self.cntry_list):
            self.cntry_list[ind[0]] = ind[1] + " SUM"


    def make_graph(self):
        """
        Make graph of all countries in one graph
        :return:
        plt.bar(self.df["TIME"], self.df[self.cntry_list[-1]], label=self.cntry_list[-1])
        plt.xticks(self.df["TIME"], rotation=90)
        plt.xlabel("YEAR")
        plt.ylabel("CONFIRMED COVID19 CASES")
        plt.title("Confirmed Cases Over Time")
        plt.legend()
        plt.grid()
        plt.show()
        """
        self.df["TIME"] = pd.to_datetime(self.df["Country/Region"]).dt.strftime("%Y-%m")
        _df = pd.DataFrame()
        _df.index = self.df["TIME"]
        _df['US SUM'] = self.df['US SUM']
        sns.lineplot(data=_df, x=_df.index, y='US SUM', label='US SUM')
        plt.xticks(rotation=90)
        plt.xlabel("YEAR")
        plt.ylabel("CONFIRMED COVID19 CASES")
        plt.title("Confirmed Cases Over Time")
        plt.legend()
        plt.grid()
        plt.show()


    def question_5_plot_hist(self):
        self.df["Country/Region"] = pd.to_datetime(self.df["Country/Region"])
        _ = self.df.columns
        sum_clms = [col for col in _ if "SUM" in col]
        fig, ax = plt.subplots(2, 4, figsize=(20, 10))
        for i in range(2):
            for j in range(4):
                ax[i, j].hist(self.df[sum_clms[i+j]], bins=20)
                ax[i, j].set_title(sum_clms[i+j])
                ax[i, j].set_xlabel("Confirmed Cases")
                ax[i, j].set_ylabel("Frequency")
        plt.show()


class QUESTION7:
    def __init__(self):
        self.df = CLN_DATA_SET

    def get_desc_info(self):
        sum_clm = [clms for clms in self.df.columns if "SUM" in clms]
        _df = self.df[sum_clm]
        _df = _df.describe().round(2)
        mean = _df.loc["mean"]
        print(_df.to_string())
        mean = mean.sort_values(ascending=False)
        print("Highest mean --> ", mean.index[0])
        var = _df.loc["std"]
        var = var.sort_values(ascending=False)
        print("Highest variance --> ", var.index[0])
        median = _df.loc["50%"]
        median = median.sort_values(ascending=False)
        print("Highest median --> ", median.index[0])


class Part2:
    def __init__(self):
        self.file_df = sns.load_dataset("titanic")
        global TITANIC_DATA_SET
        TITANIC_DATA_SET = self.file_df


    def question1(self):
        self.file_df.dropna(axis=0, inplace=True)
        print(self.file_df.head())
        print("Percentage of data imputed --> ", (self.file_df.isnull().sum().sum() / self.file_df.size) * 100)

    def question2(self):
        value_count = self.file_df['sex'].value_counts()
        plt.figure(figsize=(6, 6))
        sns.set_style("whitegrid")
        plt.pie(value_count, labels=value_count.index, autopct=lambda x: f'{int(x * sum(value_count)/100)}', startangle=90)
        plt.legend()
        plt.title('Pie Chart of total people in Titanic')
        plt.axis('equal')
        plt.show()


    def question3(self):
        value_count = self.file_df['sex'].value_counts()
        plt.figure(figsize=(6, 6))
        sns.set_style("whitegrid")
        plt.pie(value_count, labels=value_count.index, autopct='%1.1f%%', startangle=90)
        plt.legend()
        plt.title('Pie Chart of total people in Titanic')
        plt.axis('equal')
        plt.show()

    def question4(self, sex: str):
        plt.figure(figsize=(12, 12))
        _df = self.file_df[self.file_df['sex'] == sex]
        value_count = _df['survived'].value_counts()
        plt.figure(figsize=(6, 6))
        sns.set_style("whitegrid")
        if sex == 'female':
            value_count.index = [f'{sex} Survived', f' {sex} Not Survived']
        else:
            value_count.index = [f' {sex} Not Survived', f'{sex} Survived']
        plt.pie(value_count, labels=value_count.index, autopct='%1.1f%%', startangle=90)
        plt.legend(loc='upper right')
        plt.title(f'Pie Chart of {sex.upper()} Survival in Titanic')
        plt.axis('equal')
        plt.show()

    def question6(self):
        value_count = self.file_df['class'].value_counts()
        plt.figure(figsize=(6, 6))
        sns.set_style("whitegrid")
        value_count.index= ['ticket class 3', 'ticket class 2', 'ticket class 1']
        plt.pie(value_count, labels=value_count.index, autopct='%1.1f%%', startangle=90, explode=[0.1, 0, 0])
        plt.legend()
        plt.title('Pie Chart of total people in Titanic')
        plt.axis('equal')
        plt.show()

    def question7(self):
        plt.figure(figsize=(12, 12))
        sns.set_style("whitegrid")
        _df = self.file_df.groupby('class')['survived'].sum()
        _df.index = ['ticket class 1', 'ticket class 2', 'ticket class 3']
        plt.pie(_df, labels=_df.index, autopct='%1.1f%%', startangle=90, explode=[0.1, 0, 0])
        plt.legend()
        plt.title('Pie Chart of Survival Rate based on Ticket Class')
        plt.axis('equal')
        plt.show()

    def question8(self, class_type: str):
        _df = self.file_df[self.file_df['class'] == class_type]
        value_count = _df['survived'].value_counts()
        plt.figure(figsize=(6, 6))
        sns.set_style("whitegrid")
        value_count.index = ['Survival Rate', 'Death Rate']
        plt.pie(value_count, labels=value_count.index, autopct='%1.1f%%', startangle=90)
        plt.legend()
        plt.title(F'Survival & Death Rate : {class_type}')
        plt.axis('equal')
        plt.show()

class QUESTION11:
    def __init__(self):
        self.file_df = TITANIC_DATA_SET

    def question2(self, ax):
        value_count = self.file_df['sex'].value_counts()
        ax.pie(value_count, labels=value_count.index, autopct=lambda x: f'{int(x * sum(value_count) / 100)}',
               startangle=90)
        ax.legend()
        ax.set_title('Pie Chart of total people in Titanic')
        ax.axis('equal')


    def question3(self, ax):
        value_count = self.file_df['sex'].value_counts()
        ax.pie(value_count, labels=value_count.index, autopct='%1.1f%%', startangle=90)
        ax.legend()
        ax.set_title('Pie Chart of total people in Titanic')
        ax.axis('equal')

    def question4(self, ax, sex: str):
        _df = self.file_df[self.file_df['sex'] == sex]
        value_count = _df['survived'].value_counts()
        if sex == 'female':
            value_count.index = [f'{sex} Survived', f' {sex} Not Survived']
        else:
            value_count.index = [f' {sex} Not Survived', f'{sex} Survived']
        ax.pie(value_count, labels=value_count.index, autopct='%1.1f%%', startangle=90)
        ax.legend(loc='upper right')
        ax.set_title(f'Pie Chart of {sex.upper()} Survival in Titanic')
        ax.axis('equal')

    def question6(self, ax):
        value_count = self.file_df['class'].value_counts()
        value_count.index = ['ticket class 1', 'ticket class 2', 'ticket class 3']
        ax.pie(value_count, labels=value_count.index, autopct='%1.1f%%', startangle=90, explode=[0.1, 0, 0])
        ax.legend()
        ax.set_title('Pie Chart of total people in Titanic')
        ax.axis('equal')

    def question7(self, ax):
        _df = self.file_df.groupby('class')['survived'].sum()
        _df.index = ['ticket class 1', 'ticket class 2', 'ticket class 3']
        ax.pie(_df, labels=_df.index, autopct='%1.1f%%', startangle=90, explode=[0.1, 0, 0])
        ax.legend()
        ax.set_title('Pie Chart of Survival Rate based on Ticket Class')
        ax.axis('equal')

    def question8(self, ax, class_type: str):
        _df = self.file_df[self.file_df['class'] == class_type]
        value_count = _df['survived'].value_counts()
        value_count.index = ['Survival Rate', 'Death Rate']
        ax.pie(value_count, labels=value_count.index, autopct='%1.1f%%', startangle=90)
        ax.legend()
        ax.set_title(F'Survival & Death Rate : {class_type}')
        ax.axis('equal')

    def make_pie_sub_graph(self):
        fx, axes = plt.subplots(3, 3, figsize=(16, 18))
        self.question2(axes[0, 0])
        self.question3(axes[0, 1])
        self.question4(axes[0, 2], 'male')
        self.question4(axes[1,0], 'female')
        self.question6(axes[1, 1])
        self.question7(axes[1, 2])
        self.question8(axes[2, 0], 'First')
        self.question8(axes[2, 1], 'Second')
        self.question8(axes[2, 2], 'Third')
        plt.show()

if __name__ == "__main__":
    q_obj = QUESTION()
    q_obj.read_data()
    q_obj.clean_df()
    print("*"*10+"QUESTION1"+"*"*10)
    q1_obj = QUESTION1()
    q1_obj.get_cntry("China")
    print("*"*10+"QUESTION2"+"*"*10)
    q2_obj = QUESTION2()
    q2_obj.get_cntry("United Kingdom")
    print("*"*10+"QUESTION3"+"*"*10)
    q3_obj = QUESTION3()
    q2_obj.get_cntry("US")
    q3_obj.plot_data("US")
    q3_obj.plot_hist("US")
    print("*"*10+"QUESTION4"+"*"*10)
    q4_obj = QUESTION4(["United Kingdom", "China", "Germany", "Brazil", "India", "Italy", 'US'])
    q4_obj.get_info()
    q4_obj.make_graph()
    print("*"*10+"QUESTION5"+"*"*10)
    q4_obj.question_5_plot_hist()
    print("*"*10+"QUESTION6"+"*"*10)
    #exit()
    ###
    # Question 6
    ###
    print("*"*10+"QUESTION7"+"*"*10)
    q7_obj = QUESTION7()
    q7_obj.get_desc_info()
    print("*"*10+"PART 2"+"*"*10)
    print("*"*10+"QUESTION1"+"*"*10)
    q8_obj = Part2()
    q8_obj.question1()
    print("*"*10+"QUESTION2"+"*"*10)
    q8_obj.question2()
    print("*"*10+"QUESTION3"+"*"*10)
    q8_obj.question3()
    print("*"*10+"QUESTION4"+"*"*10)
    q8_obj.question4('male')
    print("*"*10+"QUESTION5"+"*"*10)
    q8_obj.question4('female')
    print("*"*10+"QUESTION6"+"*"*10)
    q8_obj.question6()
    print("*"*10+"QUESTION7"+"*"*10)
    q8_obj.question7()
    print("*"*10+"QUESTION8"+"*"*10)
    q8_obj.question8('First')
    print("*"*10+"QUESTION9"+"*"*10)
    q8_obj.question8('Second')
    print("*"*10+"QUESTION10"+"*"*10)
    q8_obj.question8('Third')
    print("*"*10+"QUESTION11"+"*"*10)
    q11_obj = QUESTION11()
    q11_obj.make_pie_sub_graph()