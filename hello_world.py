from datetime import date

def get_filename_datetime():
    # Use current date to get a text file name.
    return "file-" + str(date.today()) + ".txt"

# Get full path for writing.
name = get_filename_datetime()
print("NAME", name)

path = "C:\\Users\\SDG\\Desktop\\file_watch\\" + name
print("PATH", path);

with open(path, "w") as f:
    # Write data to file.
    f.write("HELLO\n")
    f.write("WORLD\n")
