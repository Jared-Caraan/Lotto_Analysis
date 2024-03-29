﻿<#
    Script developed by Jared Dominic V. Caraan
    
    Purpose: To compress log files
    -----------  ------                 -----------
    Change Date  Author                 Description
    -----------  ------                 -----------
    02-27-2020   j.caraan04@gmail.com   Archival of log text files older than 7 days for a more cleaner directory

#>

#--ACTIVATION OF VENV--#
    Set-Location -Path C:\venv\Scripts
    & .\activate.ps1

#--DECLARATIONS--#
    $script_dir = "C:\Users\Jared\Documents\Lotto_Analysis\Scripts\"
    $script = "lotto_archive.py"

#--EXECUTION OF PYTHON SCRIPT--#
    python "${script_dir}${script}"