This is a skinpack creator for minecraft bedrock. 

It allows you to choose a skin and a cape
(there is an option to have no cape) and put it
into a working skinpack.

This version of the program is more for delicate
selection being that you have full control over 
what you put in it and how you name things.

While this is a skinpack creator there are limits
such as you can only use slim skins and the
geometry that you use.

Presently the only geometry used is
"geometry.humanoid.customSlim" and if you have
any skins that would use different ones, it
won't work with how this program runs.

There is no selection for any other geometry but
feel free to take the code and make it!

-------------------------------------------------
So, here are the very basics on how to use the
program, first you need to have a few libraries
installed before you launch the app. 

Those libraries are customtkinter, tkinter, 
PIL, os, shutil, and uuid. 

After you have those, you can then launch the 
app and will be greeted with the UI. 

The first steps in creating your skinpack 
inside the application is by typing a name for 
your skinpack and selecting the folders that 
contain your skins and the file that contains 
your capes. 

There are dropdown menus for both your skins and 
capes near the left.

It's possible to name your skins that will go
into the skinpack otherwise it will take the
name of the files themselves and combine them.

As a disclaimer, your files may appear blurry in
the display and if that's the case it's because
of the bit depth in your file.

If the file the program is trying to display has
a bit depth higher than 8, it will appear blurry
and the way you can fix it if it really bugs you
is by exporting your file to be at a bit depth
of 8.

If you dont have an application to do that I
suggest GIMP as it is a free image editor and
with a little bit of researching you can
export your files in an 8 bit depth.

Once you've selected your files, you can click
the green add button to add it to your listings
and you can use the delete skins button to
remove listings you didn't mean to add in.

After you're happy with everything you've added
you can select the directory you want to export
to, or keep it at the default export point and
export your skinpack.

If you're using it as a 4d skinpack and you're
pushing it into your persona you dont have to
make it a zip file; however, if you're
expecting it to work like a normal skinpack,
you can compress the file and make it an
mcpack to import to minecraft.

As a disclaimer, capes only work in the persona
file and I cannot promise you that the program
can push the skinpack to that file due to the
file permissions the persona filepath has.

-------------------------------------------------
!!!!!!!BEFORE YOU USE THE SKINPACK CREATOR!!!!!!!

This program does not mess with your image files 
and only copies them to another file after saving 
your skinpack.

Notice that whenever you open the deletion menu
that you can select entries that you made.

Those entries do not update inside the
"Skinpack view and skin deletion" window while
it's open, so if you add skins in the background
while having this window open and decide to 
delete skins you risk losing your new entries.

To avoid losing skins when you want to remove
one, make sure you open the window and delete
what you want to delete from it (by selecting the
entries in the window and hitting the delete key)
and press the ESC key while you're focused on the
window to close the window and save your deletions.

If you feel like you've deleted skins entries that
you wanted just click the "X" close button in the
top right of the "Skinpack view and skin deletion"
window and it wont delete anything from the list.

There is an output box that tells you what's going
on and what's wrong if it can't do something, and 
if you cant see it that way the program also prints
the error messages in the console.

While you can select skins and capes from different
folders and use them, this program does not check
if names are the same and will either error while
copying files or if you named a skin entry the same,
it most likely will not work the way you want it to
in minecraft.

-------------------------------------------------
This is my first big coding project that I did on
my own and would be thankful if you could tell me
what I can fix or add.

This being said, thank you for looking at my
project and if you edit it or repost it please
make sure to credit me.
