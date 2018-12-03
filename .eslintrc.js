module.exports = {
  root: true,
  env: { browser: true },
  parser: 'vue-eslint-parser',
  extends: [
    'standard',
    'plugin:vue/recommended',
    'plugin:prettier/recommended'
  ],
  plugins: ['prettier', 'vue'],
  rules: {
    'prettier/prettier': [
      'error',
      {
        semi: false,
        singleQuote: true,
        trailingComma: 'es5'
      }
    ]
  }
}
