# Updating submodules for release

1. open a new topic branch from the latest `develop`
``` 
git checkout develop
git reset --hard
git pull origin develop
git branch -d update_submodules
git checkout -b update_submodules
```

1. grab the latest commits from the remote of each submodule
```
git submodule update --remote
git submodule foreach git pull
```

1. commit the updates and push
```
git add .
git commit -m "update the submodules"
git push origin update_submodules
```

1. open a PR on GitHub after checking off the PR checklist.