![](http://ForTheBadge.com/images/badges/made-with-python.svg)
![](https://forthebadge.com/images/badges/built-by-developers.svg)</br>
[![Prettier](https://img.shields.io/badge/Code%20Style-Prettier-red.svg)](https://github.com/prettier/prettier)
![Size](https://img.shields.io/github/repo-size/Iamtripathisatyam/Age_Calculator_Web_App?color=red&label=Repo%20Size%20)
![](https://img.shields.io/tokei/lines/github/Iamtripathisatyam/Age_Calculator_Web_App?color=red&label=Lines%20of%20Code)</br>
![sds](https://profile-counter.glitch.me/{Age_Calculator_Web_App}/count.svg)


### Installation: 
```python
pip install pywebio
```

- Import all the required modules

  ```python
  from dateutil.relativedelta import relativedelta
  from datetime import datetime
  from time import strptime
  from pywebio.input import *
  from pywebio.output import *
  from pywebio.session import *
  import time
  ```
- Split the Birth Date of the user and the Current Date by '/'. And then typecast all the split parts into the integer. Swap months and years for both the user’s birth date and current date.
- Check whether or not the current year is smaller than the User's D.O.B year. If the current year is smaller than through an error.
