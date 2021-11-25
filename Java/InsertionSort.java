class InsertionSort{
    public static void main(String[] args){
        int A[]={12,3,21,65,71,2,95,5};
        Algo b= new Algo();
        b.Algo(A);
        b.out(A);
        
    }
}

class Algo{
    public void Algo(int[] A){
        for(int i=1;i<A.length;i++){
            int key=A[i];
             int j=i-1;
             while (j>=0 && A[j]>key){
                 A[j+1]=A[j];
                 j=j-1;
                 A[j+1]=key;
             }
         }

    }
    public void out(int[] A){
        for(int i=0;i<=A.length-1;i++){
            System.out.print(A[i]+" ");
        }
    }
}