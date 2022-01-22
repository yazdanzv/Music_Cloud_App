# Music_Cloud_App
A GUI server and client program that you can regirster and download your music from the server (multithread server)


# Welcome to this app

# Music Cloud


## This program GUI was built with tkinter in python and it's actually a server , client app in GUI form that you can register and download your favourite music from the music bank that exists in the server (Music_Bank)


## We are going to look at every pages and features of this app 

### * Signin and Signup page : 


![](![sign in page](https://user-images.githubusercontent.com/73643415/149951004-70a54270-24bf-4191-b3d0-d25e186601fb.png)

&

![](![sign up page](https://user-images.githubusercontent.com/73643415/149954981-6346e0f9-29ae-4719-8b32-4b522643b7dc.png))


in this page you can signin and also signup in the server and it has so many features , like it will check your phone number and email address by regex and pop up a dialogebox if it's not valid()for phone validation it has been set with Iran phone numbers , you can change the regex pattern as you wish) and it will pop up another dialogebox if you missed something in signup page and waits for you to fill it

it can also tells you that you are not registered or your password is incorrect by dialogebox
after we filled the entries with right informations we press enter and it will go to the using_page


### * Using Page

![](![Using page](https://user-images.githubusercontent.com/73643415/149952427-4e454bc0-f9fd-43e5-b1ef-dd993ef563b5.png))



in this page you have a listbox that shows all of the musics that exists in the Music_Bank (server side) and you can search among them in the entry above the listbox and it will automatically bring the musics with similiar names for you (Like Google search)

you can see two buttons here , one of them (download button) is disable at the first untill you choose a path for you musics from the Select the path button
after you've selected you path it will shows up under this button and download button becomes enabele
after that you can choose your music and click the download button and see that it will be downloaded in the specified path 

you can see an avatar logo on this page , if you click on that it will bring you to the setting page 

* ### Setting_page : 

![](![changing informations page](https://user-images.githubusercontent.com/73643415/149953816-5bde8a51-ed5c-4545-8d9d-8a7313529c66.png))

you can see multiples buttons here , back button will brings you to the Setting page as it said itself , log out button will brings you to the Signin & Signup page and you can signin with another account or make another account and user data button will brings you to the next page (Account Information page) that we are going to see now 

* ### Account Information page : 

![](![user information page](https://user-images.githubusercontent.com/73643415/149954682-8ea20049-d094-4b07-a136-73947f38a6c1.png))

you can see all of your informations here 

at first I have to say I filled the phone number entry with something meaningless to don't show my phone number so it's not a bug :)

you can modify all of your informations here exept your username cause the server knows you by that , and you can also see that apply button is disabled here and it waits to something changes here and then it'll be enabeled 

as you can see the password dosn't shows here for security things !

after you pressed the apply button you can see this page will pop up 

### * Apply page : 

![](![apply the changes page](https://user-images.githubusercontent.com/73643415/149956078-00f50943-d968-4adc-9534-f1acb12c3830.png))

if you click on the no button it brings you back to the previous page with the previous informations and of you press yes button it will changes the user informations in the User_Data.json file by server and brings you to the previous page with the new informations 

### * Forget your Password page : 

![](![forget your password page](https://user-images.githubusercontent.com/73643415/149956559-c9724049-a5db-4d8c-bebf-a33c9fa99acf.png))

if you forget your informations such as password and username (it doesn't matter) you can click on this label under the password entry in the Signin and Signup page and go to this page that you can see here 
it doesn't matter that if you enter your email that you signed up with or enter you username , it will works in both ways
in this page if you enter wrong informations as we saw in the previous pages the app will pop up a dialogebox to show the error
if you want to go to the Signin and Signup page again you can click on the logo of the app above the entry

### * Verification page : 

![](![Verify page (enter the security code)](https://user-images.githubusercontent.com/73643415/149957608-fb87e034-5166-46e4-843d-7be95bcda037.png))

in this page the app is waiting for you to enter the verification code (5 digit code) that sent to your email before

if you didn't recieved it you can click on resent label to program sends you another code 

you can see email photoes here : 

![](![email sent](https://user-images.githubusercontent.com/73643415/149958323-a7a1490d-535c-4af9-b84f-cc491f222f29.png))

&

![](![email preview](https://user-images.githubusercontent.com/73643415/149958387-f217efaa-353d-45e6-aefc-bdb8bc2226b2.png))

the code sends by the server by smtplib module and an dummy email that I've made for this app
you can see them in server code

at last if you enter correct code , app will brings you to the next page that shows you the user's username and password 
like the previous pages if you enter wrong code a dialogebox will pop up and shows the error

you can see the next page here

### * Reteive Account Informations page : 

![](![reteive account informations page](https://user-images.githubusercontent.com/73643415/149960188-3ac8e57b-eede-4b8c-90d1-8522fa5f83bd.png))

finally you can see your informations here and after that by clicking on signin button or logo you can go to the first page


### * Server : 

server has no GUI page and working with it is completely with the console and the code is very simple 
at first it logs in the dummy email that I've made and after that it listens and waits for the clients and as I said before it's a multithread server and multiple clients can connects to it 

there is a main function named fun here that specifies what service client wants and after that fun transfers you to the right function

it's easy to catch and nothings is complex in server that you can't catch

at last I want to say sorry for lots of comments in the codes , I didn't delete them for updating this app in future ,
if you want you can update it for yourself and use it 
