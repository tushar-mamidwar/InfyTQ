#include<stdio.h>
int frequency_calculator(char input_string[],char character[],int frequency[],int len)
{
    int i,j,count=0,check;
    for(i=0;i<len;i++)
    {
        check=1;
        for(j=0;j<count;j++)
        {
            if(input_string[i]==character[j])
            {
                frequency[j]+=1;
                check=0;
            }
        }
        if(check)
        {
            character[count]=input_string[i];
            frequency[count]=1;
            count++;
        }
    }
    return count;
}
void print(char character[],int frequency[],int count)
{
    int i;
    printf("Character   frequency\n");
    for(i=0;i<count;i++)
    {
        printf("%c\t\t%d\n",character[i],frequency[i]);
    }
}
void main()
{
    int len;
    printf("Enter the length of the string");
    scanf("%d",&len);
    char input_string[len];
    printf("Enter the String of length %d",len);
    scanf("%s",&input_string);

    char character[26];
    int frequency[26];
    int count=frequency_calculator(input_string,character,frequency,len);
    print(character,frequency,count);
}
