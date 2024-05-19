#include <bits/stdc++.h>
using namespace std;
int cnt;
vector<pair<int, int>> v;

void hanoi(int a, int b, int n) {
    if (n == 0) return;

    hanoi(a, 6 - a - b, n - 1);
    v.push_back(make_pair(a, b));
    cnt++;
    hanoi(6 - a - b, b, n - 1);
}

int main(int argc, char const *argv[]) {
    int n;
    cin >> n;
    hanoi(1, 3, n);

    cout << cnt << '\n';
    for (int i = 0; i < v.size(); i++) {
        cout << v[i].first << ' ' << v[i].second << '\n';
    }

    return 0;
}
