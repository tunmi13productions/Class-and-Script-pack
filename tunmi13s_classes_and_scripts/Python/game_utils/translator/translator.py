"""
Translator
This class provides a simple and straightforward way to translate text in your games or applications.
The format this translator takes is original_language=new_language. For example, Hello=Hola.
Note that this translator is not an advanced one, and you may have to do a lot of work in order for it to function properly.
"""
import os
class translator:
 def __init__(self,name,langfile,load_automatically = True):
  """Initiates the class.
   Parameters:
    name(str): The name of the language. This is the name it will be displayed as to the user, such as Spanish.
    langfile(str): A string containing the path of the language file.
    load_automatically(bool): Set to True if you want the class to load the language on initialization, False if you want to do it on your own later.
  """
  #This dictionary holds all the data from the language, with the original language data as the key and the translation language as the value.
  self.lang_data = {}
  self.name = name
  self.langfile = langfile
  if load_automatically: self.load()
 def load(self):
  #Loads the language data. Returns True if the language was loaded, False otherwise.
  if self.name == "" or self.langfile == "": return False
  if not os.path.isfile(self.langfile): return False
  f = open(self.langfile,"r")
  contents = f.read()
  f.close()
  #Split the data into lines
  lines = contents.split("\n")
  for i in range(0,len(lines)):
   #Separate with the equals sign.
   o2n = lines[i].split("=")
   #We want to make sure the length is 2, and only 2. Otherwise errors may start arising.
   if len(o2n) == 2: self.lang_data[o2n[0]] = o2n[1]
   else: continue
  return True
 def translate(self,text):
  """Attempts to translate the text provided into the translation language. This is done by finding if the text provided is included in lang_data (that being the key), then returning the value (that being the translation). If there is nothing found, it will just return the text provided.
   Parameters:
    text(str): The text to be translated.
  """
  if text in self.lang_data: return self.lang_data[text]
  else: return text
 def reload(self):
  #Reloads the translation, useful for updates.
  self.lang_data.clear()
  self.load()
