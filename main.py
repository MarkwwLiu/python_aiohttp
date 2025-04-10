import aiohttp
import asyncio
import json
from typing import Dict, Any, Optional

class APIClient:
    def __init__(self, base_url: str = ""):
        self.base_url = base_url
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def request(
        self,
        method: str,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        if not self.session:
            raise RuntimeError("客戶端會話未初始化。請使用 'async with' 上下文管理器。")

        url = f"{self.base_url}{endpoint}"
        try:
            async with self.session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json_data
            ) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientError as e:
            print(f"請求錯誤: {e}")
            return {"error": str(e)}
        except Exception as e:
            print(f"未知錯誤: {e}")
            return {"error": str(e)}

async def main():
    # 範例 1: 簡單的 GET 請求
    async with APIClient() as client:
        result = await client.request(
            method="GET",
            endpoint="https://www.bitopro.com/ns/home"
        )
        print("GET 請求結果:", result)

    # 範例 2: 帶參數的 POST 請求
    async with APIClient("https://api.example.com") as client:
        result = await client.request(
            method="POST",
            endpoint="/api/data",
            headers={"Content-Type": "application/json"},
            json_data={"key": "value"}
        )
        print("POST 請求結果:", result)

    # 範例 3: 並發請求
    async with APIClient() as client:
        tasks = []
        for i in range(3):
            tasks.append(
                client.request(
                    method="GET",
                    endpoint=f"https://api.example.com/data/{i}"
                )
            )
        results = await asyncio.gather(*tasks)
        print("並發請求結果:", results)

if __name__ == '__main__':
    asyncio.run(main())
