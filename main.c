#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int nums[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (nums[nums[i] - 1] == i + 1) {
            count++;
        }
    }
    printf("%d\n", count / 2);
    return 0;
}