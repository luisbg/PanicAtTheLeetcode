/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    var ans = new Array(n * 2);
    for (i = 0; i < n; i++) {
        ans[i * 2] = nums[i];
        ans[(i * 2) + 1] = nums[i + n];
    }

    return ans;
};
