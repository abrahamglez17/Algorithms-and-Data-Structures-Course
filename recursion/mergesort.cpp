using namespace std;
include <iostream>;

// merge sort where input is nums1 and nums2 are int arr, m and n are the sizes of the arrays. nums1 has enough space to hold all elements and output should be in nums1

void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int i = m - 1, j = n - 1, k = m + n - 1;
    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    } 
    while (j >= 0) {
        nums1[k--] = nums2[j--];
    }
}


