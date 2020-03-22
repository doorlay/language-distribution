library(reticulate)
os <- import("os")
os$listdir(".")

# Assigns all of the python data to a variable
words <- py_run_file("zipf.py")
for (p in words)
{
    print(p)
}