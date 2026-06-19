import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:

    # Constructor
    def __init__(self, file_path=None):
        self.data = None
        if file_path:
            self.load_data(file_path)

    # Destructor
    def __del__(self):
        print("Object destroyed, cleanup done.")

    # Load Data (Creating)
    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Data loaded successfully")
        except Exception as e:
            print("Error:", e)

    # Data Exploration & Cleaning
    def explore_data(self):
        print("First 5 rows:\n", self.data.head())
        print("Data Info:\n", self.data.info())
        print("Data Description:\n", self.data.describe())

    def clean_data(self):
        self.data.dropna(inplace=True)
        print("Missing values removed")

    # Numpy Operations
    def numpy_operations(self):
        sales_array = self.data[' Revenue '].to_numpy()

        print("First 5 elements:", sales_array[:5])   # slicing
        print("Single element:", sales_array[0])      # indexing

    # Mathematical Operations
    def mathematical_operations(self):
        numeric_cols = self.data.select_dtypes(include=np.number)

        self.data['Sum'] = numeric_cols.sum(axis=1)
        print(self.data.head())

    # Combine & Split Data
    def combine_data(self, other_df):
        combined = pd.concat([self.data, other_df])
        print("Data combined")
        return combined
    
    def split_data(self):
        regions = dict(tuple(self.data.groupby('Region')))
        print("Data split by region")
        return regions
    
    # Search, Sort, Filter
    def search_sort_filter(self):
        # search
        col = input("Column: ")
        val = input("Value: ")
        if col in self.data.columns:
            print(self.data[self.data[col].astype(str).str.contains(val, case=False)])
        # sort
        col = input("Sort column: ")
        if col in self.data.columns:
            print(self.data.sort_values(by=col).head())
        # filter
        num_col = self.data.select_dtypes(include='number').columns[0]
        val = float(input(f"{num_col} > "))
        print(self.data[self.data[num_col] > val])

    # Aggregation
    def aggregate_functions(self):
        numeric_cols = self.data.select_dtypes(include=np.number)

        print("Sum:\n", numeric_cols.sum())
        print("Mean:\n", numeric_cols.mean())
        print("Count:\n", numeric_cols.count())

    # Statistical Analysis
    def statistical_analysis(self):
        numeric_cols = self.data.select_dtypes(include=np.number)

        print("Standard Deviation:\n", numeric_cols.std())
        print("Variance:\n", numeric_cols.var())
        print("Percentiles:\n", numeric_cols.quantile([0.25, 0.5, 0.75]))

    # Pivot Table
    def create_pivot_table(self):
        cols = self.data.columns

        if len(cols) >= 3:
            pivot = pd.pivot_table(self.data,
                                   values=cols[2],
                                   index=cols[0],
                                   columns=cols[1],
                                   aggfunc='sum')
            print(pivot)
        else:
            print("Not enough columns for pivot")

    # Matplotlib Visualization
    def visualize_data(self):
        numeric_cols = self.data.select_dtypes(include='number').columns
        if len(numeric_cols) < 1:
            print("No numeric data")
            return
            
        print("\n1.Bar 2.Line 3.Scatter 4.Pie 5.Histogram 6.Stack Plot")
        choice = int(input("Choose plot: "))

        x = self.data[numeric_cols[0]]
        y = self.data[numeric_cols[1]] if len(numeric_cols) > 1 else None

        plt.figure()

        # BAR
        if choice == 1:
                plt.bar(range(len(x)), x, label="Bar")
                plt.title("Bar Plot")
        # LINE
        elif choice == 2:
            plt.plot(x, label="Line")
            plt.title("Line Plot")
        # SCATTER
        elif choice == 3 and y is not None:
            plt.scatter(x, y, label="Scatter")
            plt.title("Scatter Plot")
        # PIE
        elif choice == 4:
            plt.pie(x.head(5), labels=x.head(5), autopct='%1.1f%%')
            plt.title("Pie Chart")
        # HISTOGRAM
        elif choice == 5:
            plt.hist(x, label="Histogram")
            plt.title("Histogram")
        # STACK PLOT
        elif choice == 6 and y is not None:
            plt.stackplot(range(len(x)), x, y, labels=['X','Y'])
            plt.title("Stack Plot")

        else:
            print("Invalid choice")
            return

        plt.legend()
        plt.show()
    
    # Seaborn Visualization
    def seaborn_plots(self):
    
        numeric_cols = self.data.select_dtypes(include=np.number)
    
        if numeric_cols.shape[1] == 0:
            print("No numeric data")
            return
    
        # Heatmap
        sns.heatmap(numeric_cols.corr(), annot=True)
        plt.title("Heatmap")
        plt.show()
        # Boxplot
        sns.boxplot(data=numeric_cols)
        plt.title("Boxplot")
        plt.show()
            
    # Save Visualization
    def save_plot(self):
                filename = input("Enter file name (with .png or .jpg): ")
                plt.savefig(filename)
                print("Plot saved")

    # Menu Driven Program
    def menu(self):
    
        analyzer = SalesDataAnalyzer()
    
        while True:
            print("\n===== MENU =====")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Clean Data")
            print("4. Numpy Operations")
            print("5. Mathematical Operations")
            print("6. Search/Sort/Filter")
            print("7. Aggregation")
            print("8. Statistical Analysis")
            print("9. Pivot Table")
            print("10. Matplotlib Visualization")
            print("11. Seaborn Visualization")
            print("12. Save Visualization")
            print("0. Exit")
    
            choice = input("Enter choice: ")
    
            if choice == '1':
                file_path = input("Enter CSV file path: ")
                analyzer.load_data(file_path)
    
            elif analyzer.data is None:
                print("Please load dataset first!")
    
            elif choice == '2':
                analyzer.explore_data()
    
            elif choice == '3':
                analyzer.clean_data()
    
            elif choice == '4':
                analyzer.numpy_operations()
    
            elif choice == '5':
                analyzer.mathematical_operations()
    
            elif choice == '6':
                analyzer.search_sort_filter()
    
            elif choice == '7':
                analyzer.aggregate_functions()
    
            elif choice == '8':
                analyzer.statistical_analysis()
    
            elif choice == '9':
                analyzer.create_pivot_table()
    
            elif choice == '10':
                analyzer.visualize_data()
    
            elif choice == '11':
                analyzer.seaborn_plots()

            elif choice == '12':
                analyzer.save_plot()

            elif choice == '0':
                break
    
            else:
                print("Invalid choice")
    
    
# Run Program
if __name__ == "__main__":
    analyzer = SalesDataAnalyzer()
    analyzer.menu()