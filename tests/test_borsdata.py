from borsdata.borsdata_client import BorsdataClient

def test_borsdata():
    borsdata_client = BorsdataClient()
    instruments_with_kpi_2_data = borsdata_client.instruments_with_kpi_data(kpi=2, save_to_csv=True)
    instruments_with_kpi_3_data = borsdata_client.instruments_with_kpi_data(kpi=3, save_to_csv=True)
    instruments_with_meta_data = borsdata_client.instruments_with_meta_data()
    
    # 1. combine these dataframes
    # 2. filter out the instruments that have kpi 2 and 3 data
    # 3. filter out the instruments that have a specific country

    pass

    