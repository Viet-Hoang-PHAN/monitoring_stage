const merge = require('webpack-merge');
const common = require('./webpack.config.js');
const path = require('path');

module.exports = merge(common, {
    mode: 'development',
    resolve: {
        alias: {vue: 'vue/dist/vue.js'}
    },
    output: {
        path: path.resolve('./assets/bundles/'),
        filename: '[name].js',
        chunkFilename:'[id].js',
        publicPath: './assets/bundles/'
    },
});