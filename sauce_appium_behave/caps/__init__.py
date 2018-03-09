"""Init caps."""
from os import environ, path

from appium import webdriver
from . import emulator, physical, sauce

SAUCE_URL = 'http://{}:{}@ondemand.saucelabs.com:80/wd/hub'
APPIUM_URL = 'http://localhost:4723/wd/hub'


def define_caps(target, apk_name, device_name,
                platform_version, apk_path='../', external_caps={}):
    """TODO."""
    url = APPIUM_URL
    if target == 'sauce':
        url = SAUCE_URL.format(environ['SAUCE_USER'], environ['SAUCE_KEY'])

    target = eval(target)
    if hasattr(target, 'desired_caps'):
        capabilities = target.desired_caps(apk_path, apk_name)
        capabilities.update(external_caps)
        return webdriver.Remote(url, capabilities)
    return None
