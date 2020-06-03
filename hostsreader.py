class HostsReader:
    @staticmethod
    def read_all(path):
        try:
            result = {}

            with open(path, 'r') as file:
                lines = [line for line in file]
                for line in lines:
                    line = line.strip()

                    if len(line) == 0:
                        continue

                    if line[0] == "\r":
                        continue

                    if line[0] == "\n":
                        continue

                    if line[0] == "#":
                        continue

                    parts = line.split()

                    if len(parts) < 2:
                        continue

                    # looks like ipv4?
                    if parts[0].count('.') != 3:
                        print("Unrecognized hosts line :" + line)
                        continue

                    result[parts[1]] = parts[0]

            return result
        except IOError:
            return {}
