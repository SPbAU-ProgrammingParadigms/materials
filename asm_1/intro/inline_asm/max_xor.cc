#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int solve(int l, int r) {
  if (l == r)
    return 0;
  int i;
  unsigned x = l ^ r;
  asm volatile("bsrl %1,%0" : "=r"(i) : "r"(x));
  return (1 << (i + 1)) - 1;
}

int main() {
  int l, r;
  cin >> l >> r;
  cout << solve(l, r) << endl;
  return 0;
}
