PROGRAM potential
IMPLICIT NONE
REAL :: delta = 1.0, a, b
INTEGER,PARAMETER :: l = 30
REAL,ALLOCATABLE :: V0(: , :)
ALLOCATE(V0(- l / 2 : l / 2, - l / 2 : l / 2))
V0 = 0
V0(- l / 6, - l / 6 : l / 6) = 10
V0(l / 6, - l / 6 : l / 6) = - 10

CALL pot(V0, delta)
CALL store(V0)

CONTAINS
    SUBROUTINE update(V)
        IMPLICIT NONE
        INTEGER :: i, j
        REAL,ALLOCATABLE :: V(: , :)
        DO i = - l / 2 + 1, l / 2 - 1
            DO j = - l / 2 + 1, l / 2 - 1
                IF ((abs(i) == l / 6).AND.(abs(j) <= l /6)) CYCLE
                V(i , j) = 1. / 4. * (V(i - 1, j) + V(i + 1, j) + V(i, j - 1) + V(i, j + 1))
            END DO 
        END DO
    END SUBROUTINE update

    SUBROUTINE pot(V, delta)
        IMPLICIT NONE
        INTEGER :: i, j
        REAL :: delta
        REAL :: a, b
        REAL,ALLOCATABLE :: V(: , :)
        DO WHILE(delta > 0.0001)
            a = sum(V)
            CALL update(V)
            b = sum(V)
            delta = abs(a - b)
        END DO
    END SUBROUTINE pot

    SUBROUTINE store(V)
        IMPLICIT NONE
        INTEGER :: stat
        REAL,ALLOCATABLE :: V(: , :)
        INTEGER :: i
        OPEN(UNIT = 1, FILE = 'potential.txt', ACTION = 'READWRITE', STATUS = 'REPLACE', IOSTAT = stat)
        IF (stat == 0) THEN
            DO i = - l / 2, l / 2
                WRITE(UNIT = 1,fmt='(70(1X,F10.6))') V(i, :)
            END DO
        END IF
        CLOSE(UNIT = 1)
    END SUBROUTINE store

END PROGRAM potential
