#!/usr/bin/python3


## ! REPEAT ! Extract later

def extract_data(filename):

    data = []
    with open(filename, "r") as f:
        data = f.read()

    data2 = data.split("\n")

    data_return = []
    for i in range(2,len(data2)):
       data_return.append(data2[i].split(","))

    return data_return


# cpu         = extract_data("cpu.txt")
temperature        = extract_data("temperature.txt")
pass_result = extract_data("pass-fail.txt")

#print(cpu)
#print(temperature)
#print(pass_result)

combined_data = []

for i in range(len(temperature)):
    combined_data.append([temperature[i][0], temperature[i][1], pass_result[i][1]])

print(combined_data[:2])

# pdb.set_trace()

#cpu_fail = []
temperature_fail = []
unknown_fail = []
total_fail = 0

for data in combined_data:
    if data[2] == "FAIL":
        total_fail += 1
        if int(data[1]) >= 35:
            temperature_fail.append(data[0])
        else:
            unknown_fail.append(data[0])

print("temperature fails: ", temperature_fail)
print("unknown_fail: ", unknown_fail)



from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))

doc_test_str = "Test Results for " + combined_data[0][0] + " to " + combined_data[-1][0]

num_tests_run = str(len(combined_data))

num_pass = str(len(combined_data) - total_fail)

num_fail = str(total_fail)

num_fail_temp = str(len(temperature_fail))

num_fail_unknown = str(total_fail - len(temperature_fail))

rendered_template = env.get_template('report.html').render(date_range = doc_test_str, num_tests_run = num_tests_run, num_pass = num_pass, num_fail = num_fail, num_fail_temp = num_fail_temp, \
                                             num_fail_unknown = num_fail_unknown)

with open("auto_report.html", "w") as f:
    f.write(rendered_template)