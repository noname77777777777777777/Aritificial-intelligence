def get_data(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix

