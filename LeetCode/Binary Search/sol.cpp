class Solution {
public:
    
    // https://en.wikipedia.org/wiki/Binary_search_algorithm
    
    int search(vector<int>& nums, int target)
    {
        int l = 0;
        int r = nums.size() - 1;
        
        while(true)
        {
            if(l > r) // the search terminates as unsuccessful.
            {
                return -1;
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
