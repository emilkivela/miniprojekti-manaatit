*** Settings ***
Resource  resource.robot
Resource  book_resource.robot
Suite Setup  Run Keywords  Open And Configure Browser  AND  Register Test User And Login
Suite Teardown  Close Browser And Clear Database
Test Setup  Clear Database

*** Test Cases ***
Download File
    Go To Book Adding Page
    Set Key  JOTT
    Set Title  Jehi Rwifhe
    Set Author  Peiwh Wihiq
    Set Year  1678
    Submit Info
    Index Page Should Be Open
    Remove File  ${DOWNLOAD_DIR}/references.bib
    Go To Home Page
    Index Page Should Be Open
    Click Link  Download file
    Wait Until Created    ${DOWNLOAD_DIR}/references.bib
