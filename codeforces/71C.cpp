#include <bits/stdc++.h>
using namespace std;

const int mxN=1e5;
int n, a[mxN];

void chk(int x) {
  for(int si=0; si<x; ++si) {
    bool ok=1;
    for(int j=si; j<n&ok; j+=x)
      ok=a[j];
      if(ok) {
        cout << "YES";
        exit(0);
      }
  }
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> n;
  for(int i=0; i<n; ++i)
    cin >> a[i];

  for(int i=1; i*i<=n; ++i) {
    if(n%i)
      continue;
    if (n/i>=3)
      chk(i);
    if (i>=3)
      chk(n/i);
  }
  cout << "NO";
}