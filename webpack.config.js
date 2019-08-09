const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const path = require('path');

module.exports = {
    context: __dirname,
    entry: {
        home: './assets/js/index.js',
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
        new VueLoaderPlugin(),
    ],

    module: {
        rules:  [
            {
                test: /\.css$/,
                use: [
                  { loader: 'vue-style-loader' },
                  { loader: 'css-loader', options: { sourceMap: true } },
                ]
              },
              {
                test: /\.scss$/,
                use: [
                  { loader: 'vue-style-loader' },
                  { loader: 'css-loader', options: { sourceMap: true } },
                  { loader: 'sass-loader', options: { sourceMap: true } },
                  { loader: 'sass-resources-loader',
                    options: {
                      sourceMap: true,
                      resources: [
                        path.resolve(__dirname,'assets/stylesheets/scss/_parameters.scss'),
                      ]
                    }
                  }
                ]
              },
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            }
        ],
    },
};
