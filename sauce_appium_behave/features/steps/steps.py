from behave import given, when, then

# put it in PO
BASE_ID = 'com.example.android.contactmanager:id/'


@given('I click on the add contact button')
def step_impl(context):
    context.driver.find_element_by_id(
        '{}addContactButton'.format(BASE_ID)).click()


@when('I enter a name and email')
def step_impl(context):
    context.driver.find_element_by_id(
        '{}contactNameEditText'.format(BASE_ID)).set_value('Some Name')
    context.driver.find_element_by_id(
        '{}contactEmailEditText'.format(BASE_ID)).set_value('Some@example.com')


@then('I click the Save button')
def step_impl(context):
    context.driver.find_element_by_id(
        '{}contactSaveButton'.format(BASE_ID)).click()
