#!/home/vagrant/miniconda3/bin/python

def read_data(file_f):
    with open(file_f, "r") as f:
        data = f.read()
        data = data.split("\n")

        data2 = []
        for d in data:
            data2.append(d.split(","))

    return data2

def combine_data():

    data_pass = read_data("pass-fail.txt")

    data_temp = read_data("temperature.txt")

    combined_data = []

    for i in range(2, len(data_pass)):

        combined_data.append([data_pass[i][0], data_pass[i][1], data_temp[i][1]])

    
    temperature_fail = []
    unknown_fail = []

    for data in combined_data:
        if data[1] == "FAIL":
            if int(data[2]) >= 35:
                temperature_fail.append(data[0])
            else:
                unknown_fail.append(data[0])


    return combined_data, temperature_fail, unknown_fail


if __name__ == '__main__':

    combined_data, temperature_fail, unknown_fail  = combine_data()

    print(combined_data[:2])
    print(temperature_fail)
    print(unknown_fail)

