from src.app.ip_get import IPGet, SiteResponse
from src.lib.structs import SiteData, SiteResponseData

key = 'spysme'


@IPGet.config(key)
def config():
    site = SiteData()
    site.name = 'Spys.me'
    site.pages = ['http://spys.me/proxy.txt']
    return site


@IPGet.parse(key)
def parse(resp: SiteResponse):
    import re
    ips = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}:\d+', resp.text)
    for ip in ips:
        try:
            item = ip.split(':')
            res = SiteResponseData()
            res.ip = item[0]
            res.port = item[1]
            yield res
        except Exception:
            continue


if __name__ == '__main__':
    from src.lib.func import run_until_complete

    runner = IPGet.test_crawl(key)
    run_until_complete(runner)
