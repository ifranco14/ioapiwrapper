import requests
from io_api_wrapper import settings


class IOBase:
    URL_ACCOUNT_STATE = "/api/v2/estadocuenta"
    URL_MARKET_RATES = "/api/v2/Cotizaciones/{instrument}/{panel}/{country}"
    URL_MUTUAL_FUND = "/api/v2/Titulos/FCI/{symbol}"
    URL_MUTUAL_FUND_IN_MARKET = "/api/v2/{market}/Titulos/{symbol}"
    URL_MUTUAL_FUND_OPTIONS = "/api/v2/{market}/Titulos/{symbol}/Opciones"
    URL_MUTUAL_FUNDS = "/api/v2/Titulos/FCI"
    URL_MUTUAL_FUNDS_ADMINS = "/api/v2/Titulos/FCI/Administradoras"
    URL_MUTUAL_FUNDS_BY_ADMIN_AND_TYPE = ("/api/v2/Titulos/FCI/Administradoras/{admin}/"
                                          "TipoFondos/{fcitype}")
    URL_MUTUAL_FUNDS_TYPES = "/api/v2/Titulos/FCI/TipoFondos"
    URL_MUTUAL_FUNDS_TYPES_BY_ADMIN = ("/api/v2/Titulos/FCI/Administradoras/"
                                      "{admin}/TipoFondos")
    URL_INSTRUMENT = ("/api/v2/{country}/Titulos/Cotizacion/"
                      "Paneles/{instrument}")
    URL_INSTRUMENTS = "/api/v2/{country}/Titulos/Cotizacion/Instrumentos"
    URL_OPERATE_BUY = "/api/v2/operar/Comprar"
    URL_OPERATE_SELL = "/api/v2/operar/Vender"
    URL_OPERATE_SUBSCRIBE = "/api/v2/operar/suscripcion/fci"
    URL_OPERATE_RESCUE = "/api/v2/operar/rescate/fci"
    URL_OPERATION = "/api/v2/operaciones/{number}"
    URL_OPERATIONS = "/api/v2/operaciones/"
    URL_OPERATIONS_DELETE = "/api/v2/operaciones/{number}"
    URL_PORTFOLIO = "/api/v2/portafolio/{country}"
    URL_STOCK = "/api/v2/{market}/Titulos/{symbol}/Cotizacion"
    URL_STOCK_HISTORY = ("/api/v2/{market}/Titulos/{symbol}/Cotizacion/"
                         "seriehistorica/{date_from}/{date_to}/{fit}")
    URL_TOKEN = "/token"


class IOWrapper(IOBase):
    def __init__(self):
        self.api = ""
        self.access_token = ""
        self.refresh_token = ""
        self.token_issued = ""
        self.token_expires = ""

    def _get_bearer_header(self):
        return {"Authorization": "Bearer " + self.access_token}

    def _store_token_info(self, response):
        self.access_token = response.get('access_token')
        self.refresh_token = response.get('refresh_token')
        self.token_issued = response.get('.issued')
        self.token_expires = response.get('.expires')

    def buy(self, market, symbol, amount, price, valid_date, term):
        payload = {
            "mercado": market,
            "simbolo": symbol,
            "cantidad": amount,
            "precio": price,
            "validez": valid_date,
            "plazo": term
        }

        url = self.api + self.URL_OPERATE_BUY

        response = requests.post(url, json=payload,
                                headers=self._get_bearer_header())

        return response.json()

    def delete_operation(self, number):
        url = self.api + self.URL_OPERATIONS_DELETE.format(number)

        response = requests.delete(url, headers=self._get_bearer_header())

        return response.json()

    def get_account_state(self):
        url = self.api + self.URL_ACCOUNT_STATE

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_instrument(self, country, instrument):
        url = self.api + self.URL_INSTRUMENT.format(country=country, instrument=instrument)

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_instruments(self, country):
        url = self.api + self.URL_INSTRUMENTS.format(country=country)

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_market_rates(self, instrument, panel, country):
        url = self.api + self.URL_MARKET_RATES.format(
            instrument=instrument, panel=panel, country=country)

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_mutual_fund(self, symbol):
        url = self.api + self.URL_MUTUAL_FUND.format(symbol=symbol)

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_mutual_fund_options(self, market, symbol):
        url = self.api + self.URL_MUTUAL_FUND_OPTIONS.format(
            market=market, symbol=symbol)

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_mutual_fund_in_market(self, market, symbol):
        url = self.api + self.URL_MUTUAL_FUND_IN_MARKET.format(
            market=market, symbol=symbol)

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_mutual_fund_types(self):
        url = self.api + self.URL_MUTUAL_FUNDS_TYPES

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_mutual_funds(self):
        url = self.api + self.URL_MUTUAL_FUNDS

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_mutual_fund_admins(self):
        url = self.api + self.URL_MUTUAL_FUNDS_ADMINS

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_mutual_fund_types_by_admin(self, admin):
        url = self.api + self.URL_MUTUAL_FUNDS_TYPES_BY_ADMIN.format(admin=admin)

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_mutual_fund_by_admin_and_type(self, admin, fcitype):
        url = self.api + self.URL_MUTUAL_FUNDS_BY_ADMIN_AND_TYPE.format(
            admin=admin, fcitype=fcitype)

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_portfolio(self, country):
        url = self.api + self.URL_PORTFOLIO.format(country=country)

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_operation(self, number):
        url = self.api + self.URL_OPERATION.format(number=number)

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_operations(self):
        url = self.api + self.URL_OPERATIONS

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_stock(self, market, symbol):
        url = self.api + self.URL_STOCK.format(market=market, symbol=symbol)

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_stock_history(self, market, symbol, date_from, date_to, fit):
        url = self.api + self.URL_STOCK_HISTORY.format(
            market=market, symbol=symbol, date_from=date_from,
            date_to=date_to, fit=fit)

        response = requests.get(url, headers=self._get_bearer_header())

        return response.json()

    def get_token(self, username=None, password=None,
                  refresh_token=None, grant_type="password"):

        payload = {}

        if grant_type == "password":

            if not username and not password:
                username = settings.USER
                password = settings.PWD

            payload = {
                "username": username,
                "password": password,
                "grant_type": grant_type
            }
        elif grant_type == "refresh_token":
            payload = {
                "refresh_token": refresh_token,
                "grant_type": grant_type
            }

        url = self.api + self.URL_TOKEN

        response = requests.post(url, data=payload)

        json_response = response.json()

        self._store_token_info(json_response)

        return json_response

    def rescue(self, symbol, amount, validate=None):
        payload = {
            "simbolo": symbol,
            "cantidad": amount,
            "soloValidar": validate
        }

        url = self.api + self.URL_OPERATE_RESCUE

        response = requests.post(url, json=payload,
                                 headers=self._get_bearer_header())
        return response.json()

    def sell(self, market, symbol, amount, price, valid_date, term=None):
        payload = {
            "mercado": market,
            "simbolo": symbol,
            "cantidad": amount,
            "precio": price,
            "validez": valid_date,
            "plazo": term
        }

        url = self.api + self.URL_OPERATE_SELL

        response = requests.post(url, json=payload,
                                 headers=self._get_bearer_header())

        return response.json()

    def subscribe(self, symbol, amount, validate):
        payload = {
            "simbolo": symbol,
            "cantidad": amount,
            "soloValidar": validate
        }

        url = self.api + self.URL_OPERATE_SUBSCRIBE

        response = requests.post(url, json=payload, headers=self._get_bearer_header())

        return response.json()


class IOService(IOWrapper):
    def __init__(self):
        super().__init__()
        self.api = "https://api.invertironline.com"
