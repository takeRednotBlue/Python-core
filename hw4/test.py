# my_list = [1, 1, 3, 4, 5, 5, 6, 6]

# for el in my_list:
#     if el == 5:
#         my_list.remove(el)



# # while 1 in my_list:
# #     my_list.remove(1)

# print(my_list)

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
    'ebook': ['.epub', '.azw', '.azw3', '.fb2', '.ibooks', '.lit', '.mobi', '.pdb']
}


Documents = ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.md', '.ppt', '.pptx', '.xls', '.xlsx', '.csv', '.odp', '.ott', '.xlsb', '.xlsm', '.xltx', '.dot', '.dotx', '.dotm', '.pps', '.ppsx', '.pot', '.potx', '.potm', '.odc', '.odf', '.odg', '.odi', '.ods', '.stw', '.sxw', '.stc', '.sxc', '.sxd', '.sxi', '.sxg']
Spreadsheets = ['.xls', '.xlsx', '.csv', '.xlsm', '.xlt', '.xltx', '.xlsb', '.numbers', '.ods']
Presentations = ['.ppt', '.pptx', '.key', '.odp', '.pps', '.ppsx', '.pot', '.potx', '.potm']

edited = set(Documents) - set(Spreadsheets) - set(Presentations)
print(file_formats['Audio'])