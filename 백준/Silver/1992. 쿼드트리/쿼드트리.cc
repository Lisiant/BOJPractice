#include <bits/stdc++.h>
using namespace std;

int graph[64][64];

bool check(int n, int x, int y) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (graph[x + i][y + j] != graph[x][y]) {
                return false;
            }
        }
    }
    return true;
}

void func(int n, int x, int y) {
    int half = n / 2;

    if (!check(n, x, y)) {
        cout << '(';
        func(half, x, y);
        func(half, x, y + half);
        func(half, x + half, y);
        func(half, x + half, y + half);
        cout << ')';
    } else {
        cout << graph[x][y];
        return;
    }
}

int main(int argc, char const *argv[]) {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++) {
            graph[i][j] = s[j] - '0';
        }
    }

    func(n, 0, 0);

    return 0;
}
