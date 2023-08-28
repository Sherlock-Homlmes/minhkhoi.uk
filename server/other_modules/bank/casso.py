# libraries
import aiohttp

# local
from all_env import CASSO_API_KEY


async def get_transaction_history() -> list:
    async with aiohttp.ClientSession() as session:
        casso_url = 'https://oauth.casso.vn/v2/transactions'
        headers = {
            'Authorization': f'Apikey {CASSO_API_KEY}'
        }
        params = {
            'page': 1,
            'pageSize': 10,
            'sort': "DESC",
        }
        response = await session.get(
            casso_url,
            headers=headers,
            params=params
        )
        data = await response.json()
        return data
