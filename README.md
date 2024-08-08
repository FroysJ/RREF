# RREF

import sys
import os

# Get the current directory of the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the directory containing the .pyd file
module_dir = os.path.join(script_dir, 'cmake-build-debug')

# Add the relative path to sys.path
sys.path.append(module_dir)

# for path in sys.path:
#     print(path)

# Import the module
import importlib.util
# spec = importlib.util.spec_from_file_location("example_module.cp312-win_amd64.pyd",
#                                               "/cmake-build-debug/example_module.cp312-win_amd64.pyd")
# foo = importlib.util.module_from_spec(spec)
# sys.modules["example_module.cp312-win_amd64.pyd"] = foo
# spec.loader.exec_module(foo)
# foo.Solution()

# import example_module