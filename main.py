"""
    This API has 1 POST and 1 GET endpoints:
    POST receives a json with poolId & poolValues; creates a new pool/update existing one.
    GET receives a json with poolId & percentile; returns the calculated quantile and number of values.
"""

from math import floor, ceil
from flask import Flask, request

app = Flask(__name__)
app.secret_key = "TEST_KEY"
pools = {}

def calculate_quantile(pool, percentile):
    """
        Calculate the percentile of a pool.
    """

    len_pool = len(pool)
    if len_pool == 0:
        return 0
    sorted_pool = sorted(pool)
    mid_point = (len_pool - 1) * (percentile/100)
    fl, cl = int(floor(mid_point)), int(ceil(mid_point))
    if fl == cl:
        return sorted_pool[fl]
    return sorted_pool[fl] * (cl - mid_point) + sorted_pool[cl] * (mid_point - fl)

@app.post("/api/pools")
def add_pool():
    """
        Add a new pool, or update an existing one.
    """

    try:
        status = "Pool appended."
        content = request.get_json()
        pool_id = content.get("poolId", None)
        if pool_id not in pools:
            pools[pool_id] = []
            status = "Pool inserted."
        cur_pool = pools[pool_id]
        cur_pool.extend(content.get("poolValues", []))
        return {"status": status}, 201
    except Exception:
        return {"error": "Malformed request."}, 400

@app.get("/api/pools")
def get_pools():
    """
        Return the calculated percentile of a pool.
    """

    try:
        content = request.get_json()
        pool_id = content.get("poolId", None)
        if pool_id not in pools:
            return {"error": "Pool not found"}, 404
        return {
            "quantile": calculate_quantile(pools[pool_id], content["percentile"]),
            "element_count": len(pools[pool_id])
        }, 200
    except Exception:
        return {"error": "Malformed request."}, 400

if __name__ == "__main__":
    app.run(debug=True)
