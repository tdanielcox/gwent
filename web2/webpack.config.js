const path = require('path');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { VueLoaderPlugin } = require('vue-loader');
const webpack = require('webpack');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'script.js',
    path: path.resolve(__dirname, 'dist')
  },
  // devtool: 'inline-source-map',
  devServer: {
	contentBase: './dist',
	hot: true,
	historyApiFallback: true,
  },
  module: {
  	rules: [
  		{
  			test: /\.(png|svg|jpg|gif)$/,
  			use: [
  				'file-loader'
  			]
  		},
		{
			test: /\.scss$/,
			use: [
				'vue-style-loader',
				'css-loader',
				'sass-loader'
			]
		},
  		{
  			test: /\.vue$/,
  			use: [
  				'vue-loader'
  			]
  		},
  		{
  			test: /\.js$/,
  			exclude: /node_modules/,
  			use: {
  				loader: 'babel-loader',
	        options: {
	          presets: ['env']
	        }
  			}
  		}
  	]
  },
  plugins: [
  	new CleanWebpackPlugin(['dist']),
  	new webpack.HotModuleReplacementPlugin(),
  	new VueLoaderPlugin(),
  	new HtmlWebpackPlugin({
  		title: 'Gwent AI',
  		template: 'index.html'
  	})
  ]
};
