# # Set the path to your main folder
# $mainFolder = "E:\git_folders\100-days-of-code\side_projects\excel_file_consolidation_project\main_folder"
#
# # Set the path to the new excel file
# $outputFile = "C:\users\nagaraj\file.xlsx"
#
# # Initialize a new Excel application
# $excel = New-Object -ComObject Excel.Application
# $excel.Visible = $false
# $excel.DisplayAlerts = $false
#
# # Create a new workbook
# $workbook = $excel.Workbooks.Add()
#
# # Initialize a counter to keep track of the row number
# $row = 1
#
# # Loop through each sub_folder in the main folder
# Get-ChildItem -Path $mainFolder -Directory | ForEach-Object {
#     $subFolder = $_.FullName
#
#     # Loop through each Excel file in the sub_folder
#     Get-ChildItem -Path $subFolder -Filter *.xlsx | ForEach-Object {
#         $excelFile = $_.FullName
#
#         # Open the Excel file
#         $sourceWorkbook = $excel.Workbooks.Open($excelFile)
#
#         # Copy data from the first sheet of the Excel file to the output workbook
#         $sourceWorksheet = $sourceWorkbook.Sheets.Item(1)
#         $sourceRange = $sourceWorksheet.UsedRange
#         $sourceRange.Copy()
#
#         # Paste data into the output workbook
#         $targetWorksheet = $workbook.Sheets.Item(1)
#         $targetRange = $targetWorksheet.Cells.Item($row, 1)
#         $targetRange.PasteSpecial(-4163) # Paste values only
#
#         # Update the row counter
#         $row += $sourceRange.Rows.Count
#
#         # Close the source workbook without saving changes
#         $sourceWorkbook.Close($false)
#     }
# }
#
# # Save and close the output workbook
# $workbook.SaveAs($outputFile)
# $workbook.Close()
#
# # Quit Excel application
# $excel.Quit()
#
# Write-Host "Combined Excel file created at $outputFile"

# # Set the path to your main folder
# $mainFolder = "E:\git_folders\100-days-of-code\side_projects\excel_file_consolidation_project\main_folder"
#
# # Set the path to the new excel file
# $outputFile = "C:\users\nagaraj\file.xlsx"
#
# # Initialize a new Excel application
# $excel = New-Object -ComObject Excel.Application
# $excel.Visible = $false
# $excel.DisplayAlerts = $false
#
# # Create a new workbook
# $workbook = $excel.Workbooks.Add()
#
# # Loop through each sheet number
# for ($sheetNumber = 1; $sheetNumber -le 3; $sheetNumber++) {
#     # Initialize a counter to keep track of the row number for the current sheet
#     $row = 1
#
#     # Initialize a sheet for the current sheet number
#     $sheet = $workbook.Worksheets.Item($sheetNumber)
#
#     # Loop through each sub_folder in the main folder
#     Get-ChildItem -Path $mainFolder -Directory | ForEach-Object {
#         $subFolder = $_.FullName
#
#         # Loop through each Excel file in the sub_folder
#         Get-ChildItem -Path $subFolder -Filter *.xlsx | ForEach-Object {
#             $excelFile = $_.FullName
#
#             # Open the Excel file
#             $sourceWorkbook = $excel.Workbooks.Open($excelFile)
#
#             # Copy data from the current sheet of the Excel file to the output workbook
#             $sourceWorksheet = $sourceWorkbook.Sheets.Item($sheetNumber)
#             $sourceRange = $sourceWorksheet.UsedRange
#             $sourceRange.Copy()
#
#             # Paste data into the output workbook
#             $targetRange = $sheet.Cells.Item($row, 1)
#             $sheet.Paste($targetRange)
#
#             # Update the row counter
#             $row += $sourceRange.Rows.Count
#
#             # Close the source workbook without saving changes
#             $sourceWorkbook.Close($false)
#         }
#     }
# }
#
# # Save and close the output workbook
# $workbook.SaveAs($outputFile)
# $workbook.Close()
#
# # Quit Excel application
# $excel.Quit()
#
# Write-Host "Combined Excel file created at $outputFile"



