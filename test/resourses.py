import os
from selene import browser, have


class RegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def fill_full_name(self, first_name, last_name):
        browser.element('[id=firstName]').type(first_name)
        browser.element('[id=lastName]').type(last_name)

    def fill_birthdate(self, year, monts, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(monts)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def fill_email(self, address):
        browser.element('[id=userEmail]').type(address)

    def choose_gender(self, gender):
        browser.element(f'//label[contains(text(), "{gender}")]').click()

    def fill_user_number(self, telephone_number):
        browser.element('[id=userNumber]').type(telephone_number)

    def set_subject(self, first_lettet):
        browser.element('#subjectsInput').type(first_lettet).press_enter()

    def select_hobbie(self, value):
        browser.element(f'//label[contains(text(), "{value}")]').click()

    def fill_address(self, address):
        browser.element('[id=currentAddress]').click()
        browser.element('[id=currentAddress]').type(address)

    def select_state(self, param):
        browser.element('#state').click()
        browser.all("#state div").element_by(have.exact_text(param)).click()

    def select_city(self, param):
        browser.element('#city').click()
        browser.all("#city div").element_by(have.exact_text(param)).click()

    def click_submit_batton(self):
        browser.element('[id=submit]').click()

    def attach_file(self, name):
        browser.element('#uploadPicture').send_keys(os.path.abspath(name))

    def should_have(self, full_name, email, gender, phone_number, birthday,
                    subject, hobbie, file_name, address, state_and_city):
        browser.element('.table').all('td').even.should(have.exact_texts(
            full_name, email, gender, phone_number, birthday,
            subject, hobbie, file_name, address, state_and_city))