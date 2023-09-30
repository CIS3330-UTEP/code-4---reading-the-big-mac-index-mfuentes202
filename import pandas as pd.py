import pandas as pd

try:
    version = pd.__version__
    print(f'pandas version {version} is installed.')
except ImportError:
    print('pandas is not installed.')
