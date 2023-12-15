*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Run Keywords  Close Browser  AND  Clear Database
Test Setup  Run Keywords  Clear Database  AND  Register Test User And Login
Test Teardown  Sign Out

*** Test Cases ***
Add A Tag When Creating A Reference
    Create Tag  Test tag
    Add Reference  &{Test Book}  tag=1
    Go To Home Page
    Page Should Contain  Test tag

Add A Tag When Editing A Reference
    Create Tag  Test tag
    Add Reference  &{Test Book}
    Go To Edit Page For  &{Test Book}  id=1
    Select From List By Index  tag  1
    Click Button  Save changes
    Index Page Should Be Open
    Page Should Contain  Test tag

*** Keywords ***
Create Tag
    [Arguments]  ${tag}
    Go To  http://${SERVER}/create_tags
    Location Should Be  http://${SERVER}/create_tags
    Title Should Be  Add tag
    Input Text  name  ${tag}
    Click Button  Create a tag
