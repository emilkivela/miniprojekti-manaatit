*** Settings ***
Resource  resource.robot

*** Keywords ***
Submit Info
    Click Button  Create reference

Set Key
    [Arguments]  ${key}
    Input Text  key  ${key}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Go To Book Adding Page
    Go To Ref Adding Page
    Click Button  showbook
    Book Adding Page Should Be Open

Go To Book Adding Page And Clear Database
    Go To Book Adding Page
    Clear Database
