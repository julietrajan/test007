# LTM GitHub Copilot Innovation Challenge

This repository contains the Jekyll site for the LTM GitHub Copilot Innovation
Challenge. The site describes an AI-powered Construction Command Center built
with GitHub Copilot and Azure AI Foundry.

## Site structure

The site source is under [`LTM/`](LTM/):

- [`index.html`](LTM/index.html) is the challenge overview, including the
  business scenario, architecture, tasks, deliverables, scoring, and
  definition of done.
- [`pre-requisites.html`](LTM/pre-requisites.html) lists the required learning
  resources.
- [`challenge-2.html`](LTM/challenge-2.html) is the current duplicate
  pre-requisites page retained for compatibility with existing links.
- Local files such as PDFs belong under `LTM/files/`, alongside the page that
  references them. The repository currently has no handbook PDF, so the
  handbook is intentionally not linked until that asset is added.

Each page has Jekyll front matter and uses the `jekyll-theme-cayman` theme.
There is no repository-wide `_config.yml` or `Gemfile`; the commands below
match that configuration by supplying the source directory and installing the
theme directly.

## Prerequisites

Install Ruby (3.2 or newer is recommended) and RubyGems. Then install Jekyll
and the theme:

```sh
gem install jekyll jekyll-theme-cayman
```

## Preview and build

Run these commands from the repository root:

```sh
# Preview at http://localhost:4000 and rebuild when files change
jekyll serve --source LTM --destination _site
```

In a second terminal, create a production-style build:

```sh
jekyll build --source LTM --destination _site
```

The generated site is written to `_site/`. Do not commit that directory.

## Content and link maintenance

Add new pages and page-local assets under `LTM/`. Use lowercase filenames for
new pages and update the navigation links in the existing pages. For a local
asset, confirm that the path is relative to the page's location and that the
file is tracked; for example, a handbook link in `LTM/pre-requisites.html`
would resolve to `LTM/files/<filename>`.

Before opening a change:

1. Run `jekyll build --source LTM --destination _site` and inspect the rendered
   pages in `_site/`.
2. Check every local `href` and `src` target against the files under `LTM/`.
3. Open external learning links and confirm they still reach the intended
   resource.
4. Use the local preview to click through the navigation and any newly added
   links.

