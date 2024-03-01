#include <stdio.h>
#include <stdlib.h>

typedef struct _complex{
	float realpart;
	float imagepart;
}Complex;

void create( Complex* X, float real, float image ){
	X -> realpart = real;
	X -> imagepart = image;
}

void add( Complex* A, Complex* B, Complex* C ){
	C -> realpart = A -> realpart + B -> realpart;
	C -> imagepart = A -> imagepart + B -> imagepart;
}

void multiply( Complex* A, Complex* B, Complex *D ){
	D -> realpart = A -> realpart * B -> realpart;
	D -> imagepart = A -> imagepart * B -> imagepart;
}

void devide( Complex* C, Complex* D, Complex* E ){
	E -> realpart = ( D -> realpart * C -> realpart + D -> imagepart * C -> imagepart )/( C -> realpart * C -> realpart + C -> imagepart * C -> imagepart);
	E -> imagepart = ( D -> imagepart * C -> realpart - D -> realpart * C -> imagepart )/( C -> realpart * C -> realpart + C -> imagepart * C -> imagepart);
}

int main(){
	Complex* A = ( Complex* )malloc( sizeof( Complex ) );
	Complex* B = ( Complex* )malloc( sizeof( Complex ) );
	float real, image;
	printf("Enter the realpart and the image part for complex A: ");
	scanf("%f %f", &real, &image);
	create( A, real, image );
	printf("Enter the realpart and the image part for complex B: ");
	scanf("%f %f", &real, &image);
	create( B, real, image );
	Complex* C = ( Complex* )malloc( sizeof( Complex ) );
	Complex* D = ( Complex* )malloc( sizeof( Complex ) );
	add( A, B, C );
	multiply( A, B, D );
	Complex* E = ( Complex* )malloc( sizeof( Complex ) );
	if( C -> realpart != 0 && C -> imagepart != 0 ){
		devide( C, D, E );		
	} 
	if( E -> imagepart < 0 ){
		printf("%.2f%.2fi", E -> realpart, E -> imagepart );
	} else if ( E -> imagepart == 0 ) {
		printf( "%.2f", E -> realpart );
	} else {
		printf("%.2f+%.2fi", E -> realpart, E -> imagepart );
	}
	free( A );
	free( B );
	free( C );
	return 0;
} 


// z = (8+6i)(4+3i)/(8+6i)+(4+3i)
