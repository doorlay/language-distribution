library(reticulate)
os <- import("os")
os$listdir(".")

source_python("zipf.py")
python_nested_list <- main()
# This nested list must be reassigned to some form of data that works better with R's graphing