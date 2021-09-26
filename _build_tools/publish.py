
import hashlib
import pathlib
import yaml
import subprocess
import shutil
import logging

def publish_changes():
    """Finds all changed files by comparing their MD5 hash value with the hash computed at the last publishing.  
    """
    raise NotImplementedError("This function is not adapted for the blog")

    logging.info("Publishing all changes...")

    # Tmp directory to hold all the changed files (used for the scp command)
    tmp_upload_dir = pathlib.Path("_build_tools/to_be_uploaded")

    # Load the currently saved hashs
    with open("_build_tools/file_hash.yaml", "r") as file:
        current_hashs = yaml.safe_load(file.read())

    # Get all files in _site and all subdirectories
    all_paths = pathlib.Path("_site").glob("**/*")
    files = [x for x in all_paths if x.is_file()]
    logging.info(f"Total files found: {len(files)}")

    # Get all files that are new or modified
    update_files = {}
    # Remove old tmp files, if existing
    if tmp_upload_dir.exists():
        shutil.rmtree(tmp_upload_dir)
    # Check all files if they are new or modified
    for file in files:
        # Get file path and hash
        file_path = str(file.relative_to("_site"))
        digest = hashlib.md5(file.read_bytes()).hexdigest()
        # Check if new or modified
        if current_hashs.get(file_path) != digest:
            # Add to update dict (path: hash)
            update_files[file_path] = digest
            # Copy file to tmp update directory
            upload_directory = pathlib.Path("_build_tools\\to_be_uploaded\\" + str(file.relative_to("_site").parent))
            upload_directory.mkdir(exist_ok=True, parents=True)
            shutil.copy(file, upload_directory)

    if len(update_files) == 0:
        logging.info("No new files to upload")
        logging.info("Done")
        return
    else:
        all_files_string = "\n- ".join(update_files.keys())
        logging.info(f"Found {len(update_files)} to upload (either new or modified):\n- {all_files_string}")

    # Upload files and then the hashs
    try:
        logging.info("Uploading files now...")
        subprocess.run("scp -r _build_tools/to_be_uploaded/* wbwurqmy@thelifeofash.com:/home1/wbwurqmy/public_html/daily", check=True, shell=True)
        logging.info("Done uploading")
        logging.info("Updating hash values...")
        current_hashs.update(update_files)
        with open("_build_tools/file_hash.yaml", "w") as file:
            yaml.dump(current_hashs, file)
        logging.info("Done updating hash values")
        logging.info("Cleaning up")
        if tmp_upload_dir.exists(): 
            shutil.rmtree(tmp_upload_dir)
        logging.info("Successfully uploaded all files")

    except subprocess.CalledProcessError:
        logging.error("An error occurred when uploading -->  the update of the files will not be saved")


if __name__ == "__main__":
    logging.basicConfig(format="[%(asctime)s] [%(levelname)8s] --- %(message)s", level=logging.INFO)
    publish_changes()
