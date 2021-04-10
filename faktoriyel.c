#include <stdio.h>
#include <stdlib.h>
int main(){
int i;
int num1;
int result=1;
printf("enter a number");
scanf("%d", &num1);
for(i=1; i<=num1; i++)
{ result=i*result;

}
printf("sonucunuz: %d", result);








}