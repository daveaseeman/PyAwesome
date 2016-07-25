#!/home/vagrant/miniconda3/bin/python

from combine_data import combine_data
import jinja2
import numpy as np


combined_data, temperature_fail, unknown_fail  = combine_data()


total_tests = len(combined_data)

tests_failed = len(temperature_fail) + len(unknown_fail)

test_passed = total_tests - tests_failed

test_fail_temp = len(temperature_fail) 

test_fail_unknown = len(unknown_fail)


test_ran_dates_str = "Tests Summary: Tests ran from: " + combined_data[0][0] + " to " + combined_data[-1][0]

data_in = np.array(combined_data)

date_array = data_in[:,0]
result_array =  data_in[:,1]

failure_cause = []

for data in combined_data:
    if data[0] in temperature_fail:
        failure_cause.append("Temperature Failure")
    elif data[0] in unknown_fail:
        failure_cause.append("Unknown Failure- Please investigate")
    else:
        failure_cause.append("")


env = jinja2.Environment(loader = jinja2.FileSystemLoader("."))

rendered_template = env.get_template("report_template.html").render(test_ran_dates_str = test_ran_dates_str, total_tests = total_tests, \
                                                                    test_passed=test_passed, tests_failed=tests_failed, test_fail_temp=test_fail_temp, \
                                                                    test_fail_unknown = test_fail_unknown, date_array=date_array,  \
                                                                    result_array = result_array, failure_cause = failure_cause
                                                                    )


with open("auto_report.html", "w") as f:
    f.write(rendered_template)
