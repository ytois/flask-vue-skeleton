var path = require('path');
var ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');

module.exports = {
  pages: {
    index: {
      entry: 'frontend/main.js'
    }
  },
  outputDir: 'backend/static',
  configureWebpack: {
    plugins: [
      new ManifestRevisionPlugin(
        path.join('backend', 'static', 'manifest.json'),
        {
          rootAssetPath: './frontend'
        }
      )
    ]
  }
};
