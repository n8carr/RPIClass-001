##################################
# 07/15/2018                     #
# Author : Andrew Tyler Pierce   #
# Desc : Outline for class 5     #
##################################

# Git and GitHub

    # Making a Pull Request

    # Start by forking repo from repo you want
    
    #  Clone that forked repository

        # git clone git@github.com:typhoontong22/RPIClass-001.git

        #                            ^
        #                            |
        #                       your username
                    
    # Navigate to that repository (or directory)

        # cd /home/pi/Desktop/RPIClass-001
    
    # Then make a branch for that repository

        # git branch example

    # Then checkout that branch

        # git checkout example

    # If you want to verify which branch you are in

        # git branch

    # Then add whatever files you've saved to your repository

        # git add -A
        # or
        # git add --all

    # Commit all of the changes you've made to your branch

        # git commit -a

    # Write in the editor a useful commit message that will
    # let you know all that was worked on. Then when you
    # finish with that message, hit:

        # ctrl+X

    # and then Y for yes to save it
    # then enter to write it to the same file

    # Everything we've been working on up to this point has
    # been local on our machine. Now we need to interact 
    # with the remote repository.

    # First pull all changes down to your local repository
    # in order to make sure that you don't have any
    # conflicts. (If this is the beginning of a new branch
    # there will not be a remote repository so it will not
    # fetch anything to merge)

        # git pull origin example

    # Then if and only if there are no merge errors, push
    # your code to the remote repository.

        # git push origin example

    # There! Now our code is safe and sound in the remote
    # repository. So if we ever accidentally ruin our
    # local repository it is not a problem since we can
    # just go and blow away our own repository and clone
    # the repository fresh again.

        # git clone git@github.com:typhoontong22/RPIClass-001.git

    # If you are finished with a branch or just want to
    # make sure your changes are in the master branch,
    # you can submit a pull request on github

    # Navigate to https://www.github.com

    # Navigate to the RPIClass-001 repository

    # In the window next to the branches drop down,
    # you should see a "New pull request" button
    # This should allow you to start the process of
    # asking for your code to merged into the master
    # branch.

    # If it isn't merged don't take it personally.
    # Your code isn't indicative of you as a coder but
    # might not be necessarily needed or wanted by the
    # repository owner. 


# Finishing Cat and Mouse game

    # Finish up setting up the cat and mouse game

# Going over Variables, Values and Types

    # What is a variable?

        # It is a place where you can store values you want
        # to use later.

    # There are also different types of variables

        # For instance, lets look at these two variables

            # variable_A = 1
            # variable_B = '1'

        # What is the difference here? Well naturally we can
        # observe that there are little quote marks around
        # the "one" in variable_B but what does it mean?
        # Well let's try something out.

        # Type:

            # type(variable_A)
            # type(variable_B)

        # What do these return?

        # What is the difference between a string and an int?

        # 
