param(
    [Parameter(Mandatory = $true)] [string] $AppUrl,
    [int] $Iterations = 10
)

$base = $AppUrl.TrimEnd('/')
1..$Iterations | ForEach-Object {
    Invoke-WebRequest "$base/" -UseBasicParsing | Out-Null
    Invoke-WebRequest "$base/slow" -UseBasicParsing | Out-Null
    try {
        Invoke-WebRequest "$base/fail" -UseBasicParsing | Out-Null
    } catch {
        Write-Host "Expected failure request sent: $($_.Exception.Response.StatusCode.value__)"
    }
}
