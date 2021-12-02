#include <stdio.h>

//adventofcode - day 2

int main()
{
    int hor = 0, dep = 0, count = 0;
    int aim = 0;
    
    FILE *fp1 = fopen("text.txt", "r");
    
    if (fp1 == NULL)
    {
        printf("Error");
        return -1;
    }
    
    fprintf(fp1,"f");
    
    while (!feof(fp1))
    {
        char dir[10];
        int unit;
        fscanf(fp1, "%s %d", dir,&unit);
        if (dir[0] == 'u')
            aim += unit;
        else if (dir[0] == 'd')
            aim -=unit;
        else if (dir[0] == 'f')
        {
            hor += unit;
            dep += unit*aim;
        }
        //printf("%s %d %d %d %d\n", dir, unit, aim, hor, dep);
    }
    printf("\n%d %d %d", hor, dep, (hor*dep));

    return 0;
}
