/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (nums[nums[i] - 1] == i + 1) {
            count++;
        }
    }
    cout << count / 2 << endl;
    return 0;
}
