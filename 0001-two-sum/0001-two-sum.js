/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let obj = {};
    for (let i = 0; i < nums.length; i++) {
        // console.log(obj)
        let diff = target - nums[i];
        if (diff in obj) {
            return [obj[diff], i];
        } else {
            obj[nums[i]] = i;
        }
    }
};