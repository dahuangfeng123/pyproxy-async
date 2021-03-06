from src.app.main import Config
from src.lib.helper import DataHelper


class IPData(DataHelper):
    ip: str = ''
    port: int = 0
    delay: float = 0.0
    http: bool = False
    https: bool = False
    rules: dict = {}
    score: float = Config.DEFAULT_SCORE

    @classmethod
    def with_str(cls, ip_str: str):
        from src.lib.func import str_to_ip
        ip, port = str_to_ip(ip_str)
        return cls(ip=ip, port=port)

    def to_str(self) -> str:
        return '%s:%d' % (self.ip, int(self.port))

    def available(self) -> bool:
        return self.http

    def to_http(self) -> str:
        return 'http://%s' % self.to_str()

    def to_https(self) -> str:
        return 'https://%s' % self.to_str()


class SiteData(DataHelper):
    name: str = ''
    key: str = ''
    pages: list = []
    enabled: bool = True
    use_proxy: bool = False
    page_interval: float = 1
    headers = {}

    def to_request(self, page) -> "SiteRequestData":
        request = SiteRequestData()
        request.url = page
        request.use_proxy = self.use_proxy
        return request


class SiteResponseData(DataHelper):
    ip: str
    port: str

    def to_str(self) -> str:
        return '%s:%d' % (self.ip, int(self.port))


class SiteRequestData(DataHelper):
    url: str = ''
    use_proxy: bool = False


class RuleData(DataHelper):
    enable: bool = True
    url: str = ''
    key: str = ''
    contains: str = ''

    def verify(self) -> bool:
        return self.url and self.key
