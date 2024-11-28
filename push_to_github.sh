# Step 1: Replace "VimeoHDDownloader" with your desired repository name
REPO_NAME="VimeoHDDownloader"

# Step 2: Initialize a new Git repository in the current directory
git init

# Step 3: Add all project files to the staging area
git add .

# Step 4: Commit the files
git commit -m "Initial commit for Vimeo HD Downloader project"

# Step 5: Create a new GitHub repository
gh repo create "$REPO_NAME" --public --confirm

# Step 6: Add the new GitHub repository as a remote
git remote add origin "https://github.com/connorodea/$REPO_NAME.git"

# Step 7: Push the code to the GitHub repository
git branch -M main
git push -u origin main
