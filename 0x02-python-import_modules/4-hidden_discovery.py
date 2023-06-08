#!/usr/bin/env python3
import importlib.util

if __name__ == "__main__":
    # Load the compiled module
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Print the names in alphabetical order that do not start with '__'
    for name in sorted(dir(module)):
        if not name.startswith('__'):
            print(name)
