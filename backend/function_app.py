import azure.functions as func
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="calculate")
def calculate(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        revenue = float(data.get("revenue", 0))
        cost = float(data.get("cost", 0))

        profit = revenue - cost

        return func.HttpResponse(
            json.dumps({"profit": profit}),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=400
        )
# comment
