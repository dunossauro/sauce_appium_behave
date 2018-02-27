"""Hooks file."""
from os import environ

from appium import webdriver
from behave.tag_matcher import ActiveTagMatcher
from sauceclient import SauceClient, Storage

from sauce_appium_behave.helpers.constants import SAUCE_URL

active_tag_value_provider = {}

active_tag_matcher = ActiveTagMatcher(active_tag_value_provider)


def before_all(context):
    """
    Get behave.ini configs and start saucelabs client.

    VARS:
        context.userdata: Behave ini usardata fields params
        context.sc: SauceClient class loged in context
        context.storage: Storage class to upload and check sauce files
    """
    context.userdata = context.config.userdata
    context.apk_name = context.userdata['apk']
    context.apk_path = context.userdata['apk_path']
    context.device = context.userdata['device']
    context.version = context.userdata['platform_version']
    context.sc = SauceClient(environ['SAUCE_USER'], environ['SAUCE_KEY'])
    context.storage = Storage(context.sc)


def before_feature(context, feature):
    """
    Check if apk is oploaded in sauce storage.

    if file in store, use don't upload, you can force upload_file
        in many cases if the new has the same name:
        context.storage.upload_file(context.apk_path, True)

    https://github.com/cgoldberg/sauceclient/pull/19
    """
    if context.apk_name not in context.storage.get_stored_files()['files']:
        context.storage.upload_file(context.apk_path)


def before_scenario(context, scenario):
    """TODO."""
    if active_tag_matcher.should_exclude_with(scenario.effective_tags):
        scenario.skip(reason="DISABLED ACTIVE-TAG")

    desired_caps = {
        'name': context.name,
        'app': 'sauce-storage:{}'.format(context.apk_name),
        'platformName': 'Android',
        'device': context.device,
        'browserName': 'latest',
        'platformVersion': context.version,
        'appiumVersion': '1.7.1',
        'deviceOrientation': 'portrait'}

    context.driver = webdriver.Remote(SAUCE_URL,
                                      desired_caps)


def after_scenario(context, scenario):
    """TODO."""
    if hasattr(context, 'driver'):
        context.driver.quit()
        test_status = scenario.status == 'passed'
        context.sc.jobs.update_job(context.driver,
                                   passed=test_status)
