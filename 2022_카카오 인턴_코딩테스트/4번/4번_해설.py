# C++버전

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define NM 50005
using namespace std;
int N, M;
vector<pair<int, int>> con[NM];
int gateN, summitN;
int gates[NM], visit[NM], summits[NM], isSummit[NM];
void Input() {
    cin >> N >> M >> gateN >> summitN;
    for (int i = 1; i <= M; i++) {
        int x, y, c;
        cin >> x >> y >> c;
        con[x].push_back({ y, c });
        con[y].push_back({ x, c });
    }
    for (int i = 1; i <= gateN; i++) {
        cin >> gates[i];
    }
    for (int i = 1; i <= summitN; i++) {
        cin >> summits[i];
        isSummit[summits[i]] = 1;
    }
    sort(summits + 1, summits + 1 + summitN);
}
#include <queue>
void BFS(int S, int X) {
    queue<int> Q;
    Q.push(S);
    visit[S] = 1;
    while (!Q.empty()) {
        int x = Q.front(); Q.pop();
        if (isSummit[x]) continue;  // x 가 봉우리 중 하나라면, 그래프 탐색 종료
        for (auto& p : con[x]) {
            int y = p.first;
            int c = p.second;
            if (c > X) continue;  // 제한을 넘어가는 간선이면 무시하기
            if (visit[y]) continue;
            visit[y] = 1;
            Q.push(y);
        }
    }
}
int ansV = 1e9, ansSummit = 0;
bool check(int X) {
    // X 라는 제한 안에 갈 수 있는 봉우리가 존재하는가?
    for (int i = 1; i <= N; i++) visit[i] = 0;  // 방문체크 초기화
    for (int i = 1; i <= gateN; i++) {
        if (visit[gates[i]]) continue;
        BFS(gates[i], X);  // 출입구마다 연결요소 전부 찾기
    }
    for (int i = 1; i <= summitN; i++) {
        if (visit[summits[i]]) {  // 만약 어떤 봉우리를 갈 수 있다면!
            ansV = X;
            ansSummit = summits[i];
            return true;
        }
    }
    return false;
}
void Pro() {
    int L = 1, R = 10000000, mid;
    while (L <= R) {
        mid = (L + R) / 2;
        if (check(mid)) {
            R = mid - 1;
        }
        else {
            L = mid + 1;
        }
    }
    cout << ansSummit << " " << ansV;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    Input();
    Pro();
    return 0;
}



