#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define OK 0
#define ERROR 1
#define STACKSIZE 100
#define STACKINCREMENT 10

typedef int ElemType;
typedef int Status;
typedef struct stack{
	ElemType *base;
	ElemType *top;
	int stacksize;
}Stack;

Status initStack( Stack *S );
Status Push( Stack *S, ElemType e );
Status Pop( Stack *S, ElemType *e );
//Status GetTopElement( Stack &S, ElemType &e );
//Status ClearStack( Stack &S );
//Status DestroyStack( Stack &S );
void BaseConvertion( unsigned n, unsigned base );

int main(){
	unsigned n, base;
	printf( "Please input a number to convert: " );
	scanf( "%u", &n );
	printf( "Please input a number as base: " );
	scanf( "%u", &base );
	BaseConvertion( n, base );
	return 0;
} 

// init
Status initStack( Stack *S ){
	S -> base = ( ElemType* )malloc( STACKSIZE * sizeof( ElemType ) );
	if( !S -> base ){
		return ERROR;
	}
	S -> top = S -> base;
	S -> stacksize = STACKSIZE;
	return OK;
}

// push
Status Push( Stack *S, ElemType e ){
	if( S -> top - S -> base > S -> stacksize ){
		S -> base = ( ElemType* )realloc( S -> base, ( S -> stacksize + STACKINCREMENT ) * sizeof( ElemType ) );
		if( !S -> base ){
			return ERROR;
		}
		S -> top = S -> base + S -> stacksize;
		S -> stacksize += STACKINCREMENT;
	}
	*( S -> top ) = e;
	S -> top ++ ;
	return OK;
}

// pop
Status Pop( Stack *S, ElemType *e ){
	if( S -> top == S -> base ){
		return ERROR;
	}
	S -> top --;
	*e = *( S -> top );
	return OK;
}

// get top element 
/*
Status GetTopElement( Stack *S£¬ ElemType *e ){
	if( S -> top == S -> base ){	//±ÜÃâ¿ÕÕ»
        return ERROR;
    }
    *e = *( S -> top - 1 );		//e´æ´¢Õ»¶¥ÔªËØ
    return OK;
} 


// clear stack
Status ClearStack( Stack *S ){
    S -> top = S -> base;
    return OK;
}

//destroy stack
Status DestroyStack( Stack &S ){
	free( S.base );
	S.top = NULL;
	S.base = NULL;
	S.stacksize = 0;
	return OK;
}*/

// Convention
void BaseConvertion( unsigned n, unsigned base ){
	Stack S;
	initStack( &S );
	int k, e;
	while( n > 0 ){
		k = n % base;
		Push( &S, k );
		n /= base;
	}
	while( S.top != S.base ){
		Pop( &S, &e );
		char format[3] = { '%' };
		if( base == 16 ){
			format[1] = 'x';
		} else{
			format[1] = 'u';
		}
		printf( format, e );
	}
	free( S.base );
}




