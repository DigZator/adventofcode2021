#include <stdio.h>

int main()
{
    FILE *fp = fopen("input.txt", "r");
    
    if (fp == NULL)
    {
        printf("Error");
        return 0;
    }
    
    int sum[12] = {0};
    int count = 0;
    
    while(!feof(fp))
    {
        char text[12];
        fscanf(fp, "%s", text);
        //printf("%s\n", text);
        for (int i = 0; i < 12; i++)
            sum[i] += (text[i] - 48);
        count++;
    }
    
    int gam = 0, epi = 0;
    
    for (int i = 0; i < 12; i++)
    {
        //printf("%d %d\n", sum[i], count);
        if (sum[i] - count/2 < 0)
        {
            epi = (epi*2) + 1;
            gam = (gam*2) + 0;
        }
        else if (sum[i] - count/2 >= 0)
        {
            epi = (epi*2) + 0;
            gam = (gam*2) + 1;
        }
    }
    printf("Gamma - %d\nEpsilon - %d", gam, epi);
    printf("\nPower Consumption - %d", (gam*epi));

    return 0;
}
