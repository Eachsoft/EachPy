from EachKit.Io.Path import *
from EachKit.Io.Writers import *


def sync_directories(src, dest):
    # Compare the directories
    comparison = dircmp(src, dest)
    
    # Copy files that are in src but not in dest or have changed
    for name in comparison.left_only + comparison.diff_files:
        src_path = os.path.join(src, name)
        dest_path = os.path.join(dest, name)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)
        print(f"Copied: {src_path} to {dest_path}")

    # Recursively sync directories
    for common_dir in comparison.common_dirs:
        sync_directories(os.path.join(src, common_dir), os.path.join(dest, common_dir))

    # Remove files and directories that are in dest but not in src
    for name in comparison.right_only:
        dest_path = os.path.join(dest, name)
        if os.path.isdir(dest_path):
            shutil.rmtree(dest_path)
        else:
            os.remove(dest_path)
        print(f"Removed: {dest_path}")
