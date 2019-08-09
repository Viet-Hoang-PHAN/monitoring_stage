const merge = require('webpack-merge');
const common = require('./webpack.config.js');
const path = require('path');

module.exports = merge(common, {
    mode: 'production',
    resolve: {
        alias: {vue: 'vue/dist/vue.min.js'}
    },
    output: {
        path: path.resolve('./dist/'),
        filename: '[name].js',
        chunkFilename:'[id].js',
        publicPath: './dist/'
    },
});