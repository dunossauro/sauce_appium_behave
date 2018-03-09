from os.path import abspath


def desired_caps(apk_path, apk_name,
                 platform_version='4.4',
                 device_name='Nexus_5X_API_19'):
    """Return capabilities related to emulator."""
    return {
        'platformName': 'Android',
        'newCommandTimeout': 3000,
        'autoGrantPermissions': 'True',
        'platformVersion': platform_version,
        'avd': device_name,
        'deviceName': device_name,
        'rullReset': 'True',
        'noReset': 'False',
        'keepArtifacts': 'False',
        'app': abspath('{}{}'.format(apk_path, apk_name))}