#
# # Set the path to your main folder
# $mainFolder = "E:\git_folders\100-days-of-code\side_projects\excel_file_consolidation_project\main_folder"
#
# # Set the path to the new excel file
# $outputFile = "C:\users\nagaraj\file.xlsx"
#
# # Initialize a new Excel application
# $excel = New-Object -ComObject Excel.Application
# $excel.Visible = $false
# $excel.DisplayAlerts = $false
#
# # Create a new workbook
# $workbook = $excel.Workbooks.Add()
# $currentSheetNumber = 1
#
# # Loop through each sheet number
# for ($sheetNumber = 1; $sheetNumber -le 2; $sheetNumber++) {
#     # Initialize a sheet for the current sheet number
#     $sheet = $workbook.Worksheets.Item($sheetNumber)
#     Write-Host "excel file sheet value $sheet"
#     Write-Host "excel file Sheet number $sheetNumber"
#
#     # Initialize a counter to keep track of the row number for the current sheet
#     $row = 1
#
#     # Loop through each sub_folder in the main folder
#     Get-ChildItem -Path $mainFolder -Directory | ForEach-Object {
#         $subFolder = $_.FullName
#         Write-Host "Sub-folder: $subFolder"
#
#         # Loop through each Excel file in the sub_folder
#         Get-ChildItem -Path $subFolder -Filter *.xlsx | ForEach-Object {
#             $excelFile = $_.FullName
#             Write-Host "excelFile: $excelFile\n"
#
#             # Open the Excel file
#             $sourceWorkbook = $excel.Workbooks.Open($excelFile)
#             Write-Host "sourceWorkbook: $sourceWorkbook"
#
#             # Copy data from the current sheet of the Excel file to the output workbook
#             $sourceWorksheet = $sourceWorkbook.Sheets.Item($sheetNumber)
#             Write-Host "sourceWorksheet: $sourceWorksheet"
#             $sourceRange = $sourceWorksheet.UsedRange
#             Write-Host "sourceRange: $sourceRange"
#             $sourceRange.Copy()
#
#             # Paste data into the output workbook
#             $targetRange = $sheet.Cells.Item($row, 1)
#             Write-Host "targetRange: $targetRange"
#             $sheet.Paste($targetRange)
#
#             # Update the row counter
#             $row += $sourceRange.Rows.Count
#
#             # Close the source workbook without saving changes
#             $sourceWorkbook.Close($false)
#         }
#     }
#
# #     $currentSheetNumber++
# #     $sheet = $workbook.Worksheets.Item($currentSheetNumber)
#     $newSheet = $workbook.Sheets.Add()
#
#     # Set the name of the new sheet
#     $newSheet.Name = "Sheet$sheetNumber"
#
#     # Copy data from the current sheet of the Excel file to the output workbook
#     $sourceWorksheet = $sourceWorkbook.Sheets.Item($sheetNumber)
# #     $sourceRange = $sourceWorksheet.UsedRange
# #     $sourceRange.Copy()
#
#     # Paste data into the new sheet
#     $targetRange = $newSheet.Cells.Item(1, 1)
#     $newSheet.Paste($targetRange)
# }
#
# # Save and close the output workbook
# $workbook.SaveAs($outputFile)
# $workbook.Close()
#
# # Quit Excel application
# $excel.Quit()
#
# Write-Host "Combined Excel file created at $outputFile"




# for ($sheetNumber = 1; $sheetNumber -le $sourceWorkbook.Sheets.Count; $sheetNumber++) {
#             # Create a new sheet in the output workbook for each sheet in the source workbook
#             $newSheet = $workbook.Sheets.Add()
#
#             # Set the name of the new sheet
#             $newSheet.Name = "Sheet$sheetNumber"
#
#             # Copy data from the current sheet of the Excel file to the output workbook
#             $sourceWorksheet = $sourceWorkbook.Sheets.Item($sheetNumber)
#             $sourceRange = $sourceWorksheet.UsedRange
#             $sourceRange.Copy()
#
#             # Paste data into the new sheet
#             $targetRange = $newSheet.Cells.Item(1, 1)
#             $newSheet.Paste($targetRange)
#         }
#
#





