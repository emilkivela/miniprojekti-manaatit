*** Settings ***
Resource  book_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser And Clear Database
Test Setup  Go To Book Adding Page And Clear Database

*** Test Cases ***
Add Book With Valid Info
    Set Key  XXX
    Set Title  Jdsfh Yeshd
    Set Author  Ewdkos Kdiffs
    Set Year  1876
    Submit Info
    Index Page Should Be Open
    Page Should Contain  XXX
    Page Should Contain  Jdsfh Yeshd
    Page Should Contain  Ewdkos Kdiffs
    Page Should Contain  1876

Add Book With Key Missing
    Set Title  Jdsfh Yeshd
    Set Author  Ewdkos Kdiffs
    Set Year  1876
    Submit Info
    Wait Until Page Contains  Create reference
    Page Should Contain  All fields must be filled

Add Book With Title Missing
    Set Key  BBB
    Set Author  Ewdkos Kdiffs
    Set Year  1876
    Submit Info
    Wait Until Page Contains  Create reference
    Page Should Contain  All fields must be filled

Add Book With Author Missing
    Set Key  CCC
    Set Title  Jdsfh Yeshd
    Set Year  1876
    Submit Info
    Wait Until Page Contains  Create reference
    Page Should Contain  All fields must be filled

Add Book With Year Missing
    Set Key  DDD
    Set Title  Jdsfh Yeshd
    Set Author  Ewdkos Kdiffs
    Submit Info
    Wait Until Page Contains  Create reference
    Page Should Contain  All fields must be filled

Add Book With Non-Numeric Year
    Set Key  EEE
    Set Title  Jdsfh Yeshd
    Set Author  Ewdkos Kdiffs
    Set Year  18r6
    Submit Info
    Wait Until Page Contains  Create reference
    Page Should Contain  Year must be a number
