from borsdata.borsdata_client import BorsdataClient

def test_borsdata():
    borsdata_client = BorsdataClient()
    shit = borsdata_client.instruments_with_meta_data()

def test_get_stocks_with_kpi():
    borsdata_client = BorsdataClient()
    shit = borsdata_client.get_stocks_with_kpi()
    