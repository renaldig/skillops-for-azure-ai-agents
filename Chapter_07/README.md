# Chapter 7 supplementary files

Exercise 7-1 builds and tests the KQL diagnostics skill. Exercise 7-2 connects the observability skill to Azure Monitor through a read-only Azure MCP Server.

The `telemetry-sample` folder is an optional from-zero ASP.NET Core app for readers whose new Application Insights resource has no `AppRequests` data. Deploying and instrumenting the sample is not a replacement for following the chapter, but it supplies safe success, slow, and HTTP 500 request paths so the KQL can return meaningful rows.
