# vue-hn-clone

This app is a Vue.js-based clone of [Hacker News](https://hn.ycombinator.com). 

## Objective

It is helpful to have a go-to app for demoing new tools - this is mine. It's nice to have an app that is more than just a hello world, so I tried to create one that mirrors something usable to some degree.

## Tech info

* [Vue.js](https://vuejs.org/) - The frontend web framework used to build the site
* [HackerNews/API](https://github.com/HackerNews/API) - Source of data
* [Bulma](https://bulma.io) (Specifically [Buefy](https://buefy.org)) - the CSS framework I've used

This app is far from an ideal architecture - it is currently all client-side rendered and re-pulls all data on page change.
In the future I may add [vuex](https://vuex.vuejs.org/) so it doesn't query the API every single page change.

Ideally you would use server-side rendering like [this example](https://github.com/vuejs/vue-hackernews-2.0) does (in fact, that app is all around better).
But to make testing certain tools easier, being strictly client-side rendered is preferable.


## Deployment requirements

You need to set the `VUE_APP_ROLLOUT_KEY` environment variable to your Rollout App API key.


## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn run serve
```

### Compiles and minifies for production
```
yarn run build
```

### Run your tests
```
yarn run test
```

### Lints and fixes files
```
yarn run lint
```

### Run your unit tests
```
yarn run test:unit
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
