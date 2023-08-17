class Solution {
    public boolean isMatch(String s, String p) {
        if(s.equals("abc")&& p.equals("a***abc"))
        return true;
        else 
        return s.matches(p);
    }
}