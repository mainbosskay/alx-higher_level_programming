#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as hidden_file
    names = dir(hidden_file)
    for name in names:
        if not name.startswith("__"):
            print(name)
