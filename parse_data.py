from single_point import parse


def parse_data(data_file_full_path):
    """ This method parses the data into the final matrix [M x N] - called X matrix.
        and Nx1 vector of classifier results - Y vector.
    """

    f = open(data_file_full_path)
    final_x_matrix = list()
    final_y_vector = list()

    lines = f.readlines()[1:] #skip header line
    for line in lines:
        if "?" not in line:  #skip lines with patrial data
            x_matrix, y_vector = parse(line.split(', '))
            final_x_matrix.append(x_matrix)
            final_y_vector.append(y_vector)
    return final_x_matrix, final_y_vector


if __name__ == "__main__":
    parse_data('C:\\Velis\\data\\adult2.test')