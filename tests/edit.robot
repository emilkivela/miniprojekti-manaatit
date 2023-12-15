*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Run Keywords  Close Browser  AND  Clear Database
Test Setup  Run Keywords  Clear Database  AND  Register Test User And Login
Test Teardown  Sign Out

*** Test Cases ***
View Edit Page For A Reference
    Add Reference  &{Test Book}
    Go To Edit Page For  &{Test Book}  id=1
    Edit Page Should Be Open For  book
    Page Should Contain All Fields Of  &{Test Book}

View Edits On Listing Page
    Add Reference  &{Test Book}
    Go To Edit Page For  &{Test Book}  id=1
    Input Text  key  FGEC
    Click Button  Save changes
    Index Page Should Be Open
    Page Should Contain  FGEC
    Page Should Not Contain  ${Test Book}[key]

*** Keywords ***
Edit Page Should Be Open For
    [Arguments]  ${type}
    Location Should Be  http://${SERVER}/edit_${type}/${CURRENT_ID}
    Page Should Contain  Edit reference
    Page Should Contain Button  Save changes

Page Should Contain All Fields Of
    [Arguments]  &{reference}
    FOR  ${field}  ${value}  IN  &{reference}
        IF  $field != "type"
            Page Should Contain Textfield  ${value}
        END
    END
