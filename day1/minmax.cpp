#include <iostream>

using namespace std;

int main() {
    int n, x;
    int max = 1 << (sizeof(int) * 8);
    int min = 1 << (sizeof(int) * 8 - 1);
    cout << "Enter number of elements: ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        if (x > max) {
            max = x;
        }
        if (x < min) {
            min = x;
        }
    }
    return 0;
}
