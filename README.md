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
* The workflow must contain at least one job with no dependencies
* Cron schedule if containt slash `/` character, needs be in qoutes
* Schedule task seems to have some delay time to start

### Github NPM Packages

There is possibility for publish npm packages directly on Github (as not scoped repository). See [GitHub Packages: Your packages, at home with their code](https://npm.pkg.github.com).

The usage in workflow is described here: [Publishing Node.js packages](https://docs.github.com/en/actions/guides/publishing-nodejs-packages).

Example set-up code:

```yml
      - name: "Set up the NPM"
        uses: actions/setup-node@v2
        with:
          node-version: '16'
          registry-url: 'https://npm.pkg.github.com'
          scope: '@dplocki'
```

Later usage:

```yml
      - name: "Compering version"
        run: |
          echo `npm info @dplocki/generic-conversation-bot version`
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

### Create tag

```yml
      - name: Create Tag
        uses: negz/create-tag@v1
        with:
          version: v0.1.1
          message: Release for version v0.1.1
          token: ${{ secrets.GITHUB_TOKEN }}
```

## Multiline scripts in YML

```yml
  run: |
    cat << EOF > run.py
    echo line 1
    echo line 2
    ; no indents on each of this lines
    EOF
```

## Links

* [GitHub Actions to securely publish npm packages](https://snyk.io/blog/github-actions-to-securely-publish-npm-packages/)
