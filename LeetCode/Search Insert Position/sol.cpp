class Solution {
public:
    int searchInsert(vector<int>& nums, int target)
    {  
        int l = 0;
        int r = nums.size() - 1;
        
        while(true)
        {
            if(l > r)
            {
                return l;
            }

            int m = (l + r) / 2;

            if(nums[m] < target)
            {
                l = m + 1;
            }
            else if(nums[m] > target)
            {
                r = m - 1;
            }
            else if(nums[m] == target)
            {
                return m;
            }
        } 
    }
};
