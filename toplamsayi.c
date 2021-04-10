#include <stdio.h>
#include <stdlib.h>

int main(){
int i;
int j;
j=1;
char girdi[20];

printf("istediginiz kadar sayi girip entera basin: \n");
scanf("%[^\n]%*c", girdi);

   for(i=0;girdi[i]!='\0';i++)
{
if(girdi[i]==' ')
{j++; 
}
}
printf("%d kadar sayi girilmistir" ,j);
   

}