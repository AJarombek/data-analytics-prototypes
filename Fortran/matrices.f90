! Working with matrices in Fortran.
! Author: Andrew Jarombek
! Date: 2/15/2020

program matrices
    implicit none

    integer, dimension (3, 3) :: matrix
    integer :: i, j

    print *, "Fortran Matrices"

    ! In Fortran, arrays are column major.  That means when accessing a matrix element with matrix(i, j),
    ! i is the column and j is the row.  C is row major, so i and j are flipped.
    ! NOTE: Column major matrices are an implementation detail, the code behaves the same as row major matrices.
    ! In fact, you can simply pretend i is the row and j is the column in Fortran matrices.
    do i = 1,3
        do j = 1,3
            matrix(i, j) = (i - 1) * 3 + j
        end do
    end do

    ! Column 1
    print *, matrix(1, 1)
    print *, matrix(1, 2)
    print *, matrix(1, 3)

    ! Column 2
    print *, matrix(2, 1)
    print *, matrix(2, 2)
    print *, matrix(2, 3)

    ! Column 3
    print *, matrix(3, 1)
    print *, matrix(3, 2)
    print *, matrix(3, 3)
end program matrices