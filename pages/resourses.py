
from selene import browser, have, command, be

from test.conftest import path
from models.users import User


class RegistrationPage:

    def __init__(self):
        self.fist_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.phone_number = browser.element('#userNumber')
        self.subject = browser.element('#subjectsInput')
        self.hobbies = browser.all('[for^= hobbies]')
        self.upload_image = browser.element('#uploadPicture')

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def register(self, user: User):
        self.fist_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.gender.element_by(have.value(user.gender)).element('..').click()
        self.phone_number.type(user.phone_number)
        self.fill_date_of_birth(user.date_of_birth)
        self.subject.type(user.subjects).press_enter()
        self.hobbies.element_by(have.text(user.hobbies)).element('..').click()
        self.upload_image.send_keys(path(user.image))
        self.fill_current_address(user.current_address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.submit()
        return self

    def fill_date_of_birth(self, date):
        year = date.year
        month = date.month - 1
        day = date.strftime('%d')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'.react-datepicker__month-select option[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_current_address(self, value):
        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#currentAddress').should(be.blank).type(value)

        return self

    def fill_state(self, state):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(state)).click()
        return self

    def fill_city(self, city):
        browser.element('#city').click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(city)).click()

    def submit(self):
        browser.element('#submit').perform(command.js.click)

    def should_have_registered(self, user):
        # browser.element('.modal-content').should(be.visible)
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            f'{user.email}',
            f'{user.gender}',
            f'{user.phone_number}',
            '{0} {1},{2}'.format(user.date_of_birth.strftime("%d"),
                                 user.date_of_birth.strftime("%B"),
                                 user.date_of_birth.year),
            f'{user.subjects}',
            f'{user.hobbies}',
            f'{user.image}',
            f'{user.current_address}',
            f'{user.state} {user.city}'
        ))
