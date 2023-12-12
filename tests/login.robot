*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser And Clear Database
Test Setup  Run Keywords  Clear Database  AND  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed
    Sign Out

Login With Incorrect Username
    Set Username  kallo
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Wrong username or password

Login With Incorrect Password
    Set Username  kalle
    Set password  kalle345
    Submit Credentials
    Login Should Fail With Message  Wrong username or password

Login With Nonexistent Username
    Set Username  \
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Wrong username or password

See Other User's References
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Add Reference  &{Test Book}
    Sign Out
    Go To Login Page
    Set Username  jussi
    Set Password  jussi456
    Submit Credentials
    Wait Until Page Contains  Article-references
    Page Should Not Contain  ${Test Book}[key]
    Sign Out

Remove A Reference That Has The Same Key As Another User's Reference
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Add Reference  &{Test Book}
    Sign Out
    Go To Login Page
    Set Username  jussi
    Set Password  jussi456
    Submit Credentials
    Add Reference  &{Test Book}
    Remove Reference  &{Test Book}
    Go To Home Page
    Wait Until Page Contains  Article-references
    Page Should Not Contain  ${Test Book}[key]
    Sign Out
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Go To Home Page
    Wait Until Page Contains  Article-references
    Page Should Contain  ${Test Book}[key]

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Create User And Go To Login Page
    Register With Credentials  kalle  kalle123
    Register With Credentials  jussi  jussi456
    Go To Login Page

Submit Credentials
    Click Button  Sign in
