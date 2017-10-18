#include <stdio.h>
#include <stdlib.h>
/* Berechnet x**2 - y**2
             (x+y)*(x-y)
 fuer float und double
 Gute Testwerte:
 x=1.04, y=1.02
 x=1.004, y=1.002
 1.04 0.94
 1.04 0.93

*/
int main(int argc, char **argv){
float x=atof(argv[1]);
float y=atof(argv[2]);

double dx=atof(argv[1]);
double dy=atof(argv[2]);

printf("Single\n");
printf("x=%f, y=%f\n",x,y);
printf("x^2=%19.17f, y^2=%19.17f, x^2-y^2 =%19.17f\n",x*x, y*y, x*x-y*y);
printf("(x-y)= %19.17f, (x+y)= %19.17f (x-y)*(x+y)= %19.17f\n",x-y,x+y,(x-y)*(x+y));

printf("Double\n");
printf("x=%f, y=%f\n",dx,dy);
printf("x^2=%19.17f, y^2=%19.17f, x^2-y^2 =%19.17f\n",dx*dx, dy*dy, dx*dx-dy*dy);
printf("(x-y)= %19.17f (x+y)= %19.17f (x-y)*(x+y)= %19.17f\n",dx-dy,dx+dy,(dx-dy)*(dx+dy));

}
