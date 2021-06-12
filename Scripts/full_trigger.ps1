<#
    Script developed by Jared Dominic V. Caraan
    
    Purpose: For automatic retrieval of latest 6/42 lotto winning result
    -----------  ------                 -----------
    Change Date  Author                 Description
    -----------  ------                 -----------
    09-22-2020   j.caraan04@gmail.com   Full scrape of 6/42 results

#>

#--ACTIVATION OF VENV--#
    Set-Location -Path C:\env\Scripts
    & .\activate.ps1

#--DECLARATIONS--#
    $script_dir = "C:\Personal_Project\Lotto_Analysis\Scripts\"
    $script = "lotto_load_full.py"
	$script2 = "lotto_concat_all.py"

#--EXECUTION OF PYTHON SCRIPT--#
    python "${script_dir}${script}"
	python "${script_dir}${script2}"