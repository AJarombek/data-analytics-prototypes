! Introductory playground of Fortran 2008 code.  I'm investigating Fortran due to its influence on the numpy library.
! Author: Andrew Jarombek
! Date: 2/14/2020

program hello
    integer :: age
    age = 24

    write (*,*) 'Hello, my age is: '
    write (*,*) age

end program hello