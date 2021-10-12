# Removing Large Files from Git History with BFG

Source: https://www.phase2technology.com/blog/removing-large-files-git-bfg

On a recent project, our Git repo had ballooned to over **3GB**. The .git directory alone was **2.7GB**. This was slowing down builds and annoying the heck out of developers.

Turns out, a [tool called BFG](https://rtyley.github.io/bfg-repo-cleaner/) makes it dead simple to clean large files out of your Git history. It does this without actually deleting the files themselves from the latest commit. Here's a quick walkthrough on putting your Git repo on a diet using BFG.


## Step 1: Install the BFG cli tool

If you're on a Mac, run `brew install bfg`, but note that it'll prompt you to install Java first if you don't have it yet.

You can also [download it directly](https://rtyley.github.io/bfg-repo-cleaner/#download).


## Step 2: Clone your repo as a mirror

Run this to clone your repo as a mirror.

`git clone --mirror git://example.com/your-repo.git`

The `--mirror` flag means that it doesn't actually download any of the files from your codebase. It downloads the `.git` directory contents into the top level, so it looks a little funky at first.


## Step 3: Back up your repo

Just in case, now is a good idea to back up your repo to a separate location so that you can restore from it if needed.

`cp -r your-repo.git your-repo-backup.git`


## Step 4: Run BFG to remove large blobs

In BFG, you have 3 main options for clearing out large files from your Git history.

*Note: "blobs" are the objects that store file contents in Git.*


### Option 1: Strip blobs bigger than a specified size

In this case, you're telling BFG to remove any blobs from history that are larger than a specified size. For example, to strip out any blobs bigger than 10MB, you run:

`bfg --strip-blobs-bigger-than 10M your-repo.git`


### Option 2: Strip the biggest blobs, limited to a specified number

If you'd rather just strip the biggest blobs regardless of how large they are, BFG makes that easy:

`bfg --strip-biggest-blobs 100 your-repo.git`

This command will strip the 100 largest blobs from your repo history.


### Option 3: Strip specific blobs, specified by IDs

If you know of specific files you want to get rid of, you can take this approach. In this case, you'll pass in a text file that contains the list of blob IDs you want to strip.

`bfg --strip-blobs-with-ids blobs.txt your-repo.git`

You can use [a one-liner like this](https://gist.github.com/rtyley/4202730) like this to find the IDs of the largest blobs.


## Protecting specific branches

BFG is very good at making sure that it doesn't touch any of the files on your HEAD. It only adjusts your history, not the files in your latest commit.

But if you have other branches you want to make sure you protect, you can do that with the `--protect-blobs-from` flag:

`bfg --protect-blobs-from master,dev,stage --strip-biggest-blobs 100 your-repo.git`


## Step 5: Expire and prune your repo

You're removing things with BFG. Now it's time to expire and prune your git history to reflect your changes. Here's how you'd do that:

`cd your-repo.git git reflog expire --expire=now --all && git gc --prune=now --aggressive`

Note that this command can take **a long time** depending on your repo size. So it's best to make sure you're done running BFG first. You only want to have to run this command one time.


## Step 6: Check your repo size

Verification time! Did the repo shrink? If not, then you probably missed a step or didn't remove the correct files.


## Step 7: Push your changes

Now you're ready to push all your updates so that everyone can enjoy the new, slimmer repo you have fashioned.

`git push`

And that's that! Your repo should be smaller, without any noticeable negative effects. Thanks BFG!