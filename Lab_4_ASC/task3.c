#include <stdio.h>
#include <stdint.h>     // provides int8_t, uint8_t, int16_t etc.
#include <stdlib.h>

struct a
{
    int64_t x;
    int32_t y, z;
};

struct b
{
    int32_t x;
    int64_t y;
    int32_t z;
};

int main(void)
{
    int32_t i1;
    int64_t l1;
    struct a a1;
    struct b b1;
    int32_t i2, i3, i4, i5;
    int64_t l2, l3, l4, l5;
    struct a a2, a3, a4, a5;
    struct b b2, b3, b4, b5;

 
    printf("b5: %p\nb4: %p\nb3: %p\nb2: %p\nb1: %p\n", &b5, &b4, &b3, &b2, &b1);
    printf("a5: %p\na4: %p\na3: %p\na2: %p\na1: %p\n", &a5, &a4, &a3, &a2, &a1);
    printf("l5: %p\nl4: %p\nl3: %p\nl2: %p\nl1: %p\n", &l5, &l4, &l3, &l2, &l1);
    printf("i5: %p\ni4: %p\ni3: %p\ni2: %p\ni1: %p\n", &i5, &i4, &i3, &i2, &i1);

 
    printf("struct a: %zu\nstruct b: %zu\n", sizeof(struct a), sizeof(struct b));

    
    void* aux_vect = malloc(10 * sizeof(float) + 31);
    
    float* vect = (float*)(((uintptr_t)aux_vect + 31) & ~31);

    printf("aux_vect: %p\n", aux_vect);
    printf("vect:     %p\n", vect);

    
    free(aux_vect);

    return 0;
}