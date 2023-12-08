*** Settings ***
Resource  resource.robot
Resource  book_resource.robot
Suite Setup  Run Keywords  Open And Configure Browser  AND  Register Test User And Login
Suite Teardown  Close Browser And Clear Database
Test Setup  Clear Database

*** Test Cases ***
Download File
    Add Reference  type=book  key=JOTT  title=Jehi Rwifhe  author=Peiwh Wihiq  year=1678  publisher=Hewfiow
    Remove File  ${DOWNLOAD_DIR}/references.bib
    Go To Home Page
    Index Page Should Be Open
    Click Link  Download file
    Wait Until Created    ${DOWNLOAD_DIR}/references.bib
