import sys
import pandas, openpyxl, requests, pydantic, rapidfuzz
import dotenv

print("Python   ", sys.version.split()[0])
print("Running from:", sys.prefix)
print("pandas   ", pandas.__version__)
print("openpyxl ", openpyxl.__version__)
print("requests ", requests.__version__)
print("pydantic ", pydantic.__version__)
print("rapidfuzz", rapidfuzz.__version__)
print("dotenv    OK")
print("Setup complete.")