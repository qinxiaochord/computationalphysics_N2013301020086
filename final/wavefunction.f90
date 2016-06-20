PROGRAM wavefunction
IMPLICIT NONE
REAL :: delta = 0.1, d = 0.1, a, b
INTEGER,PARAMETER :: l = 30
INTEGER :: m, n
REAL,ALLOCATABLE :: psi0(: , :)
ALLOCATE(psi0(- l / 2 : l / 2, - l / 2 : l / 2))

psi0 = 0.03
!DO m = -l / 2 + 1, l / 2 -1
!    DO n = - l / 2 + 1, l / 2 - 1
!        psi0(m, n) = EXP(- (m ** 2 + n ** 2) * delta ** 2)
!    END DO
!END DO
psi0(- l / 2, :) = 0.
psi0(l / 2, :) = 0.
psi0(:, - l / 2) = 0.
psi0(:, l / 2) = 0.

CALL pot(psi0, delta, d)
CALL store(psi0)

CONTAINS
    SUBROUTINE update(psi, d)
        IMPLICIT NONE
        INTEGER :: i, j
        REAL :: d
        REAL,ALLOCATABLE :: psi(: , :)
        DO i = - l / 2 + 1, l / 2 - 1
            DO j = - l / 2 + 1, l / 2 - 1
                psi(i , j)=1./2.*(psi(i-1,j)+psi(i+1,j)+psi(i,j-1)+psi(i,j+1))/(2.+0.5*d**4-d**2)
            END DO 
        END DO
    END SUBROUTINE update

    SUBROUTINE pot(psi, delta, d)
        IMPLICIT NONE
        INTEGER :: i, j
        REAL :: delta, d
        REAL :: a, b
        REAL,ALLOCATABLE :: psi(: , :)
        DO WHILE(delta > 0.0001)
            a = sum(psi)
            CALL update(psi, d)
            b = sum(psi)
            delta = abs(a - b)
        END DO
    END SUBROUTINE pot

    SUBROUTINE store(psi)
        IMPLICIT NONE
        INTEGER :: stat
        REAL,ALLOCATABLE :: psi(: , :)
        INTEGER :: i
        OPEN(UNIT = 1, FILE = 'wavefunction.txt', ACTION = 'READWRITE', STATUS = 'REPLACE', IOSTAT = stat)
        IF (stat == 0) THEN
            DO i = - l / 2, l / 2
                WRITE(UNIT = 1,fmt='(70(1X,F10.6))') psi(i, :)
            END DO
        END IF
        CLOSE(UNIT = 1)
    END SUBROUTINE store

END PROGRAM wavefunction
