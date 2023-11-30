*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Article Adding Page

*** Test Cases ***
Add Article With Valid Info
    Set Key  SFGH
    Set Title  Jdsfh Yeshd
    Set Author  Ewdkos Kdiffs
    Set Journal  Gehsilhw
    Set Year  1876
    Set Volume  15
    Set Pages  145-6
    Submit Info
    Index Page Should Be Open
    Page Should Contain  SFGH
    Page Should Contain  Jdsfh Yeshd
    Page Should Contain  Ewdkos Kdiffs
    Page Should Contain  Gehsilhw
    Page Should Contain  1876
    Page Should Contain  15
    Page Should Contain  145-6

Add Article With Key Missing
    Set Title  Jdsfh Yeshd
    Set Author  Ewdkos Kdiffs
    Set Journal  Gehsilhw
    Set Year  1876
    Set Volume  15
    Set Pages  145-6
    Submit Info
    Page Should Contain  Create reference
    Page Should Contain  All fields must be filled

Add Article With Title Missing
    Set Key  SFGH
    Set Author  Ewdkos Kdiffs
    Set Journal  Gehsilhw
    Set Year  1876
    Set Volume  15
    Set Pages  145-6
    Submit Info
    Page Should Contain  Create reference
    Page Should Contain  All fields must be filled

Add Article With Author Missing
    Set Key  SFGH
    Set Title  Jdsfh Yeshd
    Set Journal  Gehsilhw
    Set Year  1876
    Set Volume  15
    Set Pages  145-6
    Submit Info
    Page Should Contain  Create reference
    Page Should Contain  All fields must be filled

Add Article With Journal Missing
    Set Key  SFGH
    Set Title  Jdsfh Yeshd
    Set Author  Ewdkos Kdiffs
    Set Year  1876
    Set Volume  15
    Set Pages  145-6
    Submit Info
    Page Should Contain  Create reference
    Page Should Contain  All fields must be filled

Add Article With Year Missing
    Set Key  SFGH
    Set Title  Jdsfh Yeshd
    Set Author  Ewdkos Kdiffs
    Set Journal  Gehsilhw
    Set Volume  15
    Set Pages  145-6
    Submit Info
    Page Should Contain  Create reference
    Page Should Contain  All fields must be filled

Add Article With Non-Numeric Year
    Set Key  SFGH
    Set Title  Jdsfh Yeshd
    Set Author  Ewdkos Kdiffs
    Set Journal  Gehsilhw
    Set Year  18r6
    Set Volume  15
    Set Pages  145-6
    Submit Info
    Page Should Contain  Create reference
    Page Should Contain  Year must be a number

Add Article With Volume Missing
    Set Key  SFGH
    Set Title  Jdsfh Yeshd
    Set Author  Ewdkos Kdiffs
    Set Journal  Gehsilhw
    Set Year  1876
    Set Pages  145-6
    Submit Info
    Page Should Contain  Create reference
    Page Should Contain  All fields must be filled

Add Article With Pages Missing
    Set Key  SFGH
    Set Title  Jdsfh Yeshd
    Set Author  Ewdkos Kdiffs
    Set Journal  Gehsilhw
    Set Year  1876
    Set Volume  15
    Submit Info
    Page Should Contain  Create reference
    Page Should Contain  All fields must be filled

*** Keywords ***
Submit Info
    Click Button  css:#article input[value="Create reference"]

Set Key
    [Arguments]  ${key}
    Input Text  css:#article #key  ${key}

Set Title
    [Arguments]  ${title}
    Input Text  css:#article #title  ${title}

Set Author
    [Arguments]  ${author}
    Input Text  css:#article #author  ${author}

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Year
    [Arguments]  ${year}
    Input Text  css:#article #year  ${year}

Set Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}

Set Pages
    [Arguments]  ${pages}
    Input Text  pages  ${pages}

Go To Article Adding Page
    Go To Ref Adding Page
    Click Button  showarticle
    Article Adding Page Should Be Open