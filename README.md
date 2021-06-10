# 🥔 Special Octo Potato

This is my blasting field for Github Actions. The place to test workflows, actions their result.

## Notes

* Official help for [Github Action](https://help.github.com/en/actions)
* Cannot use `alpine` image as `runs-on`
  * The only available options can be found on the page: [Virtual environments for GitHub-hosted runners](https://help.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners)
  * You can use docker image
* The job names must start with a letter or '_' and contain only alphanumeric characters, '-', or '_'
* You can react on tags without declaring the branch
* If you have the syntax error in you workflow file, you lose access to history of previous builds for that workflow

## Links

* [GitHub Actions to securely publish npm packages](https://snyk.io/blog/github-actions-to-securely-publish-npm-packages/)
