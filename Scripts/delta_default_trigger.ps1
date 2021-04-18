<#
    Script developed by Jared Dominic V. Caraan
    
    Purpose: For automatic retrieval of latest 6/42 lotto winning result (default order)
    -----------  ------                 -----------
    Change Date  Author                 Description
    -----------  ------                 -----------
    04-18-2021   j.caraan04@gmail.com   Scheduled checking of new 6/42 lotto result from the website, and appending it to the datasheet

#>

#--ACTIVATION OF VENV--#
    Set-Location -Path C:\env\Scripts
    & .\activate.ps1

#--DECLARATIONS--#
    $script_dir = "C:\Personal_Project\Lotto_Analysis\Scripts\"
    $script = "lotto_default_delta.py"

#--EXECUTION OF PYTHON SCRIPT--#
    python "${script_dir}${script}"