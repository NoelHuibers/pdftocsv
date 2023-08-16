file_name = "people.txt"
counter = 0
lines_dict = {}  # Initialize the dictionary

def secondFunction(line):
    global lines_dict
    global counter
    
    if line.strip() == "":
        return
    
    values = line.strip().split(',')
    if values[0].isdigit() and len(values[0]) != 4 or (counter >= 99 and values[0][:3].isdigit() and values[0][3] == ' ') or values[0][:3] == '43 ':
        counter += 1
        if counter not in lines_dict:
            lines_dict[counter] = []  # Initialize with an empty list
        new_values = []
        if counter >= 100:
            new_values.append(values[0][:3])
            new_values.append(values[0][4:])
        else:
            new_values.append(values[0][:2])
        for i in range(len(values)):
            if i == 0:
                continue
            new_values.append(values[i])
        values = new_values
        # Extend the existing list with new values
        lines_dict[counter].extend(values)
    else:
        if counter not in lines_dict:
            lines_dict[counter] = []  # Initialize with an empty list
        # Extend the existing list with new values
        lines_dict[counter].extend(values)


with open(file_name, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith('_') or (line.strip().isdigit() and len(line.strip()) == 4):
            continue
        else:
            secondFunction(line)

for entries in lines_dict.items():
        print(entries[1])


def dict_list_to_csv_semicolon(dict_list, filename):
    try:
        with open(filename, 'w') as csv_file:
            
            # Write data rows
            for entries in dict_list.items():
                row_data = ';'.join(str(values) for values in entries[1]) + '\n'
                csv_file.write(row_data)
        
        print(f"CSV file '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


dict_list_to_csv_semicolon(lines_dict, 'output.csv')

