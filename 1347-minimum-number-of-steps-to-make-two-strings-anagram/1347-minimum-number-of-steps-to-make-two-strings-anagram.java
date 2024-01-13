class Solution {
    public int minSteps(String s, String t) {
        int character[]=new int[26];
        for(int i=0;i<s.length();i++){
            character[t.charAt(i)-'a']++;
            character[s.charAt(i)-'a']--;
            
        }
        int ans=0;
        for(int j=0;j<26;j++){
            ans +=Math.max(0,character[j]);
        }
        return ans;
        
        
    }
}