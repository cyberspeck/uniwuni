#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Berechnet das Endkapital für n Tage und dem Zinsatz z für 100 WE
   K_app: Kapital mit Umformung (1+x)**n = exp(n*ln(1+x/n))

*/
int main(int argc, char **argv){
int n=atof(argv[1]);
float z=atof(argv[2]),t;

double dz=atof(argv[2]),dt;

t= 100.*(pow((1.+z/n),n)-1.)/(z/n);
dt=100.*(pow((1.+dz/n),n)-1.)/(dz/n);

printf("Single: K=%.3f\n",t);


printf("Double: K=%.3f\n",dt);

}
