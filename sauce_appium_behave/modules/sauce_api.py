"""
Module example.

You can use modules for simplify the functions calls in your tests.
"""

from os.path import abspath

import sauceclient


def upload_apk(apk_name, apk_path, storage):
    if not check_uploaded_apk(apk_name, storage):
        storage.upload_file(abspath('{}{}'.format(apk_path, apk_name)))


def check_uploaded_apk(apk_path: str, storage: sauceclient.Storage):
    """
    Check if apk is on storage.

    Generate a apk checksum (MD5) to compare name and md5 with sauce response

    TODO: implement md5_sum a check response

    NOTE: Saucelabs storage api response example
    {'files': [{'name': 'ContactManager.apk',
                'size': 25931,
                'md5': 'b2d2916bb5388e1dc281ec3e71ef1234',
                'mtime': 1519825807.6420677}]}
    """
    return True
