class Solution {
    public int minSteps(String s, String t) {
        int character[]=new int[26];
        for(char ch: s.toCharArray()){
            character[ch-'a']++;
        }
        int ans=0;
        for(char ch: t.toCharArray()){
            if(character[ch-'a']<=0){
                ans ++;
            }
            character[ch-'a']--;
        }
        return ans;
        
        
    }
}