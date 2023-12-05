*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Library  AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0 seconds
${INDEX_URL}  http://${SERVER}/
${ADDING_URL}  http://${SERVER}/new
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

Go To Home Page
    Go To  ${INDEX_URL}

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
