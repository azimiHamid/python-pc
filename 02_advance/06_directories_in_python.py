from pathlib import Path

# Absolute path
# c:\program files\microsoft
# Relative path

# Create a Path object
path1 = Path("path_test")
path2 = Path("emails")
# path2.mkdir()  create the emails directory
# path2.rmdir()  removes the emails directory

print(path1.exists())
print(path2.exists())
print(path1.cwd())


# lets get all the files in the current directory
# current_file_path = Path(__file__)
# path = (current_file_path.parent)

path = Path()
for file in path.glob("*"):  # * -> all (file and folder), *.py -> all .py files, *.* -> all files 
    print(file)
    


# from pathlib import Path

# # Get the path to the current file (main.py)
# current_file_path = Path(__file__)

# # Get the directory of the current file
# current_dir = current_file_path.parent

# # Get the path to the 'ecommerce' folder (assuming it's a sibling to main.py)
# sibling_folder = current_dir / "ecommerce"

# # Check if the path exists
# print("Current file path:", current_file_path)
# print("Current directory:", current_dir)
# print("Sibling 'ecommerce' folder path:", sibling_folder)
# print("Does the 'ecommerce' folder exist?", sibling_folder.exists())
