# FeelUOwn-bilibili

FeelUOwn plugin for bilibili

## About this template repository 

This template is used for creating a FeelUOwn plugin. Follow the steps to initialize
your project.

1. Rename file from `*bilibili*` to `*YOUR_PLUGIN_NAME*`.
1. Replace the *string* `bilibili` in all files with your plugin name.

For example, if your plugin name is bilibili, you can do it by following commands

```sh
git grep -l 'bilibili' | xargs sed -i 's/bilibili/bilibili/g'
# macOS
# git grep -l 'bilibili' | xargs sed -i '' -e 's/bilibili/bilibili/g'

git grep -l 'cosven' | xargs sed -i 's/cosven/your-name/g'
git grep -l 'yinshaowen241@gmail.com' | xargs sed -i 's/yinshaowen241@gmail.com/your-email/g'

find . -type f -name '*bilibili*' | grep -v .git/ | xargs -I{} sh -c 'mv {} $(echo {} | sed -e "s/bilibili/bilibili/g")'
```

## Installation

```sh
pip3 install fuo-bilibili
```

## Changelog

### 0.1 (2021-11-06)
-
