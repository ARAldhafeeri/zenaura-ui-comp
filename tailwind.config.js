/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'selector',
  content: [
    './public/index.html', "./public/**/*.py"
  ],
  theme: {
    colors: {
      dark: {
        black: "#040D12",
        purble1: "#393646",
        gray1: "#222831",
        gray2: "#344955",
        hover: "#00ADB5",
        page1: "#F4EEE0",
      },
      light: {
        white: "#EEEEEE",
        hover: '#CCCCCC',
        green: "#76ABAE",
        gray1: "#31363F",
        gray2: "#222831",
      }
    },
    extend: {},
  },
  plugins: [],
}

