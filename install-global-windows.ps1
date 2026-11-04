$ErrorActionPreference = 'Stop'
$Source = Join-Path $PSScriptRoot '.claude\skills'
$Target = Join-Path $HOME '.claude\skills'
if (-not (Test-Path $Source)) { throw "Skills source not found: $Source" }
New-Item -ItemType Directory -Force -Path $Target | Out-Null
$copied = 0; $skipped = 0
Get-ChildItem -Directory $Source | ForEach-Object {
  $dest = Join-Path $Target $_.Name
  if (Test-Path $dest) { Write-Host "SKIP existing: $($_.Name)"; $skipped++ }
  else { Copy-Item -Recurse $_.FullName $dest; Write-Host "INSTALLED: $($_.Name)"; $copied++ }
}
Write-Host "Done. Installed=$copied Skipped=$skipped Target=$Target"
