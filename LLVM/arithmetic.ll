; ModuleID = add.ll

; LLVM code that adds two numbers together
; Author: Andrew Jarombek
; Date: 2/17/2020

declare i32 @printf(i8*, ...)

define i32 @add(i32 %x, i32 %y) {
entry:
    %tmp = add i32 %x, %y
    ret i32 %tmp
}

define i32 @mult(i32 %x, i32 %y) {
entry:
    %tmp = mul i32 %x, %y
    ret i32 %tmp
}

define i32 @main() {
    %result = call i32 @add(i32 2, i32 3)

    ret i32 %result
}