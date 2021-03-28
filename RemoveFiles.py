import os
import shutil
import time

def ageOfFolder(path):

	ctime = os.stat(path).st_ctime

	return ctime


def removeFolder(path):

	if not shutil.rmtree(path):

		print(f"{path} is removed successfully")

	else:

		print(f"Unable to delete the "+path)



def removeFile(path):
	if not os.remove(path):

		print(f"{path} is removed successfully")

	else:

		print("Unable to delete the "+path)

def main():


	path = '/Dummyfolder'

	days = 30


	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):

		for root_folder, folders, files in os.walk(path):

			if seconds >= ageOfFolder(root_folder):

				removeFolder(root_folder)

				break

			else:

				for folder in folders:

					folder_path = os.path.join(root_folder, folder)

					if seconds >= ageOfFolder(folder_path):

						removeFolder(folder_path)

				for file in files:

					file_path = os.path.join(root_folder, file)

					if seconds >= ageOfFolder(file_path):

						removeFile(file_path)
    
		else:
            
			if seconds >= ageOfFolder(path):

				removeFile(path)
	else:
		print(f"{path} is not found")

if __name__ == '__main__':
	main()