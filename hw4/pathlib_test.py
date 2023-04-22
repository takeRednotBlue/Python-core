from pathlib import Path
import re

def new_dir(path: Path, newDirName: str) -> Path:
    '''Makes new directory in the parent directory for file
     and nested directory for dir'''
    if path.is_file():
        newDir = path.parent / newDirName
        newDir.mkdir(exist_ok=True)
    else:
        newDir = path.parent / "books"
        newDir.mkdir(exist_ok=True)
    return newDir

def custom_sort_into_dir(files: list):
    file_formats = {
    'Audio': ['.mp3', '.wav', '.aac', '.wma', '.ogg', '.flac', '.alac', '.aiff', '.ape', '.au', '.m4a', '.m4b', '.m4p', '.m4r', '.mid', '.midi', '.mpa', '.mpc', '.oga', '.opus', '.ra', '.ram', '.tta', '.weba'],
    'Video': ['.mp4', '.avi', '.mkv', '.wmv', '.mov', '.flv', '.webm', '.m4v', '.mpg', '.mpeg', '.3gp', '.3g2', '.m2ts', '.mts', '.vob', '.ogv', '.mxf', '.divx', '.f4v', '.h264'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff', '.svg', '.webp', '.eps', '.raw', '.cr2', '.nef', '.dng', '.orf', '.arw', '.pef', '.raf', '.sr2', '.kdc', '.mos', '.mrw', '.dcr', '.x3f', '.erf', '.mef', '.pcx'],
    'Documents': ['.dot', '.odi', '.sxc', '.sxd', '.doc', '.txt', '.odf', '.sxw', '.odt', '.pdf', '.sxg', '.ott', '.odg', '.stw', '.sxi', '.stc', '.dotm', '.md', '.odc', '.docx', '.dotx', '.rtf'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv', '.xlsm', '.xlt', '.xltx', '.xlsb', '.numbers', '.ods'],
    'Presentations': ['.ppt', '.pptx', '.key', '.odp', '.pps', '.ppsx', '.pot', '.potx', '.potm'],
    'Archives': ['.zip', '.rar', '.tar.gz', '.7z', '.tar', '.tgz', '.bz2', '.dmg', '.iso', '.gz', '.jar', '.cab', '.z', '.tar.bz2', '.xz'],
    'Programs': ['.exe', '.apk', '.app', '.msi', '.deb', '.rpm', '.bat', '.sh', '.com', '.gadget', '.vb', '.vbs', '.wsf'],
    'Code': ['.py', '.java', '.js', '.html', '.css', '.cpp', '.c', '.php', '.xml', '.rb', '.pl', '.swift', '.h', '.hpp', '.cs', '.m', '.mm', '.kt', '.dart', '.go', '.lua', '.r', '.ps1'],
    'Database': ['.sql', '.db', '.mdb', '.accdb', '.sqlitedb', '.dbf', '.dbs', '.myd', '.frm', '.sqlite'],
    'Ebook': ['.epub', '.azw', '.azw3', '.fb2', '.ibooks', '.lit', '.mobi', '.pdb']
    }

    for file in files:
        for categ, format in file_formats.items():
            if file.suffix.lower() in format:
                file.rename(new_dir(file, categ) / file.name)
                break
        else:
            file.rename(new_dir(file, "unknown") / file.name)


donwloads = Path(r"C:\Users\maxym\OneDrive\Робочий стіл\Download")
files = [file for file in donwloads.iterdir() if file.is_file()]

# Finds all file formats in the dir
suffixes = set()
for file in files:
    suffixes.add(file.suffix)


# print(suffixes)
# custom_sort_into_dir(files)

doc = Path(r"C:\Users\maxym\OneDrive\Робочий стіл\Download\Documents")
files_doc = [file for file in doc.iterdir() if file.is_file()]


# Determine whether text contain Ukrainian letters
def contain_ukr_letters(text):
    ukrainian_pattern = re.compile('[А-ЩЬЮЯЄІЇҐа-щьюяєіїґ]')
    if ukrainian_pattern.search(text):
        return True
    else:
        False
 
# Delete all file that has Ukrainian letters in it's name       
# for file in files_doc:
#     if contain_ukr_letters(file.name):
#         file.unlink()
