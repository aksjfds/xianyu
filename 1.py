import asyncio
import aiohttp
import json

# 构建请求数据
data = {
    "data": '{"itemId":"828150551587"}'
}

# 构建请求头
headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "mtop_partitioned_detect=1; _m_h5_tk=940cd421637797975e20d10c463e0092_1724670626926; _m_h5_tk_enc=4357fff3320ccafbe92eda50d0a4a6ec; isg=BPb2HgE-jI2C1HhprlxC0Pr3Ryz4FzpRu57a-WDf8ll0o5Y9yKQlY-pVv3_PCzJp",
    "origin": "https://www.goofish.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.goofish.com/",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
}

# 请求的URL
url = "https://h5api.m.goofish.com/h5/mtop.taobao.idle.pc.detail/1.0/?jsv=2.7.2&appKey=12574478&t=1724661279847&sign=210c1817acce27eecc363fd0e8091986&v=1.0&type=originaljson&accountSite=xianyu&dataType=json&timeout=20000&api=mtop.taobao.idle.pc.detail&sessionOption=AutoLoginOnly&spm_cnt=a21ybx.item.0.0&spm_pre=a21ybx.search.searchFeedList.1.6dd83da6q7ESZB&log_id=6dd83da6q7ESZB"

# 异步请求函数
async def fetch(session):
    async with session.post(url, headers=headers, data=data) as response:
        resp = await response.text()
        print(json.loads(resp).get('ret'))

# 主函数
async def main():
    arr = [None] * 1000
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session) for _ in arr]
        await asyncio.gather(*tasks)

# 运行异步主函数
if __name__ == "__main__":
    asyncio.run(main())
