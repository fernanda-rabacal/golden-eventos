import styled from "styled-components";

export const LoginContainer = styled.div`
  width: 100%;
  max-width: 40rem;
  margin-top: 5rem;
  
  display: flex;
  flex-direction: column;
  align-items: center;
  
  h1 {
    font-size: ${({theme}) => theme.textSizes["title-m"]};
    font-weight: 400;
  }
`

export const KeepConnectedContainer = styled.div`
  display: flex;
  align-items: center;
  gap: 1rem;

  label {
    font-size: ${({theme}) => theme.textSizes["text-regular-m"]};
  }
`

export const FormContainer = styled.form`
  text-align: center;
  border-radius: 5px;
  border: 1px solid  ${({ theme }) => theme.colors["base-hover"]};
  padding: 2rem 3rem 0;
  margin-top: 1.5rem;
  
  a {
    color: ${({theme}) => theme.colors["base-yellow"]};
    font-size: ${({theme}) => theme.textSizes["text-regular-m"]};
  }
  
  p {
    font-size: ${({theme}) => theme.textSizes["text-regular-m"]};
    color: ${({theme}) => theme.colors["base-label"]};
  }

  p:first-of-type {
    margin-bottom: 4rem;
  }

  hr {
    color: ${({theme}) => theme.colors["base-input"]};
  }

  .register {
    padding: 2rem;
  }

  > div {
    position: relative;
    margin-top: 1.5rem;

    label {
      color: ${({theme}) => theme.colors["base-label"]};
      margin-block: 0.5rem;
      display: flex;
      align-items: baseline;
    }
    
     svg {
      position: absolute;
      top: 50%;
      right: 4%;
      cursor: pointer;
     }
   }
  
  button {
    width: 30rem;
    margin-block: 2rem;
  }
`