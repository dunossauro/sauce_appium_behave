from os.path import abspath


def desired_caps(apk_path, apk_name,
                 platform_version='4.4',
                 device_name='Android Emulator'):
    """Return capabilities related to physical device."""
    return {
        'name': apk_name,
        'app': 'sauce-storage:{}'.format(apk_name),
        'platformName': 'Android',
        'device': device_name,
        'browserName': 'latest',
        'platformVersion': platform_version,
        'appiumVersion': '1.7.1',
        'deviceOrientation': 'portrait'}
