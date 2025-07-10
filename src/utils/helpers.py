def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def validate_data(data):
    """Validates the data before processing."""
    if not data:
        log_message("No data provided for validation.")
        return False
    # Add more validation rules as needed
    log_message("Data validation passed.")
    return True

def format_data(data):
    """Formats the data for consistency."""
    if isinstance(data, list):
        formatted_data = [str(item).strip() for item in data]
    elif isinstance(data, dict):
        formatted_data = {k: str(v).strip() for k, v in data.items()}
    else:
        formatted_data = str(data).strip()
    
    log_message("Data formatting completed.")
    return formatted_data
def save_data_to_file(data, file_path):
    """Saves the data to a specified file."""
    try:
        with open(file_path, 'w') as file:
            file.write(str(data))
        log_message(f"Data saved successfully to {file_path}.")
    except Exception as e:
        log_message(f"Error saving data to file: {e}")
        raise
def read_data_from_file(file_path):
    """Reads data from a specified file."""
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        log_message(f"Data read successfully from {file_path}.")
        return data
    except FileNotFoundError:
        log_message(f"File not found: {file_path}.")
        raise
    except Exception as e:
        log_message(f"Error reading data from file: {e}")
        raise
def get_file_extension(file_path):
    """Returns the file extension of the given file path."""
    import os
    _, ext = os.path.splitext(file_path)
    return ext.lower() if ext else None
def is_valid_excel_file(file_path):
    """Checks if the file is a valid Excel file."""
    valid_extensions = ['.xlsx', '.xls']
    ext = get_file_extension(file_path)
    if ext in valid_extensions:
        log_message(f"{file_path} is a valid Excel file.")
        return True
    else:
        log_message(f"{file_path} is not a valid Excel file.")
        return False
def is_valid_csv_file(file_path):
    """Checks if the file is a valid CSV file."""
    valid_extensions = ['.csv']
    ext = get_file_extension(file_path)
    if ext in valid_extensions:
        log_message(f"{file_path} is a valid CSV file.")
        return True
    else:
        log_message(f"{file_path} is not a valid CSV file.")
        return False
def is_valid_json_file(file_path):
    """Checks if the file is a valid JSON file."""
    valid_extensions = ['.json']
    ext = get_file_extension(file_path)
    if ext in valid_extensions:
        log_message(f"{file_path} is a valid JSON file.")
        return True
    else:
        log_message(f"{file_path} is not a valid JSON file.")
        return False
def is_valid_text_file(file_path):
    """Checks if the file is a valid text file."""
    valid_extensions = ['.txt']
    ext = get_file_extension(file_path)
    if ext in valid_extensions:
        log_message(f"{file_path} is a valid text file.")
        return True
    else:
        log_message(f"{file_path} is not a valid text file.")
        return False
def is_valid_file(file_path):
    """Checks if the file is valid based on its extension."""
    if is_valid_excel_file(file_path):
        return True
    elif is_valid_csv_file(file_path):
        return True
    elif is_valid_json_file(file_path):
        return True
    elif is_valid_text_file(file_path):
        return True
    else:
        log_message(f"{file_path} is not a valid file type.")
        return False
def get_file_size(file_path):
    """Returns the size of the file in bytes."""
    import os
    try:
        size = os.path.getsize(file_path)
        log_message(f"Size of {file_path} is {size} bytes.")
        return size
    except FileNotFoundError:
        log_message(f"File not found: {file_path}.")
        raise
    except Exception as e:
        log_message(f"Error getting file size: {e}")
        raise
def get_file_creation_time(file_path):
    """Returns the creation time of the file."""
    import os
    try:
        creation_time = os.path.getctime(file_path)
        log_message(f"Creation time of {file_path} is {creation_time}.")
        return creation_time
    except FileNotFoundError:
        log_message(f"File not found: {file_path}.")
        raise
    except Exception as e:
        log_message(f"Error getting file creation time: {e}")
        raise
def get_file_modification_time(file_path):
    """Returns the last modification time of the file."""
    import os
    try:
        modification_time = os.path.getmtime(file_path)
        log_message(f"Last modification time of {file_path} is {modification_time}.")
        return modification_time
    except FileNotFoundError:
        log_message(f"File not found: {file_path}.")
        raise
    except Exception as e:
        log_message(f"Error getting file modification time: {e}")
        raise
