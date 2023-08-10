import datetime

import allure
from models.users import User
from pages.resourses import RegistrationPage

katrin = User(
first_name='Kat',
    last_name='Kat',
    email='test@test.by',
    gender='Female',
    phone_number='8967625366',
    date_of_birth=datetime.date(1994, 11, 15),
    hobbies='Reading',
    subjects='Biology',
    image='trusost.jpg',
    current_address='Kronverksky 4000',
    state='NCR',
    city='Delhi'
)


@allure.title('Successful fill form')
def test_registration_form(setup_browser):
    registration_page = RegistrationPage()

    with allure.step('Open registrations form'):
        registration_page.open()

    with allure.step('Fill form Users'):
        registration_page.register(katrin)

    with allure.step('Check form results'):
        registration_page.should_have_registered(katrin)
