*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Book Adding Page

*** Test Cases ***
Add Book With Valid Info
    Set Key  SFGH
    Set Title  Jdsfh Yeshd
    Set Author  Ewdkos Kdiffs
    Set Year  1876
    Submit Info
    Index Page Should Be Open
    Page Should Contain  SFGH
    Page Should Contain  Jdsfh Yeshd
    Page Should Contain  Ewdkos Kdiffs
    Page Should Contain  1876

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
