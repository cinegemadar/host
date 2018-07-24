#include "nav.h"

extern "C" {
  Nav* Nav_new() // C const wrapper
  {
    return new Nav();
  }

  int Nav_getGPSSignal(Nav* nav, int iDesired) // C getGPSSignal wrapper
  {
    return nav->getGPSSignal(iDesired);
  }

  void Nav_test(Nav* nav) // C test wrapper
  {
    nav->test();
  }
}
