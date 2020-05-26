#include <stdio.h>
#include <gsl/gsl_linalg.h>
int main()
{
    double a[] = {1, 0.67, 0.33, 0.45, 1, 0.55, 0.67, 0.33, 1};
    int i,j,k;
    int flag = 0;

    //initialize the matrix
    gsl_matrix *m = gsl_matrix_alloc(3, 3);
    gsl_matrix *A = gsl_matrix_alloc(3, 3);

    printf("A = \n");
    for(i = 0;i<3;i=i+1)
    {
      for(j=0;j<3;j=j+1)
      {
        gsl_matrix_set(m,i,j,a[i*3+j]);
        gsl_matrix_set(A,i,j,a[i*3+j]);
        printf("%0.4f\t\t",a[i*3+j]);
      }
      printf("\n");
    }
    printf("\n");

    int s;
    gsl_permutation *p = gsl_permutation_alloc(3);

    //LU_decomposition using inbuilt function
    gsl_linalg_LU_decomp(m, p, &s);

    gsl_matrix *U = gsl_matrix_alloc(3,3);
    gsl_matrix *L = gsl_matrix_alloc(3,3);

    //Print U
    printf("U = \n");
    for (i=0;i<3;i=i+1)
    {
      for (j = 0;j<3;j=j+1)
      {
        if(j<i)
          {printf("0.0000\t\t");gsl_matrix_set(U,i,j,0);}
        else
        {printf("%0.4f\t\t",gsl_matrix_get(m,i,j));gsl_matrix_set(U,i,j,gsl_matrix_get(m,i,j));}
      }
      printf("\n");
    }
    printf("\n");

    //Print L
    printf("L = \n");
    for(i=0;i<3;i=i+1)
    {
      for(j=0;j<3;j=j+1)
      {
        if(j>i)
          {printf("0.0000\t\t");gsl_matrix_set(L,i,j,0);}
        else
        {
          if(j == i)
            {printf("1.0000\t\t");gsl_matrix_set(L,i,j,1);}
          else
            {printf("%0.4f\t\t",gsl_matrix_get(m,i,j));gsl_matrix_set(L,i,j,gsl_matrix_get(m,i,j));}
        }
      }
      printf("\n");
    }
    printf("\n");

    //Generate and print Permutation Matrix
    gsl_matrix *P = gsl_matrix_alloc(3,3);
    gsl_matrix *Id = gsl_matrix_alloc(3,3);
    gsl_matrix_set_identity(Id);

    printf("P = \n");

    for(i=0;i<3;i=i+1)
    {
      for(j=0;j<3;j=j+1)
      {
        gsl_matrix_set(P,i,j,gsl_matrix_get(Id,i,gsl_permutation_get(p,j)));
        printf("%g\t\t",gsl_matrix_get(P,i,j));
      }
      printf("\n");
    }

    //Multiply P*A and L*U and check if (i,j)th elements of both matrices match
    double sum1 = 0;
    double sum2 = 0;

    for(i = 0;i<3;i=i+1)
    {
      for(j=0;j<3;j=j+1)
      {
        for(k=0;k<3;k=k+1)
        {
          sum1 = sum1 + gsl_matrix_get(P,i,k)*gsl_matrix_get(A,k,j);
          sum2 = sum2 + gsl_matrix_get(L,i,k)*gsl_matrix_get(U,k,j);
        }
        if(sum1 != sum2)
          flag = 1;
        sum1 = 0;
        sum2 = 0;
      }
    }

    if(flag == 1)
      printf("The matrices L*U and P*A do not match\n");
    else
      printf("The matrices L*U and P*A match\n");


    gsl_permutation_free(p);
    gsl_matrix_free(m);
    gsl_matrix_free(U);
    gsl_matrix_free(L);
    gsl_matrix_free(P);
    gsl_matrix_free(Id);
    return 0;
}
