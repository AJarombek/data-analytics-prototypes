; ModuleID = basics

; Exploring the basics in the LLVM documentation - https://llvm.org/docs/LangRef.html#abstract
; Author: Andrew Jarombek
; Date: 2/18/2020

@formatString = private constant [4 x i8] c"%d\0A\00"

declare i32 @printf(i8* noalias nocapture, ...)

define i32 @main() {
entry:
    ; Print the result of 1 + 2
    %x = add i32 1, 0
    %y = add i32 2, 0
    %z = add i32 %x, %y
    %call = call i32 (i8*, ...)
                @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @formatString, i32 0, i32 0), i32 %z)

    ; Integers can be varying sizes, including a single bit.
    %bit = add i1 0, 0
    call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @formatString, i32 0, i32 0), i1 %bit)

    %bit2 = add i1 %bit, 1
    call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @formatString, i32 0, i32 0), i1 %bit2)

    ret i32 0
}