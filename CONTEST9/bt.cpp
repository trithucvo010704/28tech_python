#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// Hàm kiểm tra số nguyên tố
bool nt(int n)
{
    if (n < 2)
        return false;
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main()
{
    int n, m;
    // Nhập kích thước mảng
    cin >> n >> m;
    vector<vector<int>> a(n, vector<int>(m)); // Tạo mảng 2 chiều

    // Nhập các phần tử của mảng 2 chiều
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> a[i][j];
        }
    }

    // Duyệt qua mảng và in ra các số nguyên tố
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (nt(a[i][j]))
            {
                cout << a[i][j] << " ";
            }
        }
        cout << endl; // Xuống dòng sau mỗi hàng
    }

    return 0;
}
