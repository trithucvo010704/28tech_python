#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int last_pos(const vector<int> &a, int l, int r, int x)
{
    int res = -1;
    while (l <= r)
    {
        int m = (l + r) / 2;
        if (a[m] < x)
        {
            res = m;
            l = m + 1;
        }
        else
        {
            r = m - 1;
        }
    }
    return res;
}

int main()
{
    int n, k;
    cin >> n >> k;
    vector<int> a(n);

    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
    }

    int dem = 0;
    sort(a.begin(), a.end());

    for (int i = 0; i < n; ++i)
    {
        int p1 = last_pos(a, i + 1, n - 1, k - a[i]);
        if (p1 != -1)
        {
            dem += p1 - i;
        }
    }

    cout << dem << endl;

    return 0;
}