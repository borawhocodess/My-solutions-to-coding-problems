#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    printf("\n");

    FILE *fp; // file pointer

    if(!strcmp(argv[1], "list")) // list choice
    {
        printf("TO DO LIST\n");

        fp = fopen("todo.txt","r");

        int c;

        if (fp) {
            while ((c = getc(fp)) != EOF)
                putchar(c);
        }
    }
    else if(!strcmp(argv[1], "add")) // add choice
    {
        fp = fopen("todo.txt","a");
        fprintf(fp, "%s\n", argv[2]);
        printf("ADDED ROW : %s\n", argv[2]);
    }
    else
    {
        printf("ARGV[1] is not defined : %s\n", argv[1]);
    }

    printf("\n");

    return 0;
}
