#!-*- coding:utf-8 -*-
function enumMethods() {
    Java.perform(function () {
        var hook = Java.use("com.example.b.p");
        var ownMethods = hook.class.getDeclaredMethods();
        console.log(ownMethods.join("----\n"))
        return ownMethods;
    });
}