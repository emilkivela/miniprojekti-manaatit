*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Download File
    Remove File  ${DOWNLOAD_DIR}/references.bib
    Go To Home Page
    Index Page Should Be Open
    Click Link  Download file
    File Should Exist    ${DOWNLOAD_DIR}/references.bib