#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# # 4th one from the GPT
#
# # Set the path to your main folder
# $mainFolder = "C:\path\to\main\folder"
#
# # Set the path to the new excel file
# $outputFile = "C:\path\to\output\file.xlsx"
#
# # Initialize a new Excel application
# $excel = New-Object -ComObject Excel.Application
# $excel.Visible = $false
# $excel.DisplayAlerts = $false
#
# # Create a new workbook
# $workbook = $excel.Workbooks.Add()
#
# # Initialize the current sheet number
# $currentSheetNumber = 1
#
# # Loop through each sub_folder in the main folder
# Get-ChildItem -Path $mainFolder -Directory | ForEach-Object {
#     $subFolder = $_.FullName
#
#     # Initialize a counter to keep track of the row number for the current sheet
#     $row = 1
#
#     # Loop through each Excel file in the sub_folder
#     Get-ChildItem -Path $subFolder -Filter *.xlsx | ForEach-Object {
#         $excelFile = $_.FullName
#
#         # Open the Excel file
#         $sourceWorkbook = $excel.Workbooks.Open($excelFile)
#
#         # Get the number of sheets in the source workbook
#         $sheetCount = $sourceWorkbook.Sheets.Count
#
#         # Loop through each sheet in the source workbook
#         for ($sheetNumber = 1; $sheetNumber -le $sheetCount; $sheetNumber++) {
#             # Initialize a sheet for the current sheet number
#             $sheet = $workbook.Worksheets.Item($currentSheetNumber)
#
#             # Copy data from the current sheet of the Excel file to the output workbook
#             $sourceWorksheet = $sourceWorkbook.Sheets.Item($sheetNumber)
#             $sourceRange = $sourceWorksheet.UsedRange
#             $sourceRange.Copy()
#
#             # Paste data into the output workbook
#             $targetRange = $sheet.Cells.Item($row, 1)
#             $sheet.Paste($targetRange)
#
#             # Update the row counter
#             $row += $sourceRange.Rows.Count
#
#             # If it's not the last sheet, move to the next sheet in the output workbook
#             if ($sheetNumber -lt $sheetCount) {
#                 $currentSheetNumber++
#                 $sheet = $workbook.Worksheets.Item($currentSheetNumber)
#             }
#         }
#
#         # Close the source workbook without saving changes
#         $sourceWorkbook.Close($false)
#     }
# }
#
# # Save and close the output workbook
# $workbook.SaveAs($outputFile)
# $workbook.Close()
#
# # Quit Excel application
# $excel.Quit()
#
# Write-Host "Combined Excel file created at $outputFile"


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# # 5th one from the GPT
#
# # Set the path to your main folder
# $mainFolder = "E:\git_folders\100-days-of-code\side_projects\excel_file_consolidation_project\main_folder"
#
# # Set the path to the new excel file
# $outputFile = "C:\users\nagaraj\file.xlsx"
#
#
# # Create a new Excel application
# $excel = New-Object -ComObject Excel.Application
# $excel.Visible = $false
# $excel.DisplayAlerts = $false
#
# # Create a new workbook
# $workbook = $excel.Workbooks.Add()
#
# # Loop through each sheet number
# for ($sheetNumber = 1; $sheetNumber -le 2; $sheetNumber++) {
#     # Initialize an array to hold data for the current sheet
#     $sheetData = @()
#
#     # Loop through each sub_folder in the main folder
#     Get-ChildItem -Path $mainFolder -Directory | ForEach-Object {
#         $subFolder = $_.FullName
#
#         # Loop through each Excel file in the sub_folder
#         Get-ChildItem -Path $subFolder -Filter *.xlsx | ForEach-Object {
#             $excelFile = $_.FullName
#
#             # Open the Excel file
#             $sourceWorkbook = $excel.Workbooks.Open($excelFile)
#
#             # Get data from the current sheet of the Excel file
#             $sourceWorksheet = $sourceWorkbook.Sheets.Item($sheetNumber)
#             $sourceRange = $sourceWorksheet.UsedRange
#             $data = $sourceRange.Value
#
#             # Append data to the sheet data array
#             $sheetData += $data
#
#             # Close the source workbook without saving changes
#             $sourceWorkbook.Close($false)
#         }
#     }
#
#     # Get the sheet object in the output workbook
#     $outputSheet = $workbook.Sheets.Item($sheetNumber)
#
#     # Write data to the output sheet
#     $outputRange = $outputSheet.Range("A1").Resize($sheetData.GetLength(0), $sheetData.GetLength(1))
#     $outputRange.Value = $sheetData
# }
#
# # Save the output workbook
# $workbook.SaveAs($outputFile)
#
# # Close the output workbook
# $workbook.Close()
#
# # Quit Excel application
# $excel.Quit()
#
# Write-Host "Combined Excel file created at $outputFile"


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# # 6th one from the GPT
#
#
# # Set the path to your main folder
# $mainFolder = "E:\git_folders\100-days-of-code\side_projects\excel_file_consolidation_project\main_folder"
#
# # Set the path to the new excel file
# $outputFile = "C:\users\nagaraj\file.xlsx"
#
# # Initialize a new Excel application
# $excel = New-Object -ComObject Excel.Application
# $excel.Visible = $false
# $excel.DisplayAlerts = $false
#
# # Create a new workbook
# $workbook = $excel.Workbooks.Add()
#
# # Loop through each sheet number
# for ($sheetNumber = 1; $sheetNumber -le 3; $sheetNumber++) {
#     # Initialize a new sheet for the current sheet number
#     $newSheet = $workbook.Sheets.Add()
#     $newSheet.Name = "Sheet$sheetNumber"
#
#     # Initialize a counter to keep track of the row number for the current sheet
#     $row = 1
#
#     # Loop through each sub_folder in the main folder
#     Get-ChildItem -Path $mainFolder -Directory | ForEach-Object {
#         $subFolder = $_.FullName
#
#         # Loop through each Excel file in the sub_folder
#         Get-ChildItem -Path $subFolder -Filter *.xlsx | ForEach-Object {
#             $excelFile = $_.FullName
#
#             # Open the Excel file
#             $sourceWorkbook = $excel.Workbooks.Open($excelFile)
#
#             # Copy data from the current sheet of the Excel file to the output workbook
#             $sourceWorksheet = $sourceWorkbook.Sheets.Item($sheetNumber)
#             $sourceRange = $sourceWorksheet.UsedRange
#             $sourceRange.Copy()
#
#             # Paste data into the new sheet
#             $targetRange = $newSheet.Cells.Item($row, 1)
#             $newSheet.Paste($targetRange)
#
#             # Update the row counter
#             $row += $sourceRange.Rows.Count
#
#             # Close the source workbook without saving changes
#             $sourceWorkbook.Close($false)
#         }
#     }
# }
#
# # Save and close the output workbook
# $workbook.SaveAs($outputFile)
# $workbook.Close()
#
# # Quit Excel application
# $excel.Quit()
#
# Write-Host "Combined Excel file created at $outputFile"



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# # 7th one from the GPT
#

