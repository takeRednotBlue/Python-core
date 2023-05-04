import re
import os
import sys
from pathlib import Path
import shutil

def translitterate(text: str) -> str:
    letters_dict = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'h',
        'ґ': 'g',
        'д': 'd',
        'е': 'e',
        'є': 'ie',
        'ж': 'zh',
        'з': 'z',
        'и': 'y',
        'і': 'i',
        'ї': 'i',
        'й': 'i',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'kh',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ь': '',
        'ю': 'iu',
        'я': 'ia',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'H',
        'Ґ': 'G',
        'Д': 'D',
        'Е': 'E',
        'Є': 'Ye',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'Y',
        'І': 'I',
        'Ї': 'Yi',
        'Й': 'Y',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'Kh',
        'Ц': 'Ts',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Shch',
        'Ю': 'Yu',
        'Я': 'Ya'
    }

    trans_dict = str.maketrans(letters_dict)
    new_text = text.translate(trans_dict)
    return new_text

def normalize(path: str) -> int:
    '''Transliterate from cyrillic stem of the file and replace symbols
    other than latin letters and numbeіr with "_". The result is renamed Paths of the files'''
    count_list = []
    count_normalized_files = 0
    path_object = Path(path)
    files = [file for file in get_all_items(path_object)]
    for file in files:
        pattern = r"\W"
        new_stem = re.sub(pattern, "_", translitterate(file.stem))
        try:
            file.rename(file.parent / "".join([new_stem, file.suffix]))
            count_normalized_files += 1
        except FileExistsError:
            count_list.append(file.name)
            changed_stem = new_stem + "_1"
            file.rename(file.parent / "".join([changed_stem, file.suffix]))
            count_normalized_files += 1
    return count_list, count_normalized_files

            



def new_dir(path: Path, newDirName: str) -> Path:
    '''Makes new directory in the given path. Skips if directory exists.'''
    newDir = path / newDirName
    newDir.mkdir(exist_ok=True)
    return newDir

def get_all_items(path: Path):
        '''Generator that yields items recursively fro dirs and subdirs'''
        for item in path.iterdir():
            if item.is_dir():
                yield from get_all_items(item)
            else:
                yield item

count_removed_dirs = 0
def remove_empty_dirs(path: str) -> int:
    """Deletes empty dirs recursively"""
    global count_removed_dirs
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            remove_empty_dirs(os.path.join(root, dir))
        if not dirs and not files:
            os.rmdir(root) # os.rmdir() removes only if dir is empty
            count_removed_dirs += 1
    return count_removed_dirs 

def move_to_folder(file: Path, destPath: Path):
    '''Moves file and when FilesExistsError is raised recursively changes file stem 
    till exception resolved'''
    exception_counter = 1
    def error_handler():
        nonlocal exception_counter
        try:
            changed_stem = file.stem + f"_{exception_counter}"
            file.rename(destPath / "".join([changed_stem, file.suffix]))
        except FileExistsError:
            exception_counter += 1
            error_handler()
    try:
        file.rename(destPath / file.name)
    except FileExistsError:
        error_handler()
            
    
def sort_dir(path: str, unpackArch=True) -> None:
    path_object = Path(path)
    files = [file for file in get_all_items(path_object)]

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
        for categ, formats in file_formats.items():
            if file.suffix.lower() in formats:
                if categ == "Archives" and unpackArch == True and file.suffix in {".zip", ".tar", ".gztar", ".bztar", ".xztar"}:
                    dest_to_unpack = new_dir(path_object, categ)
                    unpack_arch_and_remove(file, dest_to_unpack)
                    break
                else:
                    move_to_folder(file, new_dir(path_object, categ))
                    break
        else:
            move_to_folder(file, new_dir(path_object, "Unknown"))
           


def dirs_info(path):
    print("-"*33)
    print("|{:^15}|{:^7}|{:^7}|".format("Dir name", "Files", "Subdirs"))
    print("-"*33)
    for root, dirs, files in os.walk(path):
        root_path_obj = Path(root)
        if str(root_path_obj.parent) == path:
            print(f'|{Path(root).name:<15}|{len(files):^7}|{len(dirs):^7}|')
        else: 
            continue
    print("-"*33)
    # path_object = Path(path)
    # dirs_count = 0
    # files_count = 0
    # for item in path_object.rglob("*"):
    #     if item.is_dir():
    #         dirs_count += 1
    #     else:
    #         files_count += 1
    # return files_count, dirs_count

def make_report(destPath: str):
    '''Writes report into a file'''
    # if destPath is str:
    destPath = Path(destPath)
    with open(destPath / "report.txt", 'w') as rep:
        rep.write("-"*33+"\n")
        rep.write("|{:^15}|{:^7}|{:^7}|\n".format("Dir name", "Files", "Subdirs"))
        rep.write("-"*33+"\n")
        for root, dirs, files in os.walk(destPath):
            root_path_obj = Path(root)
            if root_path_obj.parent == destPath:
                rep.write(f'|{Path(root).name:<15}|{len(files):^7}|{len(dirs):^7}|\n')
            else: 
                continue
        rep.write("-"*33+"\n")


def unpack_arch_and_remove(file: Path, dest: Path):
    destDir = dest / file.stem
    shutil.unpack_archive(file, destDir)
    file.unlink()



