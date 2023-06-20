class Solution {
    public int removeElement(int[] nums, int val) {
        int c=0;int k=0;
        int a[]=new int[nums.length];
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]!=val){
            a[k]=nums[i];
             k++;
            }
            else 
             c++;
        }
        for(int i=0;i<nums.length;i++)
        {
            if(i<a.length)
            {
                nums[i]=a[i];
            }
        }
        return nums.length-c;
    }
}