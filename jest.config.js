module.exports = {
  verbose: false,
  transform: {
    '^.+\\.jsx?$': 'babel-jest'
  },
  collectCoverage: true,
  collectCoverageFrom: [
    '<rootDir>/components/**/*.js'
  ],
  coveragePathIgnorePatterns: [
    '<rootDir>/gulpfile.js',
    '<rootDir>/.*.config.js',
    '<rootDir>/.*.min.js',
    '<rootDir>/node_modules/',
    '<rootDir>/config/',
    '<rootDir>/dist/',
    '<rootDir>/scripts/gulp/',
    '<rootDir>/components/.?/node_modules/',
    '<rootDir>/components/capital-framework.js',
    '<rootDir>/components/cf-expandables/src/cf-expandables.js',
    '<rootDir>/components/cf-tables/src/cf-tables.js',
    '<rootDir>/test/',
    '<rootDir>/tmp/',
    '<rootDir>/scripts/'
  ],
  coverageDirectory: '<rootDir>/test/unit-test-coverage',
  testURL: 'http://localhost'
};
