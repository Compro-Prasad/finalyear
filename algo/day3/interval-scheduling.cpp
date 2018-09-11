#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct Interval {
  int start, finish;
  int weight;
  static bool compare(const Interval &x, const Interval &y) {
    return x.finish < y.finish;
  }
};

int get_last_valid_pos(vector<Interval> &x, int pos) {
  for (int i = pos - 1; i >= 0; i--) {
    if (x[i].finish <= x[pos].start)
      return i;
  }
  return 0;
}

int find_max_in_interval(vector<Interval> &x, int pos) {
  if (pos == 0) return x[pos].weight;

  int with_current_weight = x[pos].weight;
  int without_current_weight = find_max_in_interval(x, pos - 1);

  int last_valid_pos = get_last_valid_pos(x, pos);
  if (last_valid_pos)
    with_current_weight += find_max_in_interval(x, last_valid_pos);

  if (with_current_weight < without_current_weight)
    cout << x[last_valid_pos].start << " " << x[last_valid_pos].finish
         << ": " << x[last_valid_pos].weight << endl;
  else
    cout << x[pos].start << " " << x[pos].finish
         << ": " << x[pos].weight << endl;

  return max(with_current_weight, without_current_weight);
}

int find_max(vector<Interval> &x) {
  if (x.size()) {
    sort(x.begin(), x.end(), Interval::compare);
    return find_max_in_interval(x, x.size() - 1);
  }
  return 0;
}

int main() {
  int lecture_count;
  cout << "Enter number of lectures: ";
  cin >> lecture_count;
  cout << "Enter lecture intervals: ";
  vector<Interval> lecture_intervals(lecture_count);
  for (int i = 0; i < lecture_count; i++) {
    int start, end, weight;
    cin >> start >> end >> weight;
    lecture_intervals[i] = Interval{start, end, weight};
  }

  for (int i = 0; i < lecture_count; i++) {
    Interval &x = lecture_intervals[i];
    cout << x.start << " " << x.finish << ": " << x.weight << endl;
  }

  cout << "Max profit: " << find_max(lecture_intervals) << endl;

  return 0;
}
