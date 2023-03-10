import styled from "styled-components";

export const HeaderContainer = styled.header`
  width: 100%;
  padding: 2rem 2rem 0;
  display: flex;
  justify-content: space-between;
  
  .logo-and-search {
    width: 97%;
    display: flex;
    flex-direction: column;
    gap: 3rem;
  }
  
  .logo-and-search img {
    width: 30%;
  }
  
  @media(min-width: 700px) {
    height: 10vh;
    align-items: center;

    .logo-and-search {
      flex-direction: row;
      width: 60%;
    }

    img {
      width: 10%;
      max-width: 12rem;
    }
  }
  `

export const SearchWrapper = styled.div`
 display: flex;
 align-items: center;
 gap: 1rem;
 width: 100%;
 padding-inline: 1rem;
 border-radius: 4px;
 box-shadow: 0 1px 4px gray;
 
 div {
   width: 100%;
  }
  
  @media(min-width: 700px) {
    width: 70%;
   /*  box-shadow: none;
    border-bottom: 1px solid ${({theme}) => theme.colors["base-input"]}; */
 }
`

export const LoginWrapper = styled.div`
  display: none;
  padding-inline: 2rem;

  button {
    cursor: pointer;
    position: relative;
    color: ${({theme}) => theme.colors["brand-yellow-dark"]};
  }

  @media(min-width: 700px) {
    display: flex;
    align-items: center;
    gap: 2rem;
  }
`