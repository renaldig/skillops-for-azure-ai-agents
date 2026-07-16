using Azure.Monitor.OpenTelemetry.AspNetCore;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddOpenTelemetry().UseAzureMonitor();

var app = builder.Build();

app.MapGet("/", () => Results.Ok(new { status = "ok", service = "skillops-telemetry-api" }));
app.MapGet("/slow", async () =>
{
    await Task.Delay(1500);
    return Results.Ok(new { status = "slow-response-complete" });
});
app.MapGet("/fail", () => Results.Problem(
    title: "Intentional training failure",
    detail: "This endpoint returns HTTP 500 so AppRequests contains failed requests.",
    statusCode: StatusCodes.Status500InternalServerError));

app.Run();
