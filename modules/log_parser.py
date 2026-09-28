def parse_log_file(file_path):
    """
    Reads a log file and converts it into structured events.
    """

    events = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if len(parts) >= 4:
                event = {
                    "date": parts[0],
                    "time": parts[1],
                    "event": parts[2],
                    "user": parts[3]
                }
                events.append(event)

    return events