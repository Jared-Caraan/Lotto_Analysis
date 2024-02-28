<#
    Script developed by Jared Dominic V. Caraan
    
    Purpose: For automatic checking of ranges for 6/42 lotto winning result
    -----------  ------                 -----------
    Change Date  Author                 Description
    -----------  ------                 -----------
    02-29-2024   j.caraan04@gmail.com   Scheduled checking of ranges from 6/42 lotto results, and appending it to the datasheet

#>

#--ACTIVATION OF VENV--#
    Set-Location -Path C:\venv\Scripts
    & .\activate.ps1

#--DECLARATIONS--#
    $script_dir = "C:\Users\Jared\Documents\Lotto_Analysis\Scripts\"
    $script = "lotto_check_range_delta.py"

#--EXECUTION OF PYTHON SCRIPT--#
    python "${script_dir}${script}"