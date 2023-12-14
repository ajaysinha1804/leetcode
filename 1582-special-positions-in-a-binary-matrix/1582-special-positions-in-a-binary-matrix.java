class Solution {
    public int numSpecial(int[][] mat) {
        int row=mat.length;
        int col=mat[0].length;
        int[] r=new int[row];
        int[] c=new int[col];
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(mat[i][j]==1){
                    r[i]++;
                    c[j]++;
                }
            }
        }
        int count=0;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(mat[i][j]==1 && r[i]==1 && c[j]==1){
                    count++;
                }
            }
        }
        return count;
        
    }
}