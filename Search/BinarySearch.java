import java.util.*;
public class BinarySearch{
    public static void main(String[] args) {
        int [] arr = {12, 13, 222, 45, 555 , 689, 90, 4, 38};
        int key = 90;
        int l=0;
        int h= arr.length-1;
        while(l<=h){
            int middle= (l+h)/2;
            if(key>arr[middle]){
                l= middle + 1;
            } else if(key < arr[middle]){
                h= middle - 1;
            }else{
                System.out.println(middle);
                return;
            }
        }
        System.out.println("not found"+key);
    }
}


