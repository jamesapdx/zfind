#!/usr/bin/python
# pylint: disable=missing-module-docstring, invalid-name

from zipfile import ZipFile
import glob
import fnmatch
import argparse

def arg_parse():
    """ Process command line arguments

    :return: arg parse object
    """
    func = lambda  prog: argparse.HelpFormatter(prog, width=120)
    parser = argparse.ArgumentParser(formatter_class=func)

    parser.add_argument(
        '-a',
        dest='archive',
        nargs=1,
        required=True,
        help='zip archive name, including * wildcards'
    )
    parser.add_argument(
        '-f',
        dest='file',
        nargs=1,
        required=True,
        help='file name in the archive, including * wildcards'
    )

    return parser.parse_args()

def find_in_zip_archives(archive, file_name):
    """ Find zip archives and files in the zip archives.  Supports globs *.

    :return: dict of matched archive path/name and list of matched files in the archive
             ['/home/john/test1.zip': ['test11.doc', 'test22.doc']}
    """
    results = {}
    for archives_matched in glob.glob(archive):
        with ZipFile(archives_matched) as myzip:
            zip_file_list = myzip.namelist()
        temp_zip_files = []
        for zip_file in zip_file_list:
            if fnmatch.fnmatch(zip_file.split("/")[-1], file_name):
                temp_zip_files.append(zip_file)
        if temp_zip_files:
            results[archives_matched] = temp_zip_files
    return results

def print_results(archives):
    """ Print the matched archives and matched files in the archives

    :param archives: dict of matched archive path/name and list of matched files in the archive
                     ['/home/john/test1.zip': ['test11.doc', 'test22.doc']}
    """
    for archive_name, zip_files in archives.items():
        for zip_file in zip_files:
            print(f"{archive_name} --> {zip_file}")

if __name__ == "__main__":
    args = arg_parse()
    result_files = find_in_zip_archives(args.archive[0], args.file[0])
    print_results(result_files)
