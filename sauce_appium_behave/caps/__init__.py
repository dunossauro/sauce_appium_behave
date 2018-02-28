"""Init caps."""
from os import environ, path

from appium import webdriver

SAUCE_URL = 'http://{}:{}@ondemand.saucelabs.com:80/wd/hub'
APPIUM_URL = 'http://localhost:4723/wd/hub'


def define_caps(target, apk_name, device_name,
                platform_version, apk_path='../', **kwargs):
    """
    TODO.

    implemente kwargs to upload caps
    """
    url = APPIUM_URL
    if target == 'local':
        desired_caps = {
            'platformName': 'Android',
            'newCommandTimeout': 3000,
            'autoGrantPermissions': 'True',
            'platformVersion': platform_version,
            'avd': device_name,
            'deviceName': device_name,
            'rullReset': 'True',
            'noReset': 'False',
            'keepArtifacts': 'False',
            'app': path.abspath('{}{}'.format(apk_path, apk_name))}

    if target == 'physical':
        desired_caps = {
            'platformName': 'Android',
            'newCommandTimeout': 3000,
            'autoGrantPermissions': 'True',
            'platformVersion': platform_version,
            'deviceName': device_name,
            'rullReset': 'True',
            'noReset': 'False',
            'keepArtifacts': 'False',
            'app': path.abspath('{}{}'.format(apk_path, apk_name))}

    if target == 'sauce':
        url = SAUCE_URL.format(environ['SAUCE_USER'], environ['SAUCE_KEY'])
        desired_caps = {
            'name': apk_name,
            'app': 'sauce-storage:{}'.format(apk_name),
            'platformName': 'Android',
            'device': device_name,
            'browserName': 'latest',
            'platformVersion': platform_version,
            'appiumVersion': '1.7.1',
            'deviceOrientation': 'portrait'}

    return webdriver.Remote(url, desired_caps)
