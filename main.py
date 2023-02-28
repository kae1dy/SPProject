import matplotlib.pyplot as plt

from func import analysis_data, max_trace_data

data_dir = "./data/filtered_traces"
json_name = "gestures.json"

if __name__ == '__main__':

    dict_traces = analysis_data(data_dir, json_name)
    max_trace_data(data_dir, json_name)

    try:
        # Create a visualization
        fig, ax = plt.subplots()
        plt.bar(list(dict_traces.keys()), dict_traces.values(), color='b')
        plt.grid()

        fig.set_figwidth(8)
        fig.set_figheight(8)

        ax.set_xlabel('track length')
        ax.set_ylabel('number of tracks')

        plt.savefig('barchart.png')
        plt.show()

    except Exception as err:
        print("Error:", err)


