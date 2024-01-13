import os
import requests
import tqdm
import zipfile

cookies = {
    'MicrosoftApplicationsTelemetryDeviceId': '5f6c01ce-f3b4-48ee-8eef-d66793c9885c',
    'MSFPC': 'GUID=4d82e13d68754e49b37e2e5f8dfbff26&HASH=4d82&LV=202309&V=4&LU=1694662803321',
    'PowerPointWacDataCenter': 'US4C',
    'WacDataCenter': 'US4C',
    'rtFa': '8Q1YeitV/x9V0m3Y/G1vm9VsbDE5KXerIw2DdGREVm0mMjA2ZjRjMDAtYWFiNS00MjEwLTgyMDQtZDA4NzdlMTMwMmVkIzEzMzQ5NTQ1NjQyMDIwMTQxNiMzNzA2MDFhMS02MDdiLTIwMDAtZDJhOC1mNjE4ZjBkZGIxYjcjMjE1MjI0MDclNDBtcy51aXQuZWR1LnZuIzE5NjE5MSN2dEdDYmVUR1BkaXNRS2VodkVzUEYtMWFNSkkyzP8q2R775HfIYO04zfCaUKz+9tA8VFIB+23HVafBji5NYH9hrfNsTvJsp4fszf02eSJV4+9CApiZ3vhKPUWtTz0yIaY6FYBiWYQnl3YJfZ+eYmra7H4tq6nSpvN8Wp6sLZfRdguMe1PAhHwNP34PS+bDBOd61g14PUu9FyTr7a2bgHQupTsAkkjpbOAxQxTH2osgeZsppyda9ZxGoZbCc4zd9kIhRYJO0c5ALanUz4fyWK/p105GRyjI9CO17qMnA1GU2Sk7Z514NX++lRc4WKHH5UfnE9wgInl7oW+0YIzVUg5H3zj+U8JPySeJq3q0Vf0xFBfxIFnh2lnD1c9PuQAAAA==',
    'SIMI': 'eyJzdCI6MH0=',
    'FedAuth': '77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U1A+VjEzLDBoLmZ8bWVtYmVyc2hpcHx1cm4lM2FzcG8lM2Fhbm9uIzVhMzNkMjQwM2M0OTFhYjQwNDcyMDY1NTA1NjQ0ZjZiOTFhMjRkZjhjYmNjZTA0ODkwMzYxYWFjODk5MGJhZjUsMCMuZnxtZW1iZXJzaGlwfHVybiUzYXNwbyUzYWFub24jNWEzM2QyNDAzYzQ5MWFiNDA0NzIwNjU1MDU2NDRmNmI5MWEyNGRmOGNiY2NlMDQ4OTAzNjFhYWM4OTkwYmFmNSwxMzM0OTU0NTkxNzAwMDAwMDAsMCwxMzM0OTY4NjIwNjAxMzY1NDYsMC4wLjAuMCwyNTgsMjA2ZjRjMDAtYWFiNS00MjEwLTgyMDQtZDA4NzdlMTMwMmVkLCwsMzEwNjAxYTEtZDA2NS0yMDAwLWQyYTgtZjMwYWUxZTg0YThhLGRmMzkwMWExLWUwMjItMjAwMC1kMmE4LWY1YTliYzFhZTU0Nyx5NGxvUWxSbk4wUzlDNFZjbWJLUGpnLDAsMCwwLCwsLDI2NTA0Njc3NDM5OTk5OTk5OTksMCwsLCwsLCwwLCwxOTYxOTEsR0FkeFdYM3FnLXBsUDRlOVhCUDF5MTZpZmpVLFNZdnVtbjlKUlFTUk5KRUUwUjFBeUZmbGxCMkd1VjZIK2drNnpMTTM5ZnRobUo0b1VwelVTbDBZQ1ZrOFM2UVZyWmZhTDNHTm9NVlFaNS9jN0VxYnJHMjhnRkxQOGw4MzRsc0M5MWZUMXdxN0d1eDNyKzRiS2UvNkRZeXh6cUVJMDczWWhyT3ZHL1BIOXd6UGltbExxclNna01rcFI4cGRqUHBjRnhKL2sxbU5ZeGNwbUg5emlvUUw4aStKQkErU21CMkFoTU55bnRSSVFsL2VaQ1Nrb0QzbEwrakcxYy9ZVVVTWm5uQm5EclJzL1RmNW42a0lUaW4yb0pnYUFxNS9zTjQ3djVic0RXV3pJTEdRdTNZczRIeTFrVytWN0Q1K2hJMHpFSWRxWk1NZGFFUGVUT1dkWktrdFE0aWlhaVE4YWdxZjBWUi9wSXJLWjRwQ3dZUFl3UT09PC9TUD4=',
    'ai_session': '7xe/nEgX4rHkzA8meMd27h|1705126206727|1705126206727',
}

