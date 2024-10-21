#include<stdio.h>
#include<stdlib.h>
int max,front=-1,rear=-1,lq[20];
int enqueue();
int dqueue();
int display();
int main()
{
    int ch,item;
    printf("Enter the maximum size of the queue:\n");
    scanf("%d",&max);
    while (1)
    {
        printf("\n(-_-) 1 for queue insert \n(-_-) 2 for queue delete \n(-_-) 3 for display queue \n(-_-) 4 for exit programme\n");
        printf("Enter your choice:\n");
        scanf("%d",&ch);
        switch (ch)
        {
        case 1:enqueue();
            break;

        case 2:dqueue();
            break;
        
        case 3:display();
            break;

        case 4:exit(0);    

        default:printf("You enter wrong choice\n");
            break;
        }
    }
    
}

int enqueue()
{
    int item;
    printf("Enter item:\n");
    scanf("%d",&item);
    if(front==-1 && rear==-1)
    {
        front=0;
    }
    
    if(rear+1==max)
        {
            printf("Queue is full");
        }
        else{
            rear=rear+1;
            lq[rear]=item;
        }
    }

int dqueue(){
    if(front==-1 && rear==-1)
    {
        printf("Queue is empty\n");
    }
    else{
        printf("Delete item=%d",lq[front]);
    if(front==rear)
        {
            front=rear=-1;
        }
        else{
        front=front+1;

        }
    }

    }
    
int display(){
    if(front==-1 && rear==-1)
    {
        printf("Queue is empty\n");
    }
    else{
        printf("Item in linear queue:\n");
        for(int i=front;i<=rear;i++)
        {
            printf("%d\t",lq[i]);
        }
        printf("\n");
    }
}