int main() {
 // Üç sınav bir proje notunu girilen öğrencinin ortalaması
 // ort < 50 --> ff
 // ort 50/60--> dd
 // ort 60/70--> cc
 // ort 70/85-->bb
 // ort> 85 -->aa
 
 int sayi1,sayi2,sayi3,proje,ort;
 
 printf("İlk notunuzu giriniz:");
 scanf("%d",&sayi1);
 
 printf("İkinci notunuzu giriniz:");
 scanf("%d",&sayi2);
 
 printf("Ücüncü notunuzu giriniz:");
 scanf("%d",&sayi3);
 
 printf("Proje notunuzu giriniz:");
 scanf("%d",&proje);
 
 ort=(sayi1+sayi2+sayi3+proje)/4;
 
 if(ort<50)
 {print("ff");
 }
 if(ort>50 && ort<60)
 {printf("dd");
 }
 if(ort>60 && ort<70)
 {printf("cc");
 }
 if(ort>70 && ort<85)
 {printf("bb");
 }
 if(ort>85)
 {printf("aa");
 } 
 
 
 
 
 
 
 
 
 
 return 0;
}