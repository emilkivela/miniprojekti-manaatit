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
&{Test Book}  type=book  key=REFC  title=Iwedj Pfwei  author=Qierhsfe Sgfnjr
...           year=1745  publisher=Wdslifhbb

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

Login Page Should Be Open
    Wait Until Page Contains  Sign in
    Page Should Contain Button  Sign in

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
    Set Suite Variable  &{LATEST_REFERENCE}  &{reference}

Adding Reference Should Succeed
    ${exists} =  Get Variable Value  ${LATEST_REFERENCE}
    IF  $exists is None
        Fail  ERROR: Attempted to call 'Adding Reference Should Succeed' without first calling 'Add Reference'
    END
    Index Page Should Be Open
    FOR  ${field}  ${value}  IN  &{LATEST_REFERENCE}
        IF  $field != "type"
            Page Should Contain  ${value}
        END
    END

Adding Reference Should Fail With Message
    [Arguments]  ${message}
    Wait Until Page Contains  Create reference
    Page Should Contain  ${message}

Remove Reference
    [Arguments]  &{reference}
    Go To Home Page
    Input Text  refkey  ${reference}[key]
    Click Button  Remove reference

Reference Should Exist
    [Arguments]  &{reference}
    Go To Home Page
    Page Should Contain  ${reference}[key]

Reference Should Not Exist
    [Arguments]  &{reference}
    Go To Home Page
    Page Should Not Contain  ${reference}[key]

Register With Credentials
    [Arguments]  ${username}  ${password}
    Go To Registration Page
    Input Text  username  ${username}
    Input Text  password  ${password}
    Click Button  Sign up

Register Test User And Login
    Register With Credentials  testuser  testuser1234
    Log In With Credentials  testuser  testuser1234

Registration Should Succeed
    Login Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Registration Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Log In With Credentials
    [Arguments]  ${username}  ${password}
    Go To Login Page
    Input Text  username  ${username}
    Input Text  password  ${password}
    Click Button  Sign in

Login Should Succeed
    Index Page Should Be Open

Sign Out
    Index Page Should Be Open
    Click Link  Sign out
