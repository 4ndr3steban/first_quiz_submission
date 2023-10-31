package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {

  public static VendingMachine getInstance() {
    
    return new VendingMachineImpl();
  }

  @Override
  public void insertQuarter() {

  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    return null;
  }

}
