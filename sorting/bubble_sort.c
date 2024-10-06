// Bubble sort
#include<stdio.h>
#include<conio.h>
int main()
{
    int i,j,t,n,a[50];
    printf("enterr the number:");
    scanf("%d",&n);
    printf("enter the array element:\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(a[j]>a[j+1])
            {
            t=a[j];
            a[j]=a[j+1];
            a[j+1]=t;
            }
        }
    }
    printf("after sorting:\n");
    for(i=0;i<n;i++)
    {
        printf("%d\t",a[i]);
    }

    return 0;
}
