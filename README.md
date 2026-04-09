[![Netlify Status](https://api.netlify.com/api/v1/badges/npm-hat-cms/deploy-status)](https://app.netlify.com/sites/npm-hat-cms/deploys)

# npm-HAT-CMS

A custom CMS to help manage the [npm-HAT](https://github.com/SummittDweller/npm-HAT) (Hometown Action Team) website. This project is patterned after the [wieting-one-click-hugo-cms](https://github.com/SummittDweller/wieting-one-click-hugo-cms) project in the same GitHub account.

## Overview

This repository provides a [Netlify CMS](https://www.netlifycms.org/) (Decap CMS) interface for managing content in the [SummittDweller/npm-HAT](https://github.com/SummittDweller/npm-HAT) Hugo website. It uses [Victor Hugo](https://github.com/netlify/victor-hugo) as the underlying build system (webpack + Hugo).

### Managed Content Types

The CMS provides editing interfaces for the following content types in the npm-HAT project:

| Collection | Folder | Description |
|---|---|---|
| **Events** | `content/event` | HAT steering committee meetings and other events |
| **Posts** | `content/post` | General news and announcements |
| **Plans** | `content/plan` | Community planning documents and concept overviews |
| **Documents** | `content/document` | Meeting minutes and reference documents |
| **Education** | `content/education` | Educational content (e.g. RRFB guides) |
| **Let's Moove** | `content/moove` | Let's Moove / Connect Tama-Toledo project pages |
| **Main Pages** | `content/` | Top-level pages: About, Calendar, Contact |

## Getting Started

### Prerequisites

- Node.js 12+ (see `.nvmrc`)
- Hugo (installed via `hugo-bin` npm package)
- A GitHub account with access to the [SummittDweller/npm-HAT](https://github.com/SummittDweller/npm-HAT) repository
- A [Netlify](https://www.netlify.com/) account (for deployment and authentication)

### Local Development

Clone this repository and install dependencies:

```bash
git clone https://github.com/SummittDweller/npm-HAT-CMS.git
cd npm-HAT-CMS
npm install
```

Then start the development server:

```bash
npm start
```

For local CMS editing (without deploying to Netlify), run the Netlify CMS proxy server in a separate terminal:

```bash
npx netlify-cms-proxy-server
```

Then set `local_backend: true` in `site/static/admin/config.yml`.

### Building for Production

```bash
npm run build
```

The built site will be in the `dist/` directory.

## Deployment

This project is designed to be deployed on [Netlify](https://www.netlify.com/). The `netlify.toml` file configures the build command and publish directory.

### Netlify Setup

1. Connect the repository to Netlify
2. Enable **Netlify Identity** on your Netlify site (Site Settings → Identity → Enable Identity)
3. Under **Identity → Services → Git Gateway**, enable Git Gateway
4. The CMS will be available at `https://your-site.netlify.app/admin/`

### Backend Configuration

The CMS backend is configured in `site/static/admin/config.yml`. By default it uses the `github` backend pointing directly to the `SummittDweller/npm-HAT` repository:

```yaml
backend:
  name: github
  repo: SummittDweller/npm-HAT
  branch: main
```

Alternatively, if you add npm-HAT as a git subtree under `site/`, you can switch to the `git-gateway` backend (see comments in `config.yml`).

## Project Structure

```
npm-HAT-CMS/
├── .babelrc              # Babel configuration
├── .eslintrc.yml         # ESLint configuration
├── .gitignore
├── .nvmrc                # Node.js version (12)
├── netlify.toml          # Netlify build configuration
├── package.json          # npm scripts and dependencies
├── postcss.config.js     # PostCSS configuration
├── webpack.common.js     # Shared webpack config
├── webpack.dev.js        # Development webpack config
├── webpack.prod.js       # Production webpack config
├── src/
│   ├── cms.html          # CMS HTML entry template
│   ├── index.js          # Main JS entry point
│   ├── css/
│   │   └── main.css      # Main stylesheet
│   └── js/
│       └── cms.js        # Netlify CMS initialization
└── site/                 # Hugo site
    ├── config.toml       # Hugo configuration
    └── static/
        └── admin/
            ├── index.html    # CMS admin page
            └── config.yml    # CMS collections configuration
```

## Related Projects

- [npm-HAT](https://github.com/SummittDweller/npm-HAT) — The Hugo website this CMS manages
- [wieting-one-click-hugo-cms](https://github.com/SummittDweller/wieting-one-click-hugo-cms) — The template project this CMS is patterned after

