# Patricia Rodrigo Barrio Portfolio

Static GitHub Pages portfolio for **Patricia Rodrigo Barrio**.

## Structure

- `index.html` - main page
- `src/styles.css` - responsive styling
- `src/main.js` - project rendering and navigation behavior
- `data/projects.json` - editable project data source
- `public/images/` - local image assets

## Editing Projects

Project cards are generated from `data/projects.json`. Each project supports:

- `title`
- `description`
- `categories`
- `technologies`
- `featured`
- `links.github`
- `links.demo`

Set `"featured": true` to show a project in the Featured Projects section.

## Profile Image

The portrait is stored at:

```text
public/images/profile.png
```

To replace it, add a new image in `public/images/` and update the portrait `src` in `index.html`.

## Deployment

This repository is ready for GitHub Pages. For a user or organization site named `prodbar.github.io`, push these files to the default branch and GitHub Pages will serve the site from:

```text
https://prodbar.github.io
```
