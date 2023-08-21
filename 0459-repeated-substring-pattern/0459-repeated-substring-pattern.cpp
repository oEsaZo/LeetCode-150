class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n = s.length();
        string str = "";
        for(int i = 0; i<n/2; i++){
            str += s[i];
            string check = "";
            for(int j = 0 ;j < n/str.length(); j++){
                check += str;
            }
            if(check == s){
                return true;
            }
        }
        return false;
    }
};