! Working with matrices in Fortran.
! Author: Andrew Jarombek
! Date: 2/15/2020

program matrices
    implicit none

    integer, dimension (3, 3) :: matrix
    integer :: i, j

    print *, "Fortran Matrices"

    ! In Fortran, arrays are column major.  That means when accessing a matrix element with matrix(j, i),
    ! j is the column and i is the row.  C is row major, so i and j are flipped.
    do i = 1,3
        do j = 1,3
            matrix(j, i) = (i - 1) * 3 + j
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