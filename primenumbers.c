#include <stdio.h>
#include <stdlib.h>
int main(){

int i;
int num1;
int a; 
a=1; //asal
printf("Enter a number:\n");
scanf("%d", &num1);
for(i=2;i<num1;i++)
{
if(num1%i==0)
{
a=0; //asal değil
}
}
if (a==1)
{printf("prime");
}
else if (a==0)
{
    printf("not prime");
}
}
  


