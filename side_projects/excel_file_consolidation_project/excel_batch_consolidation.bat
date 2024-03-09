@echo off
setlocal

set "input_directory=E:\git_folders\100-days-of-code\side_projects\excel_file_consolidation_project\main_folder\"
set "output_filename=C:\users\nagaraj\Merged_Data.xlsx"

echo Creating empty output file...
copy NUL "%output_filename%" > nul

for %%F in ("%input_directory%\*.xlsx") do (
    set "fullpath=%%~fF"
    set "filename=%%~nF"
    echo Merging sheets from %%~nxF...
    for /l %%N in (1, 1, 15) do (
        call :merge_sheet "%fullpath%" "%%N" "!filename!"
    )
)

echo Merging complete.
exit /b

:merge_sheet
set "excel_file=%1"
set "sheet_number=%2"
set "filename=%3"
set "temp_file=%filename%_temp.xlsx"

echo Extracting sheet %sheet_number% from %filename%...
powershell -Command "& { $excel = New-Object -ComObject Excel.Application; $workbook = $excel.Workbooks.Open('%excel_file%'); $worksheet = $workbook.Sheets.Item(%sheet_number%); $worksheet.Copy(); $workbook.SaveAs('%temp_file%'); $excel.Quit(); }"

echo Adding sheet %sheet_number% from %filename% to output file...
powershell -Command "& { $excel = New-Object -ComObject Excel.Application; $workbook = $excel.Workbooks.Open('%output_filename%'); $worksheet = $workbook.Sheets.Item($workbook.Sheets.Count); $importWorkbook = $excel.Workbooks.Open('%temp_file%'); $importWorksheet = $importWorkbook.Sheets.Item(1); $importWorksheet.Copy($null, $worksheet); $importWorkbook.Close(); $workbook.Save(); $excel.Quit(); }"

echo Cleaning up temp file...
del "%temp_file%"

exit /b