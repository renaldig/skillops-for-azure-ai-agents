param(
    [Parameter(Mandatory = $true)] [string] $Subscription,
    [string] $ResourceGroup = "rg-skillops-ch3-sandbox",
    [string] $Location = "australiaeast"
)

$ErrorActionPreference = "Stop"
az account set --subscription $Subscription
az group create --name $ResourceGroup --location $Location --tags purpose=skillops-learning environment=sandbox
az group show --name $ResourceGroup --output table

Write-Host "Created or confirmed $ResourceGroup. This script creates only the resource group; it does not deploy paid resources."
