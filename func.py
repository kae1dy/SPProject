import json
from pathlib import Path
from collections import deque


def analysis_data(data_dir="./data/filtered_traces", json_name="gestures.json",
                  screenshots_name="screenshots", hierarchies_name="view_hierarchies", key="children") -> list:
    apps = Path(data_dir)
    traces_len = list()

    counter_apps = len(list(apps.iterdir()))
    counter_traces = 0

    max_depth = 0
    max_app = ""

    for app in apps.iterdir():
        work_dir = Path(app)

        traces = Path(work_dir)

        for trace in traces.iterdir():
            counter_traces += 1
            work_trace = Path(trace)

            with open(Path.joinpath(work_trace, json_name)) as file:
                templates = json.load(file)

            # check length of trace

            trace_len = len(templates)
            screenshots = Path(Path.joinpath(trace, screenshots_name))
            hierarchies = Path(Path.joinpath(trace, hierarchies_name))

            file.close()

            if len(list(screenshots.iterdir())) == len(list(hierarchies.iterdir())) == trace_len:
                traces_len.append(trace_len)
            else:
                print(f"{str(app)} have incorrect dataset.")

            # check depth of every {NumberUI}.json
            for tree in hierarchies.iterdir():
                with open(tree) as file:
                    tree_json = json.load(file)
                try:
                    tmp = max_depth_deq(tree_json["activity"]["root"], key)
                    if max_depth < tmp:
                        max_depth = tmp
                        max_app = str(app)

                except Exception as err:
                    print(f'Error: {err}')
                finally:
                    file.close()
    # output
    print(f"Number of applications in the dataset: {counter_apps}.\n"
          f"Number of traces in the dataset: {counter_traces}.\n\n"
          f"The maximum depth of the UI tree in the dataset: {max_depth}.\n"
          f"The application on which it is achieved: {max_app}.\n")

    return traces_len

# find max_depth UI-tree (recursive)
def max_depth_recursive(tree_json: dict, key: str) -> int:
    if not tree_json:
        return 0
    if key not in tree_json:
        return 1

    max_depth = 0
    for children in tree_json[key]:
        temp = max_depth_recursive(children, key)
        max_depth = max(temp, max_depth)

    return max_depth + 1


# find max_depth UI-tree (with deque)
def max_depth_deq(root: dict, key: str) -> int:
    if not root:
        return 0
    list_nodes = deque([root])
    list_size = 1

    node_level = 1
    levels = 0

    while list_nodes:
        node = list_nodes.popleft()
        list_size -= 1

        if key in node:
            for children in node[key]:

                if children:
                    list_nodes.append(children)
                    list_size += 1

        node_level -= 1
        if node_level == 0:
            levels += 1
            node_level = list_size
    return levels
