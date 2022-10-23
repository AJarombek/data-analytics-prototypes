! Learning the basics of Fortran 2008.
! Author: Andrew Jarombek
! Date: 2/15/2020

program basics

    ! Fortran a statically typed language that uses manifest typing.  This means that types of variables must
    ! be declared before the variable is used.  This is different than other languages such as the dynamically typed
    ! JavaScript/Python which allow variables to be declared without an explicitly written type (the types are inferred).
    ! Fortran also has a legacy 'implicit typing' feature where types of variables can be inferred by the first letter
    ! of a variable name.  This feature is strongly discouraged nowadays.
    implicit none

    ! Variable declaration section.
    real :: minutes = 4
    real :: seconds = 47.75
    integer :: miles = 1
    integer :: meters = 1609
    real :: total_seconds

    print *, "Fortran Basics"

    ! Compute the seconds per 200m in my Mile race Thursday night
    total_seconds = (minutes * 60) + seconds
    print *, "Seconds per 200m:"
    print *, (total_seconds / meters) * 200

end program basics