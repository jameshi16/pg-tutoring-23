#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

int main() {
    char some_arr[] = "congrats!";
    printf("%llu\n", *((unsigned long long*) some_arr));
    return 0;
}
