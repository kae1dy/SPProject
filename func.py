import json
import os


def analysis_data(data_dir="./data/filtered_traces", json_name="gestures.json"):
    apps = os.listdir(data_dir)

    counter_apps = len(apps)
    counter_traces = 0
    dict_traces = {}

    for app in apps:
        work_dir = os.path.join(data_dir, app)

        if os.path.isdir(work_dir):
            traces = os.listdir(work_dir)

            for trace in traces:
                counter_traces += 1
                work_trace = os.path.join(work_dir, trace)
                try:
                    with open(os.path.join(work_trace, json_name)) as file:
                        templates = json.load(file)

                    trace_len = len(templates)
                    if trace_len in dict_traces.keys():
                        dict_traces[trace_len] += 1
                    else:
                        dict_traces[trace_len] = 1

                except FileNotFoundError as err:
                    print("Error: ", err)

    print(f"Number of applications in the dataset: {counter_apps}.\n"
          f"Number of traces in the dataset: {counter_traces}.\n")
    return dict_traces


def max_trace_data(data_dir='./data/filtered_traces', json_name="gestures.json"):

    apps = os.listdir(data_dir)

    max_len_trace = 0
    max_app = ""

    for app in apps:
        work_dir = os.path.join(data_dir, app)
        if os.path.isdir(work_dir):
            traces = os.listdir(work_dir)

            for trace in traces:
                work_trace = os.path.join(work_dir, trace)
                try:
                    with open(os.path.join(work_trace, json_name)) as file:
                        templates = json.load(file)

                    trace_len = len(templates)

                    if trace_len > max_len_trace:
                        max_len_trace = trace_len
                        max_app = app

                except FileNotFoundError as err:
                    print("Error: ", err)

    if max_len_trace != 0:
        print(f"The maximum depth of the UI tree in the dataset: {max_len_trace}.\n"
              f"The application on which it is achieved: {max_app}.\n")



