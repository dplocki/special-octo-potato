# 🥔 Special Octo Potato

This is my balasting field for Github Actions. The place to test workflows, actions their result.

## Notes

* Offical help for [Github Action](https://help.github.com/en/actions)
* Cannot use `alpine` image as `runs-on`
  * The only avaible options can be found on the page:[Virtual environments for GitHub-hosted runners](https://help.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners)
  * You can use docker image
* The job names must start with a letter or '_' and contain only alphanumeric characters, '-', or '_'
* You can react on tags without declaring the branch
* If you have the syntax error in you workflow file, you lose acess to history of prevouse builds for that workflow
