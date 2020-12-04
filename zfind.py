#!/usr/bin/python
# pylint: disable=missing-module-docstring, invalid-name

import os
from zipfile import ZipFile

file_name = "test.doc"
archive_name = "test"
archive_ext = ".zip"
search_path = "/home"

archives = {}
for (path, _, files) in os.walk(search_path):
    for file in files:
        if file.endswith(archive_ext) and archive_name in file:
            file = f"{path}/{file}"
            temp_files = []
            with ZipFile(file) as myzip:
                zip_files = myzip.namelist()
            for zip_file in zip_files:
                if file_name in zip_file:
                    temp_files.append(zip_file)
            if temp_files:
                archives[path] = temp_files

for archive, zip_files in archives.items():
    for zip_file in zip_files:
        print(f"{archive}:{zip_file}")
    print("----")
