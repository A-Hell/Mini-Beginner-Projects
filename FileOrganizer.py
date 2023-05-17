import os
import pathlib
import shutil

file_dictionary = {
    "Web": [".html5", ".html", ".htm", ".xhtml"], 
	
    "Pictures": [".jpeg", ".jpg", ".tiff", ".gif",
    ".bmp", ".png", ".bpg", "svg",".heif", ".psd"], 
	
    "Videos": [".avi", ".mkv",".flv", ".wmv",
    ".mov", ".mp4", ".webm", ".vob", 
    ".mng",".qt", ".mpg", ".mpeg", ".3gp"], 
	
    "Documents": [".oxps", ".epub", ".pages", ".docx",
    ".txt", ".pdf", ".doc", ".fdf",
    ".ods",".odt", ".pwi", ".xsn",
    ".xps", ".dotx", ".docm", ".dox",
    ".rvg", ".rtf", ".rtfd", ".wpd", 
    ".xls", ".xlsx", ".ppt","pptx"], 
	
   "Compressed": [".a", ".ar", ".cpio", ".iso", 
    ".tar", ".gz", ".rz", ".7z",
    ".dmg", ".rar", ".xar", ".zip"], 
	
    "Music": [".aac", ".aa", ".aac", ".dvf",
    ".m4a", ".m4b", ".m4p", ".mp3",
    ".msv", "ogg", "oga", ".raw", 
    ".vox", ".wav", ".wma"],

    "Programs" : [".exe" , ".msi"]}

print("Note That if a file already exits in a folder it is being moved to the program will crash :< ")
print("")
start = input("Press Enter To Organize Your Files")
if start == "":
 active = True

file_type = list(file_dictionary.keys())
file_formats = list(file_dictionary.values())

for file in os.scandir():

    os.getcwd()
    
    file_name = pathlib.Path(file)
    format_type = file_name.suffix.lower()
    
    src = str(file_name)
    des = "Other"

    if file_type == "":
         print(src , "Has Unkown File Extension")
         continue
    else: 
            for formats in file_formats:
                if format_type in formats:
                    folder = file_type[file_formats.index(formats)]
                    des = folder
                    if os.path.isdir(folder) == False:
                         os.mkdir(folder)
                if os.path.isdir("Other") == False:
                    os.mkdir("Other")
    if src not in file_type and src not in ["FileOrganizer.exe" , 'FileOrganizer.py' , 'Other']: 
     print (  f"{src}" , " Moved To " , des)
     print("")
     shutil.move(src,des)


while active == True:
 exit = input("\n Press Enter To Exit")
 if exit == "" : break