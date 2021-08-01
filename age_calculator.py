# Import the following modules
from dateutil.relativedelta import relativedelta
from datetime import datetime
from time import strptime
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import time
  
# Run infinite loop
while True:  
    clear() 
      
    # Put a heading Age Calculator
    put_html("<p align=""left""><h4> AGE CALCULATOR</h4></p>
")
      
    # Getting Current time.
    date = datetime.now().strftime("%d/%m/%Y")  
      
    # Taking age from the user
    DOB = input("", placeholder="Your Birth Date(dd/mm/yyyy)")
    try:
        
        # Check whether the input age
        # format is same as given format
        val = strptime(DOB, "%d/%m/%Y")
    except:
        
        # If format is different, then through an error.
        put_error("Alert! This is not the right format")
          
        # sleep for 3 seconds
        time.sleep(3)  
        continue
    in_date = DOB.split('/') 
    date = date.split('/')  
      
    # Typecast all the converted part into the int.
    in_date = [int(i) for i in in_date]
    date = [int(i) for i in date]
      
    # Define an empty list
    newdate = []  
      
    # Swap days with years
    in_date[0], in_date[2] = in_date[2], in_date[0]  
      
    # Swap days with years
    date[0], date[2] = date[2], date[0]  
    if in_date <= date:
        now = datetime.strptime(DOB, "%d/%m/%Y")
          
        # Display output
        popup("Your Age",
              [put_html("<h4>"f"{relativedelta(datetime.now(),now).years} Years</br> \
              {relativedelta(datetime.now(),now).months} Months</br>\
              {relativedelta(datetime.now(),now).days} Days""</h4>"), put_buttons(
                  ['Close'], onclick=lambda _: close_popup())], implicit_close=True)
    else:
        
        # If you input the year greater than current year
        put_warning(
            f"No result found, this is {date[0]}, and you can't be in {in_date[0]}.")
        time.sleep(3)
    clear()
    # Give user a choice
    choice = radio("Do you want to calculate again?",
                   options=['Yes', 'No'], required=True)
    if choice.lower() == 'yes':
        continue
    else:
        clear()
          
        # Show a toast notification
        toast("Thanks a lot!")  
        exit()