headers = {
    'authority': 'uithcm-my.sharepoint.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'MicrosoftApplicationsTelemetryDeviceId=5f6c01ce-f3b4-48ee-8eef-d66793c9885c; MSFPC=GUID=4d82e13d68754e49b37e2e5f8dfbff26&HASH=4d82&LV=202309&V=4&LU=1694662803321; PowerPointWacDataCenter=US4C; WacDataCenter=US4C; rtFa=8Q1YeitV/x9V0m3Y/G1vm9VsbDE5KXerIw2DdGREVm0mMjA2ZjRjMDAtYWFiNS00MjEwLTgyMDQtZDA4NzdlMTMwMmVkIzEzMzQ5NTQ1NjQyMDIwMTQxNiMzNzA2MDFhMS02MDdiLTIwMDAtZDJhOC1mNjE4ZjBkZGIxYjcjMjE1MjI0MDclNDBtcy51aXQuZWR1LnZuIzE5NjE5MSN2dEdDYmVUR1BkaXNRS2VodkVzUEYtMWFNSkkyzP8q2R775HfIYO04zfCaUKz+9tA8VFIB+23HVafBji5NYH9hrfNsTvJsp4fszf02eSJV4+9CApiZ3vhKPUWtTz0yIaY6FYBiWYQnl3YJfZ+eYmra7H4tq6nSpvN8Wp6sLZfRdguMe1PAhHwNP34PS+bDBOd61g14PUu9FyTr7a2bgHQupTsAkkjpbOAxQxTH2osgeZsppyda9ZxGoZbCc4zd9kIhRYJO0c5ALanUz4fyWK/p105GRyjI9CO17qMnA1GU2Sk7Z514NX++lRc4WKHH5UfnE9wgInl7oW+0YIzVUg5H3zj+U8JPySeJq3q0Vf0xFBfxIFnh2lnD1c9PuQAAAA==; SIMI=eyJzdCI6MH0=; FedAuth=77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U1A+VjEzLDBoLmZ8bWVtYmVyc2hpcHx1cm4lM2FzcG8lM2Fhbm9uIzVhMzNkMjQwM2M0OTFhYjQwNDcyMDY1NTA1NjQ0ZjZiOTFhMjRkZjhjYmNjZTA0ODkwMzYxYWFjODk5MGJhZjUsMCMuZnxtZW1iZXJzaGlwfHVybiUzYXNwbyUzYWFub24jNWEzM2QyNDAzYzQ5MWFiNDA0NzIwNjU1MDU2NDRmNmI5MWEyNGRmOGNiY2NlMDQ4OTAzNjFhYWM4OTkwYmFmNSwxMzM0OTU0NTkxNzAwMDAwMDAsMCwxMzM0OTY4NjIwNjAxMzY1NDYsMC4wLjAuMCwyNTgsMjA2ZjRjMDAtYWFiNS00MjEwLTgyMDQtZDA4NzdlMTMwMmVkLCwsMzEwNjAxYTEtZDA2NS0yMDAwLWQyYTgtZjMwYWUxZTg0YThhLGRmMzkwMWExLWUwMjItMjAwMC1kMmE4LWY1YTliYzFhZTU0Nyx5NGxvUWxSbk4wUzlDNFZjbWJLUGpnLDAsMCwwLCwsLDI2NTA0Njc3NDM5OTk5OTk5OTksMCwsLCwsLCwwLCwxOTYxOTEsR0FkeFdYM3FnLXBsUDRlOVhCUDF5MTZpZmpVLFNZdnVtbjlKUlFTUk5KRUUwUjFBeUZmbGxCMkd1VjZIK2drNnpMTTM5ZnRobUo0b1VwelVTbDBZQ1ZrOFM2UVZyWmZhTDNHTm9NVlFaNS9jN0VxYnJHMjhnRkxQOGw4MzRsc0M5MWZUMXdxN0d1eDNyKzRiS2UvNkRZeXh6cUVJMDczWWhyT3ZHL1BIOXd6UGltbExxclNna01rcFI4cGRqUHBjRnhKL2sxbU5ZeGNwbUg5emlvUUw4aStKQkErU21CMkFoTU55bnRSSVFsL2VaQ1Nrb0QzbEwrakcxYy9ZVVVTWm5uQm5EclJzL1RmNW42a0lUaW4yb0pnYUFxNS9zTjQ3djVic0RXV3pJTEdRdTNZczRIeTFrVytWN0Q1K2hJMHpFSWRxWk1NZGFFUGVUT1dkWktrdFE0aWlhaVE4YWdxZjBWUi9wSXJLWjRwQ3dZUFl3UT09PC9TUD4=; ai_session=7xe/nEgX4rHkzA8meMd27h|1705126206727|1705126206727',
    'referer': 'https://uithcm-my.sharepoint.com/personal/21522034_ms_uit_edu_vn/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F21522034%5Fms%5Fuit%5Fedu%5Fvn%2FDocuments%2Fmodel%2Ezip&parent=%2Fpersonal%2F21522034%5Fms%5Fuit%5Fedu%5Fvn%2FDocuments&ga=1',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'service-worker-navigation-preload': 'true',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
resp = requests.get(
    'https://uithcm-my.sharepoint.com/personal/21522034_ms_uit_edu_vn/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2F21522034%5Fms%5Fuit%5Fedu%5Fvn%2FDocuments%2Fmodel%2Ezip',
    cookies=cookies,
    headers=headers,
    stream=True)
total = int(resp.headers.get('content-length', 0))
with open('model.zip', 'wb') as file, tqdm.tqdm(
    desc='model.zip',
    total=total,
    unit='iB',
    unit_scale=True,
    unit_divisor=1024,
) as bar:
    for data in resp.iter_content(chunk_size=1024):
        size = file.write(data)
        bar.update(size)
with zipfile.ZipFile('model.zip', 'r') as zip_ref:
    zip_ref.extractall('')
os.remove("model.zip")
