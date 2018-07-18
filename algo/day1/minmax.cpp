#include <iostream>
#include <vector>

using namespace std;

void minmax_recursive (int* a, int i, int j, int &min, int &max) {
  int lmin, lmax, rmin, rmax, mid;
  if (i == j) {
    min = a[i];
    max = a[j];
  } else if (j == i + 1) {
    if (a[i] > a[j]) {
      min = a[j];
      max = a[i];
    } else {
      min = a[i];
      max = a[j];
    }
  } else {
    mid = (i + j) / 2;
    minmax_recursive(a, i, mid, lmin, lmax);
    minmax_recursive(a, mid + 1, j, rmin, rmax);
    min = (lmin > rmin) ? rmin : lmin;
    max = (lmax > rmax) ? lmax : rmax;
  }
}

void minmax_iterative (int *a, int i, int j, int min, int max) {
  min = max = a[i];
  for (int k = i + 1; k <= j; k++) {
    if (a[k] > max) {
      max = a[k];
    } else if (a[k] < min) {
      min = a[k];
    }
  }
}

void tester (int *a, int size) {
  int min, max;
  minmax_recursive (a, 0, size, min, max);
  minmax_iterative (a, 0, size, min, max);
  printf ("%d -> Min = %d, Max = %d\n", size, min, max);
}

int random(int min, int max) {
  return rand() % (max - min) + min;
}

int main () {
  srand(time(0));
  const int size = random(10000, 100000);
  vector<int> same_elements(size, size);
  vector<int> incr_elements(size);
  vector<int> decr_elements(size);
  vector<int> rand_elements(size);
  incr_elements[0] = decr_elements[0] = rand_elements[0] = random(100000, 200000);
  for (int i = 1; i < size; i++) {
    incr_elements[i] = random(incr_elements[i - 1], incr_elements[i - 1] + 1000);
    decr_elements[i] = random(decr_elements[i - 1] - 1000, decr_elements[i - 1]);
    rand_elements[i] = rand();
  }
  tester(&same_elements[0], size);
  tester(&incr_elements[0], size);
  tester(&decr_elements[0], size);
  tester(&rand_elements[0], size);
  return 0;
}
