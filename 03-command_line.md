# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> >
1. __Show current Working Directory__  
   $ pwd

2. __Creating a directory__  
$ mkdir dirname

3. __Deleting a directory__  
$ rm -r dirname ('r' deletes all child directories also)

4. __Creating a file using touch command__  
$ touch hello.txt

5. __Deleting a file__  
$ rm filename

6. __Renaming a file__  
$ mv filename newfilename

7. __Copying a file from one directory to another__  
$ cp filename ../directory/ ( moves up the tree and saves it to the directory there)
$ cp filename ../../directory/filename ( moves up 2 level of the tree and saves file to the directory there)

8. __Listing hidden files__   
$ ls -a

9. __Search and replace words within a file__  
sed 's/word/NewWord/' filename (search and replace the 'word' and replaces with 'NewWord')

10. __Find/Groups file/directory containing a string__  
$ grep -r word (-r is recursive use and finds word within all directories and files

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> >ls : list files  
ls -a : list all files (including hidden)  
ls -l : list files with long listing format  
ls -lh: list files with long listing and trucated files sizes (human readable)  
ls -lah :list all files(hidden also) in long listing with human readable format  
ls -t : list files with time sort ( newer first )  
ls -Glp: list in long listing format without any grouping  


---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> >ls -a  
ls -alt  
ls -t  
ls --help  
ls -Sl   

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 

