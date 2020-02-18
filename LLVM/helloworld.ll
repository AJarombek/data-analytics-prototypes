; ModuleID = helloworld.ll

; A Hello World file in LLVM Intermediate Language.
; Author: Andrew Jarombek
; Date: 2/17/2020

@.str = internal constant [13 x i8] c"Hello World\0A\00"

declare i32 @printf(i8*, ...)

define i32 @main(i32 %argc, i8** %argv) nounwind {
entry:
    %temp = getelementptr [13 x i8],[13 x i8]* @.str, i32 0, i32 0
    call i32 (i8*, ...) @printf(i8* %temp) nounwind
    ret i32 0
}