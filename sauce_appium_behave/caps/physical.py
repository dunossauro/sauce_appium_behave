from os.path import abspath


def desired_caps(apk_path, apk_name,
                 platform_version='7.0',
                 device_name='Moto_G__5_'):
    """Return capabilities related to physical device."""
    return {
        'platformName': 'Android',
        'newCommandTimeout': 3000,
        'autoGrantPermissions': 'True',
        'platformVersion': platform_version,
        'deviceName': device_name,
        'rullReset': 'True',
        'noReset': 'False',
        'keepArtifacts': 'False',
        'app': abspath('{}{}'.format(apk_path, apk_name))}
