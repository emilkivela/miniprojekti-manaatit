*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0.2 seconds
${ADDING_URL}  http://${SERVER}/new

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Go To Ref Adding Page
    Go To  ${ADDING_URL}

Book Adding Page Should Be Open
    Location Should Be  ${ADDING_URL}
    Page Should Contain  Create reference

Index Page Should Be Open
    Title Should Be  Main page
