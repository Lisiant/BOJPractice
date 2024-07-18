#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[]) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    stack<pair<int, int>> stk;
    vector<int> v;

    for (int i = 0; i < n; i++) {
        while (!stk.empty() && stk.top().second < arr[i]) {
            stk.pop();
        }
        if (stk.empty()) {
            v.push_back(0);
            stk.push(make_pair(i + 1, arr[i]));
        } else {
            v.push_back(stk.top().first);
            stk.push(make_pair(i + 1, arr[i]));
        }
    }

    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << ' ';
    }

    return 0;
}
