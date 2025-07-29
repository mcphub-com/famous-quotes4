import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/saicoder/api/famous-quotes4'

mcp = FastMCP('famous-quotes4')

@mcp.tool()
def get_random_quotes(category: Annotated[str, Field(description='')],
                      count: Annotated[Union[int, float], Field(description='Default: 2')]) -> dict: 
    '''Get multiple random quotes from chosen category or send **all** to get results from multiple categories. You can view all categories on the Category endpoint'''
    url = 'https://famous-quotes4.p.rapidapi.com/random'
    headers = {'x-rapidapi-host': 'famous-quotes4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'category': category,
        'count': count,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_categories() -> dict: 
    '''List all available categories'''
    url = 'https://famous-quotes4.p.rapidapi.com/'
    headers = {'x-rapidapi-host': 'famous-quotes4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
