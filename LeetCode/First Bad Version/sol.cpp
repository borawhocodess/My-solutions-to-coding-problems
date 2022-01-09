// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) 
    {  
        int l = 1;
        int r = n;
        
        while(l < r)
        {
            int m = l + (r - l) / 2; // WOW FOR OVERFLOW !!!

            if(!isBadVersion(m))
            {
                l = m + 1;
            }
            else if(isBadVersion(m))
            {
                r = m;
            }
        }
        return l;
    }
};
