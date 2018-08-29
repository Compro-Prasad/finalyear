#include <vector>
#include <iostream>

using namespace std;

class bst {
  pair<int, int> x;  // parent -> left or parent -> right
  bst *left, *right, *parent, *root;
public:
  bst () : left(nullptr),
           right(nullptr),
           parent(nullptr)
  {
  }
  void insert (pair<int, int> x)
  {
  }
};

int main() {
  int vertices, edges;
  cout << "Enter number of vertices: ";
  cin >> vertices;
  cout << "Enter number of edges: ";
  cin >> edges;
  vector<vector<int>> graph(vertices, vector<bool>(vertices, 0));
  vector<pair<int, int>> edge_list;
  cout << "Enter the edges:\n";
  for (int i = 0; i < edges; i++) {
    int x, y, distance;
    cin >> x >> y >> distance;
    edge_list.push_back(pair<int,int>(x, y));
    graph[x][y] = graph[y][x] = distance;
  }
  for (auto &i : graph) {
    for (auto j : i) {
      cout << j << ' ';
    }
    cout << endl;
  }
  for (auto &i : edge_list) {
    cout << i.first << " " << i.second << endl;
  }
  return 0;
}
