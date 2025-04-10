# Python 非同步 HTTP 客戶端

這是一個使用 `aiohttp` 開發的非同步 HTTP 客戶端，支援多種 HTTP 請求方法和並發處理。

## 功能特點

- 支援所有 HTTP 方法（GET、POST、PUT、DELETE 等）
- 非同步處理，高效能並發請求
- 自動會話管理
- 完整的錯誤處理
- 支援自定義請求頭和參數
- 支援 JSON 數據傳輸

## 安裝需求

```bash
pip install aiohttp
```

## 使用方法

### 基本 GET 請求

```python
async with APIClient() as client:
    result = await client.request(
        method="GET",
        endpoint="https://api.example.com/data"
    )
```

### 帶參數的 POST 請求

```python
async with APIClient("https://api.example.com") as client:
    result = await client.request(
        method="POST",
        endpoint="/api/data",
        headers={"Content-Type": "application/json"},
        json_data={"key": "value"}
    )
```

### 並發請求

```python
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
```

## 參數說明

- `method`: HTTP 請求方法（GET、POST、PUT、DELETE 等）
- `endpoint`: API 端點 URL
- `headers`: 可選的請求頭字典
- `params`: 可選的 URL 參數字典
- `json_data`: 可選的 JSON 數據字典

## 錯誤處理

客戶端會自動處理以下錯誤：
- HTTP 請求錯誤
- 網路連接錯誤
- 其他未預期的錯誤

所有錯誤都會返回包含錯誤信息的字典。

## 範例代碼

完整的範例代碼可以在 `main.py` 中找到，包含了三種不同的使用場景：
1. 簡單的 GET 請求
2. 帶參數的 POST 請求
3. 並發請求處理

## 注意事項

- 使用時必須使用 `async with` 上下文管理器
- 確保正確處理非同步操作
- 建議在生產環境中添加適當的錯誤處理和重試機制

## 授權

MIT License
