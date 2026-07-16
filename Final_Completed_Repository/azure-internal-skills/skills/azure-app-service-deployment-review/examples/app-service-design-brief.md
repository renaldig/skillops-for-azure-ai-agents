# App Service Deployment Design Brief

A team wants to deploy a .NET 8 API to Azure App Service. The API will connect to Azure SQL Database and Azure Storage. The initial plan stores connection strings in App Service application settings. The team has not yet configured managed identity, Key Vault references, deployment slots, health checks, or Application Insights. The target environment is production.
