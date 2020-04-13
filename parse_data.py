from single_point import parse

MISSING_DATA = "?"
DATA_FEATURES = 15


def parse_line(line):
    features_array = line.split(',')
    return list(map(str.strip, features_array))


def parse_data(data_file_full_path):
    """ This method parses the data into the final matrix [M x N] - called X matrix.
        and Nx1 vector of classifier results - Y vector.
    """
    corrupted_data = False
    f = open(data_file_full_path)
    final_x_matrix = list()
    final_y_vector = list()
    for line in f.readlines():
        if MISSING_DATA not in line:  # skip lines with partial data
            data = parse_line(line)  # removing commas and whitespaces
            if len(data) == DATA_FEATURES:
                    x, y = parse(data)
                    if x != None and y != None:
                        final_x_matrix.append(x)
                        final_y_vector.append(y)
                    else:
                        corrupted_data=True
    return final_x_matrix, final_y_vector,corrupted_data


