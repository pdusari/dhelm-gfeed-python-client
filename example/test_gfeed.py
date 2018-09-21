from DhelmGfeedClient.gfeedclient import GfeedClient
from DhelmGfeedClient.constants import Constants
import json
import time
import datetime

def test_dhelm_gfeed_client():
    client = GfeedClient("ws://nimblestream.lisuns.com:4526/","f31b6d7d-0138-428d-93ef-28acbd9632d2")


    def on_authenticated(ws):
        ws.get_exchanges()
        ws.get_instruments_on_search("NSE", "SBIN")
        ws.get_instruments("NSE")
        ws.get_last_quote("NSE", "SBIN")
        ws.get_last_quotes_array("NSE", ["SBIN", "BEPL", "INFY"])
        ws.get_snapshot("NSE", ["SBIN", "BEPL", "INFY"])
        ws.get_instrument_types("NFO")
        ws.get_products("NFO", "FUTIDX")
        ws.get_expiry_dates("NFO", "FUTIDX", "NIFTY")
        ws.get_option_types("NFO", "FUTIDX", "NIFTY", "25OCT2018")
        ws.get_strike_prices("NFO", "FUTIDX", "NIFTY", "25OCT2018")
        ws.get_limitations()
        ws.get_market_message("NSE")
        ws.get_exchange_message("NSE")
        ws.subscribe_realtime("NSE", "SBIN")
        ws.subscribe_realtime_snapshot("NSE", "SBIN", Constants.MINUTE)
        ws.get_historical_tick_data("NSE", "SBIN", 10)
        ws.get_historical_ohlc_data("NSE", "SBIN", Constants.HOUR,
                                int(time.mktime((datetime.datetime(2018, 9, 13)).timetuple())),
                                int(time.mktime((datetime.datetime.now()).timetuple())), 10)


    def on_message_get_exchanges(list_exchanages):
        print("\n*********LIST OF EXCHANGES*************\n")
        response = (json.loads(list_exchanages))
        print(response)
        print("\n")
        print(response['Result'])



    def on_message_instruments_on_search(list_instruments):
        print("\n*********LIST OF INSTRUMENTS*************\n")
        print(list_instruments)


    def on_message_instruments(list_instruments):
        print("\n*********LIST OF INSTRUMENTS*************\n")
        print(list_instruments)


    def on_message_last_quote(last_quote):
        print("\n*********LAST QUOTE*************\n")
        print(last_quote)


    def on_message_last_quote_array(last_quote_array):
        print("\n*********LAST QUOTE ARRAY*************\n")
        print(last_quote_array)


    def on_message_snapshot_data(snapshot_data):
        print("\n*********SNAPSHOT DATA*************\n")
        print(snapshot_data)


    def on_message_instrument_types(instrument_types):
        print("\n*********INSTRUMENT TYPES*************\n")
        print(instrument_types)


    def on_message_products(products):
        print("\n*********PRODUCTS*************\n")
        print(products)


    def on_message_expiry_dates(expiry_dates):
        print("\n*********EXPIRY DATES*************\n")
        print(expiry_dates)


    def on_message_option_types(option_types):
        print("\n*********OPTION TYPES*************\n")
        print(option_types)


    def on_message_strike_prices(strike_prices):
        print("\n*********STRIKE PRICES*************\n")
        print(strike_prices)


    def on_message_account_limitations(account_limitations):
        print("\n*********ACCOUNT LIMITATIONS*************\n")
        print(account_limitations)


    def on_message_market_message(market_message):
        print("\n*********MARKET MESSAGE*************\n")
        print(market_message)


    def on_message_exchange_message(exchange_message):
        print("\n*********EXCHANGE MESSAGE*************\n")
        print(exchange_message)


    def on_message_realtime_data(realtime_data):
        print("\n*********REALTIME DATA*************\n")
        print(realtime_data)


    def on_message_realtime_snapshot_data(realtime_snapshot_data):
        print("\n*********REALTIME SNAPSHOT DATA*************\n")
        print(realtime_snapshot_data)


    def on_message_historical_tick_data(historical_tick_data):
        print("\n*********HISTORICAL TICK DATA*************\n")
        print(historical_tick_data)


    def on_message_historical_ohlc_data(historical_ohlc_data):
        print("\n*********HISTORICAL OHLC DATA*************\n")
        print(historical_ohlc_data)


    client.on_authenticated = on_authenticated
    client.on_message_get_exchanges = on_message_get_exchanges
    client.on_message_instruments_on_search = on_message_instruments_on_search
    client.on_message_instruments = on_message_instruments
    client.on_message_last_quote = on_message_last_quote
    client.on_message_last_quote_array = on_message_last_quote_array
    client.on_message_snapshot_data = on_message_snapshot_data
    client.on_message_historical_tick_data = on_message_historical_tick_data
    client.on_message_historical_ohlc_data = on_message_historical_ohlc_data
    client.on_message_instrument_types = on_message_instrument_types
    client.on_message_product = on_message_products
    client.on_message_expiry_dates = on_message_expiry_dates
    client.on_message_option_types = on_message_option_types
    client.on_message_strike_prices = on_message_strike_prices
    client.on_message_account_limitations = on_message_account_limitations
    client.on_message_market_message = on_message_market_message
    client.on_message_exchange_message = on_message_exchange_message
    client.on_message_realtime_data = on_message_realtime_data
    client.on_message_realtime_snapshot_data = on_message_realtime_snapshot_data
    client.connect()