# Set the path to your main folder
$mainFolder = "E:\git_folders\100-days-of-code\side_projects\excel_file_consolidation_project\main_folder"

# Set the path to the new excel file
$outputFile = "C:\users\nagaraj\file.xlsx"

# Initialize a new Excel application
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# Create a new workbook
$workbook = $excel.Workbooks.Add()

# Loop through each sheet number
for ($sheetNumber = 1; $sheetNumber -le 3; $sheetNumber++) {
    # Initialize a new sheet for the current sheet number
    if ($sheetNumber -gt 1) {
        $newSheet = $workbook.Sheets.Add()
        $newSheet.Name = "Sheet$sheetNumber"
    }

    # Initialize a counter to keep track of the row number for the current sheet
    $row = 1

    # Loop through each sub-folder in the main folder
    Get-ChildItem -Path $mainFolder -Directory | ForEach-Object {
        $subFolder = $_.FullName

        # Loop through each Excel file in the sub-folder
        Get-ChildItem -Path $subFolder -Filter *.xlsx | ForEach-Object {
            $excelFile = $_.FullName

            # Open the Excel file
            $sourceWorkbook = $excel.Workbooks.Open($excelFile)

            # Copy data from the current sheet of the Excel file to the output workbook
            $sourceWorksheet = $sourceWorkbook.Sheets.Item($sheetNumber)
            $sourceRange = $sourceWorksheet.UsedRange
            $sourceRange.Copy()

            # Paste data into the new sheet
            if ($sheetNumber -gt 1) {
                $targetRange = $newSheet.Cells.Item($row, 1)
                $newSheet.Paste($targetRange)
            } else {
                $targetRange = $workbook.ActiveSheet.Cells.Item($row, 1)
                $workbook.ActiveSheet.Paste($targetRange)
            }

            # Update the row counter
            $row += $sourceRange.Rows.Count

            # Close the source workbook without saving changes
            $sourceWorkbook.Close($false)
        }
    }
}

# Save and close the output workbook
$workbook.SaveAs($outputFile)
$workbook.Close()

# Quit Excel application
$excel.Quit()

Write-Host "Combined Excel file created at $outputFile"
