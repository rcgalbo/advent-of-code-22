from adventOfCode22.day1 import parse_data

# Sample data
ex_dat = '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''

def test_parse_data():
    assert parse_data(ex_dat) == [6000, 4000, 11000, 24000, 10000]

def test_max_parse_data():
    assert max(parse_data(ex_dat)) == 24000