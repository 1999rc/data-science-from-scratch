from src.utils import normalize_data
def test_normalize_data():
    values=[0.5,10]
    normalized=normalize_data(values)
    assert min(normalized)==0.0 
    assert max(normalized)==1.0
    