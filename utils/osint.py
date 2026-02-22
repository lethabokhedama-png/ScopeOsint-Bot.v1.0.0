import os
from dotenv import load_dotenv
import requests

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")


def serp_search(query, num_results=5):
    if not SERPAPI_KEY:
        return {"results": []}

    try:
        url = "https://serpapi.com/search.json"

        params = {
            "q": query,
            "num": num_results,
            "api_key": SERPAPI_KEY
        }

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        results = []

        for item in data.get("organic_results", []):
            results.append({
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet")
            })

        return {"results": results}

    except Exception as e:
        return {"results": []}


def run_search(query, search_type):
    try:
        combined_results = []

        # 🔹 Local modules (optional)
        try:
            if search_type == "email":
                from search.email import search_email
                local = search_email(query)
                combined_results.extend(local.get("results", []))

            elif search_type == "username":
                from search.username import search_username
                local = search_username(query)
                combined_results.extend(local.get("results", []))

            elif search_type == "phone":
                from search.phone import search_phone
                local = search_phone(query)
                combined_results.extend(local.get("results", []))

            elif search_type == "url":
                from sources.archives import wayback_search
                local = wayback_search(query)
                combined_results.extend(local.get("results", []))

        except:
            pass  # ignore if local modules fail

        # 🔥 ALWAYS add Google results
        serp = serp_search(query)
        combined_results.extend(serp.get("results", []))

        return {
            "query": query,
            "type": search_type,
            "results": combined_results,
            "found": bool(combined_results)
        }

    except Exception as e:
        return {"error": str(e)}
