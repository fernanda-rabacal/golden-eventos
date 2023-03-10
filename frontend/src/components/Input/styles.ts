import styled, { css } from "styled-components";

export const InputWrapper = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
  position: relative;

  > p {
    font-size: 1.2rem;
    color: ${({theme}) => theme.colors["base-error"]};
  }
`

interface InputProps {
  hasError: boolean
}

export const InputContainer = styled.div<InputProps>`
  outline: none;
  height: 4.5rem;
  border-bottom: 1px solid ${({ theme }) => theme.colors["base-button"]};
  transition: 0.4s;
  display: flex;
  align-items: center;
  justify-content: space-between;

  ${({ theme, hasError }) =>
    hasError &&
    css`
      border-color: ${theme.colors["base-error"]};
    `}
`

export const InputStyled = styled.input`
  flex: 1;
  height: 100%;
  width: 100%;
  background: none;
  border: none;
  outline: none;
  font-size: 1.4rem;
  padding: 0 0.8rem;
  color: ${({ theme }) => theme.colors["base-text"]};

  &::placeholder {
    color: ${({theme}) => theme.colors["base-label"]};
  }
`

export const OptionalText = styled.p`
  font-size: 1.2rem;
  margin-right: 0.75rem;
  font-style: italic;
  color: ${({theme}) => theme.colors["base-label"]};
`