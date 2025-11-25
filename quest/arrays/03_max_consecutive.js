/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    var ones = 0;
    var tmp = 0;

    for (i = 0; i < nums.length; i++) {
        if (nums[i] == 1) {
            tmp += 1;

            if (tmp > ones) {
                ones = tmp;
            }
        } else {
            tmp = 0;
        }
    }

    return ones;
};
