from pathlib import Path
import shutil

def create_file_map(original_dir, modified_dir, allowed_extensions= {'.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif', '.arw'}):
    file_map = {}

    # Create a map from original file names to their full paths
    original_files = {file.stem: file for file in original_dir.rglob('*') if file.is_file() and file.suffix.lower() in allowed_extensions}
    modified_files = {file.stem: file for file in modified_dir.rglob('*') if file.is_file() and file.suffix.lower() in allowed_extensions}

    # for key, value in original_files.items():
    #     print(f"key: {key}, value: {value}")

    # Map each original file to its corresponding modified file based on name
    for key, original_file in original_files.items():
        modified_file = modified_files.get(key)
        modified_dir_name = str(modified_dir.name)
        original_dir_name = str(original_dir.name)

        if modified_file is None:
            file_map[original_file] = None
        elif modified_file.suffix.lower() == '.jpeg':  # Assuming all modified files are JPEGs
            file_map[original_file] = modified_file if modified_file else None
        else:
            print(f"Warning: Unmatched file {modified_file}")

    return file_map


def apply_changes(original_dir_name: str):
    base_dir = Path.cwd()
    modified_dir_name = original_dir_name + '_small'
    original_dir = Path(base_dir / original_dir_name)
    modified_dir = Path(base_dir / modified_dir_name)

    # Map of filenames to their paths in the original directory

    original_to_modified_files_map = create_file_map(original_dir, modified_dir)

    #print number of deletions and moves and wait for y key input
    print(f"Number of deletions: {len([x for x in original_to_modified_files_map.values() if x is None])}")
    files_to_delete = [key for key, val in original_to_modified_files_map.items() if val is None]
    print(f"files to be deleted:")
    for file in files_to_delete:
        print(file)
    print("Press y to continue")
    if input() != 'y':
        print("Exiting")
        return

    # Process moves and deletes
    for original_file, modified_file in original_to_modified_files_map.items():
        new_loc_in_original_dir = str(modified_file).replace(modified_dir_name, original_dir_name).replace('jpeg', 'ARW')
           
        if not modified_file:
            print(f"Deleting {original_file}")
            original_file.unlink()
        elif original_file != new_loc_in_original_dir:
            # new_loc_in_original_dir = str(modified_file).replace(modified_dir_name, original_dir_name)
            new_loc_in_original_dir = str(modified_file).replace(modified_dir_name, original_dir_name).replace('jpeg', 'ARW')
            if new_loc_in_original_dir != str(original_file):
                print(f"Moving {original_file} to {new_loc_in_original_dir}")
                # make parent directories if they don't exist
                new_loc_in_original_dir = Path(new_loc_in_original_dir)
                new_loc_in_original_dir.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(original_file), str(new_loc_in_original_dir))


    # # Remove empty directories in the original directory
    # for original_subdir in original_dir.rglob('*'):
    #     if original_subdir.is_dir() and not any(original_subdir.iterdir()):
    #         original_subdir.rmdir()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python move_delete.py <original_folder_name>")
        sys.exit(1)

    original_folder_name = sys.argv[1]
    apply_changes(original_folder_name)



    # "/Users/eduard/workspace/ed_copy_delete/data/100MSDCF/DKT03589.ARW"
    # "/Users/eduard/workspace/ed_copy_delete/data/DCIM/100MSDCF/DKT03589.ARW"