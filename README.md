# Peng Ruoxin — Academic Homepage

Source for [pengruoxin.github.io](https://pengruoxin.github.io), an English academic homepage focused on computer vision, vision-model reassembly, and efficient architecture search.

The site is built with [Jekyll](https://jekyllrb.com/) and [al-folio](https://github.com/alshedivat/al-folio), then deployed through GitHub Pages.

## Local development

```bash
bundle install
npm ci
bundle exec jekyll serve --livereload
```

Run the rendered-site contract and formatting checks with:

```bash
node --test tests/site-contract.test.mjs
npm run lint:prettier
```
