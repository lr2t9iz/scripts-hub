# Hello World (Discovery) -> Testing

Write-Host "hello_world"
$date = Get-Date
Write-Host $date

Write-Host "`n--- AV List ---"
Get-CimInstance -Namespace "root\SecurityCenter2" -ClassName AntiVirusProduct | Select-Object displayName, productState
