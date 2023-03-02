import matplotlib.pyplot as plt
import seaborn as sns

from func import analysis_data

data_dir = "./data/filtered_traces"
json_name = "gestures.json"


if __name__ == '__main__':
    list_traces = analysis_data(data_dir, json_name)

    try:
        # Create a visualization
        sns.histplot(list_traces, color='blue', bins=20, kde=True)
        plt.xlabel('Track length')
        plt.grid()
        plt.savefig('barchart.png')

        plt.show()

    except Exception as err:
        print("Error:", err)
