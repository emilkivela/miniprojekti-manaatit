*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Run Keywords  Close Browser  AND  Clear Database
Test Setup  Clear Database

*** Test Cases ***
Register Two Users With Same Username
    Register With Credentials  eirifl  c4h334c3
    Registration Should Succeed
    Register With Credentials  eirifl  rhw8o43h2
    Registration Should Fail With Message  Username already exists

Register With Too Short Password
    Register With Credentials  ehrfu  g4
    Registration Should Fail With Message  Password is too short

Log In With Registered Credentials
    Register With Credentials  uwelfew  4839r84h
    Registration Should Succeed
    Log In With Credentials  uwelfew  4839r84h
    Login Should Succeed

*** Keywords ***
Register With Credentials
    [Arguments]  ${username}  ${password}
    Go To Registration Page
    Input Text  username  ${username}
    Input Text  password  ${password}
    Click Button  Sign up

Registration Should Succeed
    Index Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Registration Page Should Be Open
    Page Should Contain  ${message}

Log In With Credentials
    [Arguments]  ${username}  ${password}
    Go To Login Page
    Input Text  username  ${username}
    Input Text  password  ${password}
    Click Button  Login

Login Should Succeed
    Index Page Should Be Open
