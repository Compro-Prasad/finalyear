#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int lecture_count;
  cout << "Enter number of lectures: ";
  cin >> lecture_count;
  cout << "Enter lecture intervals: ";
  vector<pair<int, pair<int, int>>> intervals(lecture_count);
  for (int i = 0; i < lecture_count; i++) {
    int start, end, priority;
    cin >> start >> end >> priority;
    intervals[i] = make_pair(priority, make_pair(start, end));
  }

  sort(intervals.rbegin(), intervals.rend());

  int end = 0;

  cout << "\nSelected lectures in the given class are:\n";

  for (int i = 0; i < intervals.size(); i++) {

    if (intervals[i].second.first >= end) {
      end = intervals[i].second.second;
      cout << intervals[i].second.first << ' '
           << intervals[i].second.second << endl;
    }

  }
  return 0;
}
