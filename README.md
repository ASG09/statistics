# statistics
A simple statistics project for small integers (bellow 1000):

the `DataCapture` class provide methods to add integers bellow 1000, to be queried with 3 comparisson methods (each of O(1)): 
 - `less(n)`: returns the amount of numbers added, bellow the given n integer (not inclusive);
 - `between(n,m)`: returns the amount of numbers added, between the given n and m integers (inclusive);
 - `greater(n)`: returns the amount of numbers added, greater than the given n integer (not inclusive);

## Installing dependencies:
To get pytest to run in your virtualenv, install the dependencies with either

`pip3 install pytest`

or 

`pip3 install -r requirements.txt`

## Usage:
Once cloned you can import the `DataCapture` class from `DataCapture.py` to instantiate data capturing objects, responsible for storing data with an `add` method. The object is also capable of returning a stats object, which contains methods to query the simple statistics information from the added data (less, between and greater):

```python
from DataCapture import DataCapture


capture = DataCapture()

# adding data:
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)

# generating the stats object:
stats = capture.build_stats()

# querying statistics information:
stats.less(4) # return 2 (only two values 3, 3 are less than 4)
stats.between(3, 6) # return 4 (3, 3, 4 and 6 are between 3 and 6)
stats.greater(4) # return 2 (6 and 9 are the only two values greater than 4)

```


## Runing tests:
Run on terminal inside the project's root folder:

`pytest -q TestDataCapture.py`