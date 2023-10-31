################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

class MagicalOven:

  def __init__(self, statusIngr = None):
    self._ingredients = []
    self._statusIngr = statusIngr
    

  def add(self, item):
    """
    input: str 'item'
    output: None

    adds a item to the ingredients
    """
    self._ingredients.append(item)

  
  def freeze(self):
    """
    input: None
    output: None

    set a freezed status to the ingredients
    """
    self._statusIngr = "freezed"
  

  def boil(self):
    """
    input: None
    output: None

    set a boiled status to the ingredients
    """

    self._statusIngr = "boiled"


  def wait(self):
    """
    input: None
    output: None

    set a ambient temperature status to the ingredients
    """

    self._statusIngr = "ambient temperature"


  def get_output(self):
    """
    input: None
    output: None

    returns a result of the status and the ingredients combination
    """

    # conditional statement in order to verificate status and ingredients
    if self._statusIngr == "freezed" and ("water" in self._ingredients  
                                          and "air" in self._ingredients):
      return "snow"
    
    elif self._statusIngr == "boiled" and ("lead" in self._ingredients  
                                           and "mercury" in self._ingredients):
      return "gold"
    
    elif self._statusIngr == "boiled" and ("cheese" in self._ingredients  
                                           and "dough" in self._ingredients 
                                           and "tomato" in self._ingredients):
      return "pizza"
    
    elif self._statusIngr == "ambient temperature" and ("water" in self._ingredients 
                                                        and "fruits" in self._ingredients):
      return "juice"


# This function should return an oven instance!
def make_oven():
  """
  input: None
  output: MagicalOven

  returns a instance of magical oven
  """
  
  return MagicalOven()

def alchemy_combine(oven, ingredients, temperature):
  """
  input: MagicalOven 'oven', list<str> 'ingredients', int 'temperature'
  output: str 'result of combination'

  returns a result of ingredients combination after entablish a status
  """
  
  # set ingredients in the oven
  for item in ingredients:
    oven.add(item)

  # conditional statement to entablish status according to temperature
  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()


  return oven.get_output()