Feature: OrangeHRM Login
    Scenario: Login to OrangeHRM with valid parameters
        Given I launch Chrome browser
        When I open orange HRM Homepage
        And Enter username "admin" and password "admin123"
        And Click on login button
        Then User must successfully login to the Dashboard page

    Scenario: Logo presence on OrangeHRM home Page
        Given Launch chrome browser
        When open orange hrm homepage
        Then verify that the logo present on page.
        And close. browser