#13Updater, version 1.0
#This updater works by grabbing a version file with the given URL, and then comparing it with the given version number when called in your script.
#Please note! The method that is used in this updater will cause the main application to freeze, due to the fact that it is using wget.
#That being said,, if you are going to use this updater, warn the users that it may freeze the application, and if it does, do not close it or interfere with it.
#Required modjules.
import requests
import wget
class Updater:
	def __init__(self,project_name,current_version,version_path):
		"""Class initialization.
			Parameters:
				project_name (str): The name of your project, such as My Project.
				current_version (str): The current version of your project. This is a string because it may vary how the updater is used.
				version_path (str): A URL pointing to a file which contains a string specifying the latest version.
		"""
		self.project_name = project_name
		self.version_path = version_path
		self.current_version = current_version
	def check_for_updates(self):
		#This checks for any available updates. This will return true if an update is found, and false if there is no update.
		temp = requests.get(self.version_path)
		new_version = temp.content.decode()
		if self.current_version < new_version: return True
		else: return False
	def get_version(self):
		#This retrieves the latest version of the project without checking for an update. Returns a string containing the latest version if found, or a blank string if nothing was found.
		temp = requests.get(self.version_path)
		new_version = temp.content.decode()
		return new_version
	def dl(self,project_url_path):
		"""This starts downloading the project. Note what I said at the top of the file!
			Parameters:
				project_url_path (str): The path to the project. This can be a ZIP file, an EXE file, etc. For example, https://my-website.com/my_project.zip.
		"""
		wget.download(project_url_path,".")
