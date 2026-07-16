# Optional AppRequests Telemetry Sample

Use this sample only when you need a small non-production application to populate Application Insights request telemetry.

## Local test

```powershell
cd .\SkillOpsTelemetryApi
dotnet restore
dotnet run
```

Call `/`, `/slow`, and `/fail`. The failure endpoint intentionally returns HTTP 500 for diagnostic practice.

## Azure use

1. Create a non-production App Service and workspace-based Application Insights resource as described in Chapter 7.
2. Set the App Service application setting `APPLICATIONINSIGHTS_CONNECTION_STRING` to the Application Insights connection string, or enable recommended App Service automatic instrumentation.
3. Deploy this project.
4. Run `generate-traffic.ps1 -AppUrl https://<app-name>.azurewebsites.net`.
5. Query `AppRequests` after ingestion.

Do not expose the sample as a production application.
