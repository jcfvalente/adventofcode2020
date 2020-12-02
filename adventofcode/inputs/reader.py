def read_file(file_name: str):
    data = []
    with open(file_name) as file:
        temp_data = file.readlines()
        for line in temp_data:
            striped_line = line.rstrip('\n')
            data.append(striped_line)
    return data