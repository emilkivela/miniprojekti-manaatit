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

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
Create User And Go To Login Page
    Register With Credentials  kalle  kalle123
    Go To Login Page

Submit Credentials
    Click Button  Sign in