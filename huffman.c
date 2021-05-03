#include <stdio.h>
void swap(int *num1, int *num2)
{
    int temp = *num1;
    *num1 = *num2;
    *num2 = temp;
}
void swap_char(char *char1,char *char2)
{
    char temp=*char1;
    *char1=*char2;
    *char2=temp;
}
int partition(char character[], int arr[], int start, int end)
{
    int pivot = arr[end];
    int pindex = start;
    int i = start;

    for (i = start; i < end; i++)
    {
        if (arr[i] < pivot)
        {
            swap(&arr[i], &arr[pindex]);
            swap_char(&character[i], &character[pindex]);
            pindex++;
        }
    }
    swap(&arr[end], &arr[pindex]);
    swap_char(&character[end], &character[pindex]);
    return pindex;
}

void quicksort(char character[], int arr[], int start, int end)
{
    if (start < end)
    {
        int p = partition(character, arr, start, end);
        quicksort(character, arr, start, p - 1);
        quicksort(character, arr, p + 1, end);
    }
}
int frequency_calculator(char input_string[], char character[], int frequency[], int len)
{
    int i, j, count = 0, check;
    for (i = 0; i < len; i++)
    {
        check = 1;
        for (j = 0; j < count; j++)
        {
            if (input_string[i] == character[j])
            {
                frequency[j] += 1;
                check = 0;
            }
        }
        if (check)
        {
            character[count] = input_string[i];
            frequency[count] = 1;
            count++;
        }
    }
    quicksort(character,frequency,0,count-1);
    return count;
}
void print(char character[], int frequency[], int count)
{
    int i;
    printf("Character   frequency\n");
    for (i = 0; i < count; i++)
    {
        printf("%c\t\t%d\n", character[i], frequency[i]);
    }
}
void main()
{
    int len;
    printf("Enter the length of the string");
    scanf("%d", &len);
    char input_string[len];
    printf("Enter the String of length %d", len);
    scanf("%s", &input_string);

    char character[26];
    int frequency[26];
    int count = frequency_calculator(input_string, character, frequency, len);
    print(character, frequency, count);
}
