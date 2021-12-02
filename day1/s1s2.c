#include <stdio.h>

//adventofcode - day 1

int main()
{
    int num1, num2, count = 0;
    
    FILE *fp1 = fopen("list.txt", "r");
    FILE *fp2 = fopen("list.txt", "r");
    
    if ((fp1 == NULL) || (fp2 == NULL))
    {
        printf("Error");
        return -1;
    }
    
    fprintf(fp1,"f");
    fprintf(fp2,"f");
    //fseek(fp2, 4, SEEK_SET);
    fseek(fp2, 13, SEEK_SET);
    
    //printf("%d %d", num1, num2);
    
    while (!feof(fp2))
    {
        fscanf(fp1, "%d", &num1);
        fscanf(fp2, "%d", &num2);
        if (num2-num1>0)
            count++;
        //printf("\n num1 - %d num 2 - %d count - %d", num1, num2, count);
        num1 = num2;
    }
    printf("\n%d", count);

    return 0;
}