def get_file_access_time(file_path):
    """Returns the last access time of the file."""
    import os
    try:
        access_time = os.path.getatime(file_path)
        log_message(f"Last access time of {file_path} is {access_time}.")
        return access_time
    except FileNotFoundError:
        log_message(f"File not found: {file_path}.")
        raise
    except Exception as e:
        log_message(f"Error getting file access time: {e}")
        raise
def get_file_info(file_path):
    """Returns a dictionary with file information."""
    import os
    if not os.path.exists(file_path):
        log_message(f"File not found: {file_path}.")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    file_info = {
        'size': get_file_size(file_path),
        'creation_time': get_file_creation_time(file_path),
        'modification_time': get_file_modification_time(file_path),
        'access_time': get_file_access_time(file_path),
        'is_valid': is_valid_file(file_path)
    }
    
    log_message(f"File info for {file_path}: {file_info}")
    return file_info
def get_file_name(file_path):
    """Returns the name of the file without the directory path."""
    import os
    file_name = os.path.basename(file_path)
    log_message(f"File name extracted: {file_name}")
    return file_name
def get_file_directory(file_path):
    """Returns the directory of the file."""
    import os
    file_directory = os.path.dirname(file_path)
    log_message(f"File directory extracted: {file_directory}")
    return file_directory
def get_file_path(file_name, directory):
    """Returns the full path of the file given its name and directory."""
    import os
    file_path = os.path.join(directory, file_name)
    log_message(f"Full file path constructed: {file_path}")
    return file_path
def get_file_extension(file_name):
    """Returns the file extension of the given file name."""
    import os
    _, ext = os.path.splitext(file_name)
    ext = ext.lower() if ext else None
    log_message(f"File extension extracted: {ext}")
    return ext
def get_file_name_without_extension(file_name):
    """Returns the file name without its extension."""
    import os
    file_name_without_ext = os.path.splitext(file_name)[0]
    log_message(f"File name without extension: {file_name_without_ext}")
    return file_name_without_ext
def get_file_extension_from_path(file_path):
    """Returns the file extension from the given file path."""
    import os
    _, ext = os.path.splitext(file_path)
    ext = ext.lower() if ext else None
    log_message(f"File extension from path: {ext}")
    return ext
def get_file_name_from_path(file_path):
    """Returns the file name from the given file path."""
    import os
    file_name = os.path.basename(file_path)
    log_message(f"File name from path: {file_name}")
    return file_name
def get_file_directory_from_path(file_path):
    """Returns the directory from the given file path."""
    import os
    file_directory = os.path.dirname(file_path)
    log_message(f"File directory from path: {file_directory}")
    return file_directory
def get_file_info_from_path(file_path):
    """Returns a dictionary with file information from the given file path."""
    import os
    if not os.path.exists(file_path):
        log_message(f"File not found: {file_path}.")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    file_info = {
        'size': get_file_size(file_path),
        'creation_time': get_file_creation_time(file_path),
        'modification_time': get_file_modification_time(file_path),
        'access_time': get_file_access_time(file_path),
        'is_valid': is_valid_file(file_path)
    }
    
    log_message(f"File info from path {file_path}: {file_info}")
    return file_info
def get_file_name_and_extension(file_path):
    """Returns the file name and its extension from the given file path."""
    import os
    file_name = os.path.basename(file_path)
    file_extension = get_file_extension(file_path)
    log_message(f"File name and extension: {file_name}, {file_extension}")
    return file_name, file_extension
def get_file_name_without_extension_from_path(file_path):
    """Returns the file name without its extension from the given file path."""
    import os
    file_name_without_ext = os.path.splitext(os.path.basename(file_path))[0]
    log_message(f"File name without extension from path: {file_name_without_ext}")
    return file_name_without_ext
def get_file_extension_from_name(file_name):
    """Returns the file extension from the given file name."""
    import os
    _, ext = os.path.splitext(file_name)
    ext = ext.lower() if ext else None
    log_message(f"File extension from name: {ext}")
    return ext
def get_file_name_from_name(file_name):
    """Returns the file name from the given file name."""
    import os
    file_name_only = os.path.basename(file_name)
    log_message(f"File name from name: {file_name_only}")
    return file_name_only
def get_file_directory_from_name(file_name):
    """Returns the directory from the given file name."""
    import os
    file_directory = os.path.dirname(file_name)
    log_message(f"File directory from name: {file_directory}")
    return file_directory
