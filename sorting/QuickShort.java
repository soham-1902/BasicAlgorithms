import java.util.Arrays;

public  class QuickShort{
public static void quickshort(int arr[], int low, int high){
    if(low<high){
        int pi= parttion(arr, low, high);
        quickshort(arr,  low, pi-1);
        quickshort(arr, pi+1,high);
    }    
}

private static int parttion(int arr[], int low, int high){
	int pivot = arr[high];
	int i = (low-1);
	for(int k = low; k< high; k++){
        if(arr[k]<pivot){
            int temp = arr[i];
            arr[i]= arr[k];
            arr[k]=temp;
        }    
    }

    int temp = arr[i+1];
    arr[i+1] = arr[high];
    arr[high] = temp;
    return i+1;
}

public static void main(String[] args){
    int arr[]= { 54, 23, 21, 12, 34, 11, 9, 89, 80};
    quickshort(arr,0, arr.length -1);
    System.out.println("Shorted array is:" +Arrays.toString(arr));
    }
}
