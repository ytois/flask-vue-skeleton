const path = require('path')
const ManifestRevisionPlugin = require('manifest-revision-webpack-plugin')

module.exports = {
  pages: {
    index: {
      entry: 'frontend/main.js',
    },
  },
  outputDir: 'backend/static',
  configureWebpack: {
    plugins: [
      new ManifestRevisionPlugin(
        path.join('backend', 'static', 'manifest.json'),
        {
          rootAssetPath: './frontend',
        }
      ),
    ],
  },
  // disable output html
  chainWebpack: config => {
    config.plugins.delete('html-index')
    config.plugins.delete('preload-index')
    config.plugins.delete('prefetch-index')
  },
}
