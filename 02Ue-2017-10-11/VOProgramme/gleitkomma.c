#include <stdio.h>
/* Zeigt das Bitmuster für die Darstellung nach IEEE 754
*/
union doub{double a; long unsigned v;};
union floa{ float a; unsigned v;};

print_bin_u(unsigned v) {
unsigned mask=0x80000000;
int i=1;
while (mask){
  if (v & mask)printf("1");
  else printf("0");
  if (i && !(i%4)) printf(" ");
  i++;
  mask/=2;
 }
}

void main(void)
{union doub d;
 union floa f;
 printf("double: %lu\n",sizeof(double));
 printf("long unsigned: %lu\n",sizeof(long unsigned));
 printf("float: %lu\n",sizeof(float));
 printf("unsigned: %lu\n",sizeof(unsigned));

 d.a=4711.0815;
 f.a=18.4;
 
 // mantisse= 0100 1100 1110 0010 1001 10.11101

 // exponent= 1000 1011
 // 0 100 0101 1010 0110 0111 0001 0100 110.11101
 printf("%f -> %0x -> ",f.a,f.v);
 print_bin_u(f.v);
 printf("\n");

 printf("%lf -> %0lx\n",d.a,d.v);
 
}
