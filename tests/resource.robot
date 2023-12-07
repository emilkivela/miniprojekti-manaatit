*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Library  AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0 seconds
${INDEX_URL}  http://${SERVER}/
${ADDING_URL}  http://${SERVER}/new
${REGISTRATION_URL}  http://${SERVER}/register
${LOGIN_URL}  http://${SERVER}/login
${DOWNLOAD_DIR}  ${CURDIR}/test_downloads

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ${prefs}  Create Dictionary  download.default_directory=${DOWNLOAD_DIR}
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Call Method  ${options}  add_experimental_option  prefs  ${prefs}
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Close Browser And Clear Database
    Close Browser
    Clear Database

Go To Ref Adding Page
    Go To  ${ADDING_URL}

Go To Ref Adding Page For
    [Arguments]  ${type}
    Go To Ref Adding Page
    Click Button  show${type}
    Ref Adding Page Should Be Open For  ${type}

Go To Home Page
    Go To  ${INDEX_URL}

Go To Registration Page
    Go To  ${REGISTRATION_URL}

Go To Login Page
    Go To  ${LOGIN_URL}

Ref Adding Page Should Be Open For
    [Arguments]  ${type}
    Location Should Be  ${ADDING_URL}
    Page Should Contain  Create reference
    Radio Button Should Be Set To  reftype  show${type}

Book Adding Page Should Be Open
    Location Should Be  ${ADDING_URL}
    Page Should Contain  Create reference
    Radio Button Should Be Set To  reftype  showbook

Article Adding Page Should Be Open
    Location Should Be  ${ADDING_URL}
    Page Should Contain  Create reference
    Radio Button Should Be Set To  reftype  showarticle

Index Page Should Be Open
    Wait Until Location Is  ${INDEX_URL}
    Title Should Be  Main page

Registration Page Should Be Open
    Wait Until Page Contains  Create account
    Page Should Contain Button  Sign up

Add Reference
    [Arguments]  &{reference}
    Go To Ref Adding Page For  ${reference}[type]
    Set Local Variable  ${parent_id}  ${reference}[type]
    FOR  ${field}  ${value}  IN  &{reference}
        Set Local Variable  ${input_id}  ${field}
        IF  $field != "type"
            Input Text  css:#${parent_id} #${input_id}  ${value}
        END
    END
    Click Button  css:#${parent_id} input[value="Create reference"]
    Index Page Should Be Open
    Set Suite Variable  &{LATEST_REFERENCE}  &{reference}

Adding Reference Should Succeed
    ${exists} =  Get Variable Value  ${LATEST_REFERENCE}
    IF  $exists is None
        Fail  ERROR: Attempted to call 'Adding Reference Should Succeed' without first calling 'Add Reference'
    END
    FOR  ${field}  ${value}  IN  &{LATEST_REFERENCE}
        IF  $field != "type"
            Page Should Contain  ${value}
        END
    END

Reference Should Exist
    [Arguments]  &{reference}
    Go To Home Page
    Page Should Contain  ${reference}[key]

Reference Should Not Exist
    [Arguments]  &{reference}
    Go To Home Page
    Page Should Not Contain  ${reference}[key]
