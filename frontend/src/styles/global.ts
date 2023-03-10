import { createGlobalStyle } from "styled-components";

export const GlobalStyle = createGlobalStyle`
   :root {
    font-size: 62.5%; 
  }

  html {
    width: 100vw;
    overflow-x: hidden;
    scroll-behavior: smooth;
  }

  body {
    background-color: ${({theme}) => theme.colors["base-background"]};
    color: ${({theme}) => theme.colors.paragraph}
  }
  
  .container {  
    margin-block: 4rem;
    padding-inline: 2rem;
    box-sizing: border-box;
    margin-inline: auto;
    width: min(60rem, 100%);
  }

  @media(min-width: 700px){
    .container {
      width: min(130rem, 100%);
      padding-inline: 3rem;
    }
  }

  * {
    font-size: 1.6rem;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
  }

  body, input, textarea, button, select, option {
    font-family: "Roboto", sans-serif;
  }

  a {
    text-decoration: none;
  }

  ul {
    list-style: none;
  }

  img {
    max-width: 100%;
  }

  button {
    border: none;
    background: transparent;
    cursor: pointer;
  }
`