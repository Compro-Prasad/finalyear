#include <iostream>

using namespace std;

int main() {
    int n, x;
    int max, min;
    cout << "Enter number of elements: ";
    cin >> n;
    if (n < 1) {
        cout << "Invalid size\n";
        return 1;
    }
    cin >> x;
    min = max = x;
    for (int i = 1; i < n; i++) {
        cin >> x;
        if (x > max) {
            max = x;
        }
        else if (x < min) {
            min = x;
        }
    }
    return 0;
}
