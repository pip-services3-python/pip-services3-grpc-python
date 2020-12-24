#!/usr/bin/env pwsh

##Set-StrictMode -Version latest
$ErrorActionPreference = "Stop"

# Get component data and set necessary variables
$component = Get-Content -Path "component.json" | ConvertFrom-Json

$docsImage="$($component.registry)/$($component.name):$($component.version)-$($component.build)-proto"
$container=$component.name

# Remove old generate files
if (Test-Path "$($component.name)/protos") {
    Remove-Item -Path "$($component.name)/protos/*" -Force -Include *.py -Exclude __init__.py
}

if (Test-Path "test/protos") {
    Remove-Item -Path "test/protos/*" -Force -Include *.py -Exclude __init__.py
}

# Build docker image
docker build --build-arg COMPONENT_NAME="$($component.name)" -f docker/Dockerfile.proto -t $docsImage .

# Create and copy compiled files, then destroy
docker create --name $container $docsImage
docker cp "$($container):/app/$($component.name)/protos" ./"$($component.name)"/
docker cp "$($container):/app/test/protos" ./test/
docker rm $container
