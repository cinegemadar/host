#include <iostream>
#include "nav.h"


int Nav::getGPSSignal(int iDesired)
{
  return iDesired*30;
}

void Nav::test()
{
  std::cout<<"DLL loaded successfully..."<<std::endl;
}
