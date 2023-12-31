import os
import shutil
from datetime import datetime

# Location of your RON project content folder with forward slashes and ending with /
destination_project_content = 'G:/ReadyOrNotModding/ReadyOrNotOne/Content/'

# Location of your GIT repo content folder with forward slashes and ending with /
# You can leave this as-is if it's run from the repo directory
destination_git_content = './Content/'

interfaces_list = 'MaterialInterfaces.txt'
path_to_replace = '/Game/'

# Instead of os.remove files are moved here under a utc time
# These should be created in the root dir of the respective drive by default.
recyclepath = '/ronMaterialsRecycleBin'

curtime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
def sync_files_by_time(file1, file2):
    try:
        # Get the modification timestamps of both files
        timestamp1 = os.path.getmtime(file1)
        timestamp2 = os.path.getmtime(file2)

        # Compare timestamps to determine if the files have different modification dates
        if timestamp1 != timestamp2:
            # Determine the newest file
            if timestamp1 > timestamp2:
                source_file = file1
                destination_file = file2
                bin_path = file2.replace(destination_git_content, (recyclepath + '/git/' + curtime + '/') , 1) 
            else:
                source_file = file2
                destination_file = file1
                bin_path = file1.replace(destination_project_content, (recyclepath + '/project/'  + curtime + '/') , 1)

            # Delete the older file if it exists
            if os.path.isfile(destination_file):
                # os.remove(destination_file)
                
                if not os.path.exists(os.path.dirname(bin_path)):
                    os.makedirs(os.path.dirname(bin_path))
                shutil.move(destination_file,bin_path)
            
            # Use os.link to create a hard link to the source file
            os.link(source_file, destination_file)

            print(f'Sync successful. Newest file: {source_file}')
        # else:
            # print(f'Files have the same modification date. No synchronization needed: {file1} <> {file2}.')

    except FileNotFoundError:
        print("One or both of the files not found.")

def sync_files(file):
    if line.startswith(path_to_replace):
        p_file = line.replace(path_to_replace, destination_project_content, 1)
        p_file = os.path.splitext(p_file)[0] + '.uasset'
        
        g_file = line.replace(path_to_replace, destination_git_content, 1)
        g_file = os.path.splitext(g_file)[0] + '.uasset'
        
        if os.path.isfile(p_file) and os.path.isfile(g_file):
            sync_files_by_time(p_file, g_file)
        else:
            if os.path.isfile(p_file):
                print(f'Linking project file to git. File: {p_file}')
                
                if not os.path.exists(os.path.dirname(g_file)):
                    os.makedirs(os.path.dirname(g_file))
                    
                os.link(p_file, g_file)
                
                
            elif os.path.isfile(g_file):
                print(f'Linking git to project. File: {p_file}')
                
                if not os.path.exists(os.path.dirname(p_file)):
                    os.makedirs(os.path.dirname(p_file))
                
                os.link(g_file, p_file)
                
def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

with open(interfaces_list, 'r') as file:
# Iterate through each line in the file
    i = 0
    for line in file:
        i += 1
        sync_files(line)
    print(f'Scanned {i} files')

size = get_directory_size(recyclepath) / 1024 / 1024
print(f'Recycle path size: {size:.2f} MB')