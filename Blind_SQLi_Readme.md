
In Blind SQL injection vulnerability, we can not see any data which we have extracted by using our payload. Rather it is done via 3 methods.

# 1) Conditional MESSAGE BASED BLIND SQL INJECTION :
       If the condition is true then application behaves differently like giving a 'welcome back' message, but if false then no 'welcome back' message. With this we can guess If along side 
       the true condition which will be true every time ( like here we used Tracking ID ), if our condition is also correct then 'welcome back' message comes through which we will be able 
       to know that our condition is true otherwise false.

# 2) ERROR BASED BLIND SQL INJECTION :
       If the condition is true then we invoke the SQL to create a internal server error, If error comes then our condition is true otherwise false and have to test other condition.
