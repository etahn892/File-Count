import os

def count_files_in_folder(folder_path):
    try:
        # Initialize a counter for files
        file_count = 0

        # List all items (files and subfolders) in the specified folder
        items = os.listdir(folder_path)

        for item in items:
            item_path = os.path.join(folder_path, item)

            # Check if the item is a file
            if os.path.isfile(item_path):
                file_count += 1

        return file_count

    except FileNotFoundError:
        return "Folder not found."

    except PermissionError:
        return "Permission denied to access the folder."

# Specify the folder path for which you want to count files
folder_path = input("Enter File Path: \n")

# Call the function to count files in the folder
result = count_files_in_folder(folder_path)

if isinstance(result, int):
    print(f"Number of files in the folder: {result}")
else:
    print(f"Error: {result}")
