/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function(nums) {
    var seen = new Array(nums.length).fill(0);
    var ans = new Array(2);

    for (i = 0; i < nums.length; i++) {
        seen[nums[i] - 1] += 1;
    }

    for (i = 0; i <= nums.length; i++) {
        if (seen[i] == 2) {
            ans[0] = i + 1;
        } else if (seen[i] == 0) {
            ans[1] = i + 1;
        }
    }

    return ans;
};
