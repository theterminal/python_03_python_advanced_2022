def parse_line(line):
    parsed = line.split()

    if parsed[0] == 'Create':
        return [parsed[0], int(parsed[2])]
    elif parsed[0] == 'Locate':
        return [parsed[0], int(parsed[1])]
