import sys
import json


values_new_format_data = {}


def handle_values_list(values: list, report_obj):
    for i, val in enumerate(values):
        if type(val) is dict:
            if "value" in report_obj["values"][i].keys():
                if val["id"] in values_new_format_data.keys():
                    report_obj["values"][i]["value"] = values_new_format_data[val["id"]]["value"]

            if "values" in val.keys():
                if type(val["values"]) is list and len(val["values"]) != 0:
                    handle_values_list(val["values"], report_obj["values"][i])

        elif type(val) is list:
            handle_values_list(val, report_obj[i])


values_file_path = sys.argv[1]
tests_file_path = sys.argv[2]
report_file_path = sys.argv[3]

with open(values_file_path, "r", encoding="UTF-8") as values_file:
    values_data = json.load(values_file)

with open(tests_file_path, "r", encoding="UTF-8") as tests_file:
    tests_data = json.load(tests_file)


for value in values_data["values"]:
    values_new_format_data[value["id"]] = value

report_data = tests_data.copy()
val_arr = tests_data["tests"]
deep_val_arr = []

for i, val in enumerate(val_arr):
    if type(val) is dict:
        if val["id"] in values_new_format_data.keys():
            report_data["tests"][i]["value"] = values_new_format_data[val["id"]]["value"]
        if "values" in val.keys():
            if type(val["values"]) is list and len(val["values"]) != 0:
                handle_values_list(val["values"], report_data["tests"][i])
        pass
    elif type(val) is list:
        handle_values_list(val, report_data["tests"][i])

with open(report_file_path, "w", encoding="UTF-8") as report_file:
    report_file.write(json.dumps(report_data, indent=2))
