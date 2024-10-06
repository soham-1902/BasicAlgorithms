#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
int queue[20];
int front = -1, rear = -1;
int max;
void qinsert();
void qdelete();
void qtraverse();

int main()
{
    int ch;
    printf("Enter the maximum size of queue:\n");
    scanf("%d", &max);
    while (1)
    {
        printf("(-) 1 for qinsert \n (-) 2 for qdelete \n (-) 3 for qtraverse \n (-) 4 for exit program\n");
        printf("Enter your choice:\n");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            qinsert();
            break;

        case 2:
            qdelete();
            break;

        case 3:
            qtraverse();
            break;

        case 4:
            exit(0);

        default:
            printf("wrong choice");
            break;
        }
    }

    return 0;
}

void qinsert()
{
    int item;
    if (rear < max - 1)
    {
        printf("Enter the item:\n");
        scanf("%d", &item);
        if (rear == -1)
        {
            rear = front = 0;
        }
        else
        {
            rear = rear + 1;
        }
        queue[rear] = item;
    }
    else
    {
        printf("queue is full\n");
    }
}

void qdelete()
{
    int item;
    if (front != -1)
    {
        printf("Deleted item =%d\n", queue[front]);
        if (front == rear)
        {
            front = -1;
            rear = -1;
        }
        else
            front = front + 1;
    }
}
void qtraverse()
{
    int i;
    if (front != -1)
    {
        printf("item in queue\n");
        for (i = front; i <= rear; i++)
        {
            printf("%d\t", queue[i]);
        }
        printf("\n");
    }

    else
        printf("queue is underflow");
}
