
import hashlib
import pathlib
import yaml
import subprocess
import shutil
import logging
import argparse
import os


def build_site():
    """Builds the site with jekyll
    """
    logging.info("Building site...")
    try:
        subprocess.run("bundle exec jekyll build", check=True, shell=True)
    except subprocess.CalledProcessError:
        logging.error("An error occurred when building the site")
    else:
        logging.info("Done building the site")


def publish_changes(testing, upload_all):
    """Finds all changed files by comparing their MD5 hash value with the hash computed at the last publishing.  
    """
    # Path to the file hashs file
    current_hashs_path = "_build_tools/file_hash.yaml"
    # Tmp directory to hold all the changed files (used for the scp command)
    tmp_upload_dir = pathlib.Path("_build_tools/to_be_uploaded")

    logging.info("Publishing all changes...")

    # File hashs file does not exist or all files should be uploaded -> create empty file hashs file
    if upload_all or not os.path.isfile(current_hashs_path):
        with open(current_hashs_path, "w") as file:
            file.write("")

    # Load the currently saved hashs
    with open(current_hashs_path, "r") as file:
        current_hashs = yaml.safe_load(file.read())
    if not current_hashs:
        current_hashs = {}

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

    # Inform user about the files that will be uploaded, if any
    if len(update_files) == 0:
        logging.info("No new files to upload")
        logging.info("Done")
        return
    else:
        all_files_string = "\n- ".join(update_files.keys())
        logging.info(f"Following files will be uploaded:\n- {all_files_string}")
        logging.info(f"Found {len(update_files)} to upload (either new or modified)")
    
    # Target address, where all files are gonna be uploaded to
    target_address = "wbwurqmy@thelifeofash.com:/home1/wbwurqmy/public_html"
    if testing: target_address += "/aperture"
    logging.info(f"Upload address: {target_address}")

    # Upload files and then the hashs
    try:
        logging.info("Uploading files now...")
        subprocess.run(f"scp -r _build_tools/to_be_uploaded/* {target_address}", check=True, shell=True)
        logging.info("Done uploading")
        logging.info("Updating hash values...")
        current_hashs.update(update_files)
        with open("_build_tools/file_hash.yaml", "w") as file:
            yaml.dump(current_hashs, file)
        logging.info("Done updating hash values")

    except subprocess.CalledProcessError:
        logging.error("An error occurred when uploading -->  the update of the files will not be saved")

    finally:
        logging.info("Cleaning up")
        if tmp_upload_dir.exists(): 
            shutil.rmtree(tmp_upload_dir)
    
    logging.info("Done publishing")


# TODO add commandline argument to publish the changes to the main blog directory
if __name__ == "__main__":
    logging.basicConfig(format="[%(asctime)s] [%(levelname)8s] --- %(message)s", level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--publish", help="Publishes the changes to the main website instead of the test site 'Aperture'", action="store_true")
    parser.add_argument("-a", "--all", help="Uploads all files, instead of only uploading the files that have changed", action="store_true")
    args = parser.parse_args()

    build_site()
    publish_changes(
        testing = not args.publish,
        upload_all = args.all
    )
