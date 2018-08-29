#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int lecture_count;
  cout << "Enter number of lectures: ";
  cin >> lecture_count;
  cout << "Enter lecture intervals: ";
  vector<pair<int, int>> lecture_intervals(lecture_count);
  for (int i = 0; i < lecture_count; i++) {
    int start, end;
    cin >> start >> end;
    lecture_intervals[i] = pair<int, int>(end, start);
  }

  sort(lecture_intervals.begin(), lecture_intervals.end());

  int end = 0;

  cout << "\nSelected lectures in the given class are:\n";

  for (int i = 0; i < lecture_intervals.size(); i++) {

    if (lecture_intervals[i].second >= end) {
      end = lecture_intervals[i].first;
      cout << lecture_intervals[i].second << ' '
           << lecture_intervals[i].first << endl;
    }

  }
  return 0;
}
