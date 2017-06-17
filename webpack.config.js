
const path = require("path");
const webpack = require("webpack");
const ManifestRevisionPlugin = require("manifest-revision-webpack-plugin");
const ExtractTextPlugin = require("extract-text-webpack-plugin");

const extractSCSS = new ExtractTextPlugin("[name].[contenthash].css");

var root = "./assets";

module.exports = {
    entry: {
        vendor: ["jquery"],

        // JS

        // CSS
        app_css: [
            root + "/css/app.scss"
        ],
        bootstrap: [
            root + "/css/bootstrap.scss"
        ]
    },
    output: {
        path: path.resolve("public"),
        publicPath: "/assets/",
        filename: "[name].[chunkhash].js",
        chunkFilename: "[id].[chunkhash].chunk"
    },
    resolve: {
        extensions: [".js", ".jsx", ".scss"]
    },
    module: {
        loaders: [
            {
                test: /\.js$/i,
                exclude: /node_modules/,
                loader: "babel-loader"
            },
            {
                test : /\.jsx?/,
                exclude: /node_modules/,
                loader : "babel-loader"
            },
            {
                test: /\.scss$/,
                use: extractSCSS.extract({
                    fallback: "style-loader",
                    use: ["css-loader", "sass-loader"]
                })
            }

        ]
    },
    plugins: [
        extractSCSS,
        new ManifestRevisionPlugin("manifest.json", {
            rootAssetPath: root,
            ignorePaths: ["/styles", "/scripts"]
        }),
        new webpack.DefinePlugin({
            "process.env": {
                NODE_ENV: '"production"'
            }
        }),
        new webpack.optimize.CommonsChunkPlugin({
            name: "vendor",
            // filename: "vendor.js"
            // (Give the chunk a different name)

            minChunks: Infinity,
            // (with more entries, this ensures that no other module
            //  goes into the vendor chunk)
        }),
        new webpack.optimize.UglifyJsPlugin(),
        new webpack.NoEmitOnErrorsPlugin()
    ]
};
