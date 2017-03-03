// Iterative C program to implement pow(x, n)
#include <stdio.h>
 
/* Iterative Function to calculate (x^y) in O(logy) */
int power(int x, unsigned int y)
{
    int res = 1;     // Initialize result
 
    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y & 1)
            res = res*x;
 
        // n must be even now
        y = y>>1; // y = y/2
        x = x*x;  // Change x to x^2
    }
    return res;
}
 
// Driver program to test above functions
int main()
{
    int x = 3;
    unsigned int y = 2;
 
    printf("Power is %d", power(x, y));
    system("PAUSE");	
    return 0;
}
