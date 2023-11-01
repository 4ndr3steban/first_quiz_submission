package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine, Drink {

  // class variable to store the inserted money 
  private static int quarter = 0;

  // variables to store drink name and if it is fizzy
  private String drinkName;
  private boolean fizzy;

  // Builder (mainly used for build Drinks)
  public VendingMachineImpl(String drinkName, boolean fizzy) {
    this.drinkName = drinkName;
    this.fizzy = fizzy;
  }

  // Builder (used for build VendingMachine)
  public VendingMachineImpl() {}
  
  public static VendingMachine getInstance() {

    // returns a instance of VendingMachine
    return new VendingMachineImpl();
  }

  @Override
  public void insertQuarter() {

    // aument the 'money inserted' in the 'quarter' variable
    VendingMachineImpl.quarter += 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {

    // conditional statement to validate the Drink name
    if (name == "ScottCola"){
      
      // conditional statement to validate if the money is enough
      if (VendingMachineImpl.quarter < 75) { throw new NotEnoughMoneyException(); }

      else if (VendingMachineImpl.quarter >= 75) {

        // reduce money and return a 'instance of the drink'
        quarter -= 75;
        Drink drink = new VendingMachineImpl(name, true);
        return drink;

      }
    } else if (name == "KarenTea") {
      // conditional statement to validate if the money is enough
      if (VendingMachineImpl.quarter < 100) { throw new NotEnoughMoneyException(); }

      else if (VendingMachineImpl.quarter >= 100) {
        // reduce money and return a 'instance of the drink'
        quarter -= 100;
        Drink drink = new VendingMachineImpl(name, false);
        return drink;

      }
    } else {
      // exception for unknow drinks
      throw new UnknownDrinkException();
    }

    return null;
  }

  @Override
  public String getName() {

    // returns name of an instance of the drink
    return drinkName;
  }

  @Override
  public boolean isFizzy() {
    
    // returns if an instance of the drink is fizzy
    return fizzy;
  }

}
