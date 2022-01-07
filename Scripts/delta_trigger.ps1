<#
    Script developed by Jared Dominic V. Caraan
    
    Purpose: For automatic retrieval of latest 6/42 lotto winning result
    -----------  ------                 -----------
    Change Date  Author                 Description
    -----------  ------                 -----------
    09-22-2020   j.caraan04@gmail.com   Scheduled checking of new 6/42 lotto result from the website, and appending it to the datasheet

#>

#--ACTIVATION OF VENV--#
    Set-Location -Path C:\venv\Scripts
    & .\activate.ps1

#--DECLARATIONS--#
    $script_dir = "C:\Users\Jared\Documents\Lotto_Analysis\Scripts\"
    $script = "lotto_load_delta.py"

#--EXECUTION OF PYTHON SCRIPT--#
    python "${script_dir}${script}"