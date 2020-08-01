def parse_data(file_name):
    # open file
    file_in = open(file_name, "r")

    parsed_data = {}

    rms = {}

    for line in file_in:
        if "$" in line:
            # new set (type of result/DOF/node) found
            # save the previous values
            # split vaules
            values = line.split()
            # print(values)

            try:
                parsed_data[set_] =  [freqs, results]
            except:
                pass
            
            # get set type
            set_type = values[0]
            set_type = set_type.replace("$", "")

            # get node
            node = values[2]
            node = "NODE_" + str(node)

            # get the DOF
            DOF = values[3]
            # print(DOF)
            if DOF == "3": DOF = "T1"
            elif DOF == "4": DOF = "T2"
            elif DOF == "5": DOF = "T3"

            print("FOUND " + set_type + " " + node + " " + DOF)

            set_ = set_type + "_" + node + "_" + DOF
            # get rms and __what__ values
            _what_ = values[5]
            
            rms[set_] = values[4]

            # create new arrays
            freqs = []
            results = []

            
        else:
            # not anything new
            # split vaues
            values = line.split()
            # print(values)

            # get frequency and result values
            freq = float(values[1])
            result = float(values[2])
            # print(result)

            # fill the arrays with data
            freqs.append(freq)
            results.append(result)
            # print(freq)
            # print(freqs)

    # close file
    file_in.close()

    return parsed_data



def plot_fig(x, y):
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)

    line_type = "o-"
    line_type = ""
    ax.plot(x, y, line_type)
    # ax.title(set_select + " for " + node_select)
    # ax.xlabel("Frequency [Hz]")
    ax.set_xscale('log')
    # ax.ylabel("RMS")
    ax.set_yscale('log')
    ax.grid()
    plt.show()
    fig.savefig("example.png")



def calculate_rms(x, y):
    import math

    rms = 0

    val_x_ant = 0
    for val_x, val_y in zip(x,y):
        # pass values from str to in
        val_x = val_x
        val_y = val_y

        # calculate area
        aux = (val_x - val_x_ant) * val_y
        
        # save value for next iteration
        val_x_ant = val_x

        # sum the values
        rms += aux
        
    rms = math.sqrt(rms)
    # print(rms)
    return rms



if __name__ == "__main__":
    file_name = "Random_x_new.pch"

    parsed_data = parse_data(file_name)
    # print(parsed_data)

    set_select = "DISP"
    node_select = "NODE_111"
    DOF_select = "T1"
    set_ = set_select + "_" + node_select + "_" + DOF_select

    x = parsed_data[set_][0]
    # print(x)
    y = parsed_data[set_][1]
    # print(y)

    # calculate_rms(x,y)

    plot_fig(x, y)

    # f = open("example.txt", "w")
    # for val_x, val_y in zip(x, y):
    #     text = str(val_x) + "\t" + str(val_y) + "\n"
    #     f.write(text)
    # f.close()