def get_file_path_from_name(file_name, directory):
    """Returns the full path of the file given its name and directory."""
    import os
    file_path = os.path.join(directory, file_name)
    log_message(f"Full file path from name: {file_path}")
    return file_path
def get_file_info_from_name(file_name, directory):  
    """Returns a dictionary with file information from the given file name and directory."""
    import os
    file_path = get_file_path_from_name(file_name, directory)
    if not os.path.exists(file_path):
        log_message(f"File not found: {file_path}.")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    file_info = {
        'size': get_file_size(file_path),
        'creation_time': get_file_creation_time(file_path),
        'modification_time': get_file_modification_time(file_path),
        'access_time': get_file_access_time(file_path),
        'is_valid': is_valid_file(file_path)
    }
    
    log_message(f"File info from name {file_name}: {file_info}")
    return file_info
def get_file_name_and_extension_from_name(file_name):
    """Returns the file name and its extension from the given file name."""
    import os
    file_name_only = os.path.basename(file_name)
    file_extension = get_file_extension_from_name(file_name)
    log_message(f"File name and extension from name: {file_name_only}, {file_extension}")
    return file_name_only, file_extension
def get_file_name_without_extension_from_name(file_name):
    """Returns the file name without its extension from the given file name."""
    import os
    file_name_without_ext = os.path.splitext(os.path.basename(file_name))[0]
    log_message(f"File name without extension from name: {file_name_without_ext}")
    return file_name_without_ext
def get_file_extension_from_path_name(file_path):
    """Returns the file extension from the given file path."""
    import os
    _, ext = os.path.splitext(file_path)
    ext = ext.lower() if ext else None
    log_message(f"File extension from path name: {ext}")
    return ext
def get_file_name_from_path_name(file_path):
    """Returns the file name from the given file path."""
    import os
    file_name = os.path.basename(file_path)
    log_message(f"File name from path name: {file_name}")
    return file_name
def get_file_directory_from_path_name(file_path):
    """Returns the directory from the given file path."""
    import os
    file_directory = os.path.dirname(file_path)
    log_message(f"File directory from path name: {file_directory}")
    return file_directory
def get_file_path_from_path_name(file_path):
    """Returns the full path of the file given its path name."""
    import os
    if not os.path.exists(file_path):
        log_message(f"File not found: {file_path}.")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    log_message(f"Full file path from path name: {file_path}")
    return file_path
def get_file_info_from_path_name(file_path):
    """Returns a dictionary with file information from the given file path."""
    import os
    if not os.path.exists(file_path):
        log_message(f"File not found: {file_path}.")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    file_info = {
        'size': get_file_size(file_path),
        'creation_time': get_file_creation_time(file_path),
        'modification_time': get_file_modification_time(file_path),
        'access_time': get_file_access_time(file_path),
        'is_valid': is_valid_file(file_path)
    }
    
    log_message(f"File info from path name {file_path}: {file_info}")
    return file_info
def get_file_name_and_extension_from_path_name(file_path):
    """Returns the file name and its extension from the given file path."""
    import os
    file_name = os.path.basename(file_path)
    file_extension = get_file_extension_from_path_name(file_path)
    log_message(f"File name and extension from path name: {file_name}, {file_extension}")
    return file_name, file_extension
def get_file_name_without_extension_from_path_name(file_path):
    """Returns the file name without its extension from the given file path."""
    import os
    file_name_without_ext = os.path.splitext(os.path.basename(file_path))[0]
    log_message(f"File name without extension from path name: {file_name_without_ext}")
    return file_name_without_ext
def get_file_extension_from_name_path(file_name, directory):
    """Returns the file extension from the given file name and directory."""
    import os
    file_path = get_file_path_from_name(file_name, directory)
    _, ext = os.path.splitext(file_path)
    ext = ext.lower() if ext else None
    log_message(f"File extension from name path: {ext}")
    return ext
def get_file_name_from_name_path(file_name, directory):
    """Returns the file name from the given file name and directory."""
    import os
    file_path = get_file_path_from_name(file_name, directory)
    file_name_only = os.path.basename(file_path)
    log_message(f"File name from name path: {file_name_only}")
    return file_name_only
def get_file_directory_from_name_path(file_name, directory):
    """Returns the directory from the given file name and directory."""
    import os
    file_path = get_file_path_from_name(file_name, directory)
    file_directory = os.path.dirname(file_path)
    log_message(f"File directory from name path: {file_directory}")
    return file_directory