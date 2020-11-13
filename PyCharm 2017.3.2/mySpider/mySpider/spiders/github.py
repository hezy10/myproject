import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com']

    def parse(self, response):

        token = response.xpath("//input[@name='authenticity_token']/@value")

        url = 'https://github.com/session'
        fromdata = {
            'authenticity_token':token,
            'login':'hezy10',
            'password':'he',
            'Cookie':'_octo=GH1.1.213859777.1596501748; '
                     'logged_in=no; '
                     '_ga=GA1.2.2073382007.1596501764;'
                     ' _device_id=61b197f51ffc87b53be5b0c81c7f960e;'
                     ' tz=Asia%2FShanghai; has_recent_activity=1; '
                     '_gat=1; '
                     '_gh_sess=acmHA3v%2FQxHUN9yETXT8lxR3eQ39fXVXyB5a'
                     'Yben2Uq8lQJ2ry6ezHUjQWQ1a6fciEBX3edmkRS4jP%2Bo0G'
                     'jodrHoyssHEi6OoK1dAppLDizF9HokY3QV%2BmeD%2B1i7xC'
                     '%2F8R0tGs%2BhHXoPkFQLJYe0PZxHmFgaSL3miQh6%2BQfUY'
                     'HoARPBwZxRgff4MVZobx08vn3PXRLt%2FlK5UAJDMOfwUho4'
                     'zeBG8qF%2BHBpilwAUXmE96KOwZiN0xHmfQG5Ma2AkxtgaZu'
                     'BcbJluav3thYnT3d5p088VOE6SImLmu%2Bn2HlrJzspMwAeA'
                     'YqSqsCcjoKjCP%2FIQu%2FH%2BIJ9NNIO9JimAf6SpAPBSlu'
                     '3Dl7VnRsOHwwicDHSCyrfClaW%2FkFOiF6pZ6w1YvrlTFLKc'
                     'C2R5cTMsb23xPJiNU8%2BhO0cSGntLLKcFmpCFkS5F3HyeCL'
                     'ChDbhtGFhDhDaH2laxGPTvI0xVjDXjeATTaUOyNo41qY6FKx'
                     'a4tzCbD4p4Z6DQHSJz3e6bhr5X%2FbYVaz3j5BT1iAO%2Btb'
                     'FoTEODtp1nqJk6vdWDrWewEJ%2FaVUWD2gEpzo0HuROtPSOs'
                     'jOXyYJ7sLlIiF%2F77YdagYozI%2FpVYLeIH4wyF9RxtAt6y'
                     '9Gzh3nZdeRhReg%2FHL5YCpLaoIegL8uidOy%2FQaTTI70Ci'
                     'j4bTLSnQ9XQ125Iy0e9vcZ8hspVwwbnyig%2FCywhuUbLY9G'
                     'yi3%2FQqvZawVjGFeWnxsSvdGHNAJeG%2F3VXT9a049ERlc8'
                     'NcmuLkfIysCA%2BZjwa2r4xeP%2FAs2ZFf4hLgYSK2C4KoRF'
                     'lFo4A3WaH7yauBJfJCPA4yY5I6KaIDVTnronGAmBnlfdn2P1'
                     'LhSO32RC35fA1cFnkyvXKIsc5b5PS6JAkAkj6KiLkuE2VP6Q'
                     '6ycCUaW%2B46Xhv4hozKbq1wBvCyj2PUvOA055AblasKZ0e10'
                     'B8Jc7dg%3D%3D--NMKRVr9eFHZW93jP--gPe8poUxxTPgCby'
                     'z%2Bq9MOw%3D%3D'
        }
        yield scrapy.Request(url=url,fromdata=fromdata,callback=self.handles_pase)
    def handles_pase(self,response):
        print(response.text)