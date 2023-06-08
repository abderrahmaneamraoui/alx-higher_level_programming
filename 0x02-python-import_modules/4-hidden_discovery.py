#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for name in sorted(dir(module)):
        if not name.startswith('__'):
            print(name)
