#!/usr/bin/python
# pylint: disable=missing-module-docstring, invalid-name

from zipfile import ZipFile
import glob
import fnmatch

file_name = "*test*.doc"
archive = "/home/j*/test*.zip"

def find_in_zip_archives():
    """ Find zip archives and files in the zip archives.  Supports globs *.

    :return: dict of matched archive path/name and list of matched files in the archive
             ['/home/john/test1.zip': ['test11.doc', 'test22.doc']}
    """
    result = {}
    for archives_matched in glob.glob(archive):
        with ZipFile(archives_matched) as myzip:
            zip_file_list = myzip.namelist()
        temp_zip_files = []
        for zip_file in zip_file_list:
            if fnmatch.fnmatch(zip_file.split("/")[-1], file_name):
                temp_zip_files.append(zip_file)
        if temp_zip_files:
            results[archives_matched] = temp_zip_files
    return result

def print_results(archives):
    """ Print the matched archives and matched files in the archives

    :param archives: dict of matched archive path/name and list of matched files in the archive
                     ['/home/john/test1.zip': ['test11.doc', 'test22.doc']}
    """
    for archive_name, zip_files in archives.items():
        for zip_file in zip_files:
            print(f"{archive_name}:{zip_file}")

results = find_in_zip_archives()
print_results(results)
