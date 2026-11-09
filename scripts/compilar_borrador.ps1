$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$enginePath = Join-Path $projectRoot 'task/.tools/tectonic/tectonic.exe'
$sourceFolder = Join-Path $projectRoot '02_informe_tex'
$outputFolder = Join-Path $projectRoot 'task/borradores_internos'
$env:TECTONIC_CACHE_DIR = Join-Path $projectRoot 'task/.tools/tectonic/cache'
$env:FONTCONFIG_FILE = Join-Path $projectRoot 'task/.tools/tectonic/fonts.conf'
if (-not (Test-Path -LiteralPath $enginePath)) { throw 'Motor portátil LaTeX no disponible.' }
Push-Location -LiteralPath $sourceFolder
try {
    & $enginePath --untrusted --keep-logs --outdir $outputFolder 'W2608PRINF001_plantilla_original_borrador_v3.tex'
    if ($LASTEXITCODE -ne 0) { throw 'La compilación LaTeX no terminó correctamente.' }
} finally {
    Pop-Location
}
