from selene.support.shared import browser
from selene import be, have


def test_success_finding(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_failed_finding(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selena gomez').press_enter()
    browser.element('[id="search"]').should_not(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
