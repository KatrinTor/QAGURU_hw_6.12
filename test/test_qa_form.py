from selene import have
import allure
from resourses import RegistrationPage
from conftest import setup_browser


@allure.title("Successful fill form")
def test_fill_form(setup_browser):
    browser = setup_browser


    registration_page = RegistrationPage()
    with allure.step('Open'):
        registration_page.open()
       #browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
    with allure.step('Fill personal data'):
        registration_page.fill_full_name('Katrin', 'Torsunova')
        registration_page.fill_email('Katrin@test.ru')
        registration_page.choose_gender('Female')
        registration_page.fill_user_number('8967625366')
        registration_page.fill_birthdate(1994, 'November', 15)
        registration_page.set_subject('B')
        registration_page.select_hobbie('Reading')
        registration_page.attach_file('trusost.jpg')
        registration_page.fill_address('ul. Kronverksky 49')
        registration_page.select_state('Haryana')
        registration_page.select_city('Karnal')
    with allure.step('Click submit button'):
        registration_page.click_submit_batton()
    with allure.step('Assert personal data'):
        registration_page.should_have(
            'Katrin Torsunova',
            'Katrin@test.ru',
            'Female',
            '8967625366',
            '15 November,1994',
            'Biology',
            'Reading',
            'trusost.jpg',
            'ul. Kronverksky 49',
            'Haryana Karnal')
