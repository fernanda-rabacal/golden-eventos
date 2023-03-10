import styled from "styled-components";

export const ButtonContainer = styled.button`
  width: "75%";
  align-self: center;
  padding: 1.7rem 2.8rem;
  font-weight: 700;
  color: ${({ theme }) => theme.colors.white};
  background: ${({ theme }) => theme.colors["base-yellow"]};
  font-size: ${({ theme }) => theme.textSizes["text-regular-m"]};
  border-radius: 6px;
  margin-top: 1.5rem;
  text-transform: uppercase;
  transition: 0.4s;
  line-height: 1.3rem;

  &:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }

  &:not(:disabled):hover {
    background: ${({ theme }) => theme.colors["brand-yellow-dark"]};
  }

  @media(max-width: 500px){
    font-size: 1.6rem;
  }
`;
