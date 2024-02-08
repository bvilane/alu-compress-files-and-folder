import os
import tarfile
import zipfile
import datetime

def compress_folder(folder_path, compress_type):
    try:
        # Get the name of the folder
        folder_name = os.path.basename(folder_path)

        # Get the current date
        current_date = datetime.datetime.now().strftime("%Y_%m_%d")

        # Create the compressed file name
        compressed_file_name = f"{folder_name}_{current_date}.{compress_type}"

        # Determine compression method based on user input
        if compress_type == 'zip':
            with zipfile.ZipFile(compressed_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))
        elif compress_type == 'tar':
            with tarfile.open(compressed_file_name, 'w') as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        elif compress_type == 'tgz':
            with tarfile.open(compressed_file_name, 'w:gz') as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        else:
            print("Unsupported compression type.")
            return

        print(f"Compression successful. Compressed file saved as: {compressed_file_name}")
    except Exception as e:
        print(f"Compression failed. Error: {str(e)}")

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    compress_types = ['zip', 'tar', 'tgz']
    print("Available compression types:")
    for i, compress_type in enumerate(compress_types, start=1):
        print(f"{i}. {compress_type}")

    try:
        choice = int(input("Enter the number corresponding to the desired compression type: "))
        selected_compress_type = compress_types[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    compress_folder(folder_path, selected_compress_type)

if __name__ == "__main__":
    main()

