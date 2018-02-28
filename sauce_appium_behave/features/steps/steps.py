from behave import given, when, then


@given('I click on the add contact button')
def step_impl(context):
    context.driver.find_element_by_id(
        "com.example.android.contactmanager:id/addContactButton").click()


@when('I enter a name and email')
def step_impl(context):
    context.driver.find_element_by_id(
        "com.example.android.contactmanager:id/contactNameEditText").set_value("Some Name")
    context.driver.find_element_by_id(
        "com.example.android.contactmanager:id/contactEmailEditText").set_value("Some@example.com")


@then('I click the Save button')
def step_impl(context):
    context.driver.find_element_by_id(
        "com.example.android.contactmanager:id/contactSaveButton").click()
