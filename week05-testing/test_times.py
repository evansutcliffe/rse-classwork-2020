
import times
# content of test_expectation.py
import pytest
from pytest import raises
#import raise


@pytest.mark.parametrize("test_input,expected", [
    
    # test no overlap
    ([times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
    times.time_range("2010-01-13 12:00:00", "2010-01-13 13:00:00")], []),

    # test multiple overlap
    ([times.time_range("2010-01-12 10:00:00", "2010-01-12 10:45:00", 2, 60),
    times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)], 
    [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),
    
    # test exact intervals
    ([times.time_range("2010-01-12 10:00:00", "2010-01-12 10:45:00"),
    times.time_range("2010-01-12 10:45:00", "2010-01-12 11:00:00")], 
    []),
    ])

def test_eval(test_input, expected):
    assert eval(test_input) == expected


def eval(input):
    result = times.compute_overlap_time(input[0], input[1])
    return result

def test_negative_input():
    with raises(ValueError) as err:
        times.time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
        err.match("Start time after end time")


    #result = times.compute_overlap_time(large, short)
    #expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    #assert result == expected

# @pytest.mark.parametrize("test_input,expected", 
# ("times.time_range('2010-01-12 10:00:00', '2010-01-12 11:00:00'), times.time_range('2010-01-13 12:00:00', '2010-01-13 13:00:00')"
# , []))

# def test_eval(test_input, expected):
#     assert times.compute_overlap_time(test_input) == expected

# def test_given_input():
#     large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#     #print(compute_overlap_time(large, short))
#     result = times.compute_overlap_time(large, short)
#     expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
#     assert result == expected


# def test_no_overlap():
#     large = times.time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
#     short = times.time_range("2010-01-13 12:00:00", "2010-01-13 13:00:00")
#     #print(compute_overlap_time(large, short))
#     result = times.compute_overlap_time(large, short)
#     #print(result)
#     expected = []
#     assert result == expected   

# def test_multiple_intervals():
#     interval1 = times.time_range("2010-01-12 10:00:00", "2010-01-12 10:45:00", 2, 60)
#     interval2 = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#     #print(interval1)
#     #print(interval2)
#     #print(times.compute_overlap_time(interval1, interval2))
#     result = times.compute_overlap_time(interval1, interval2)
#     expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
#     assert result == expected

# def test_exact_intervals():
#     interval1 = times.time_range("2010-01-12 10:00:00", "2010-01-12 10:45:00")
#     interval2 = times.time_range("2010-01-12 10:45:00", "2010-01-12 11:00:00")
#     #print(interval1)
#     #print(interval2)
#     #print(times.compute_overlap_time(interval1, interval2))
#     result = times.compute_overlap_time(interval1, interval2)
#     expected = []
#     assert result == expected