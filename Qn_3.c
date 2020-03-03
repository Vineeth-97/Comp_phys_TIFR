#include <stdio.h>
#include <gsl/gsl_linalg.h>
int main()
{
    double a[] = {1, 0.67, 0.33, 0.45, 1, 0.55, 0.67, 0.33, 1};

    gsl_matrix_view m = gsl_matrix_view_array(a, 3, 3);
    int s;
    gsl_permutation *p = gsl_permutation_alloc(3);

    gsl_linalg_LU_decomp(&m.matrix, p, &s);
    printf("A = \n");

    gsl_permutation_free(p);
    return 0;
}