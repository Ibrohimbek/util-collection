# Utils to use in projects. 


---

# Overview

I have collected some methods that I used in several services.   

----

# Requirements

* Python (3.*)

# Installation

Install using `pip`...

    pip install utilcollection


# Using in code

```python
from util_collection.string import split_by_cleaning

phone_numbers_str = "(508) 655-5350 326 , 508-903-5344,  800-533-2923 , 410-796-8899, "
phone_numbers_list = split_by_cleaning(phone_numbers_str)

# result: ['(508) 655-5350 326', '508-903-5344', '800-533-2923', '410-796-8899']
```
