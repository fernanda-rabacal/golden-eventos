import { ButtonHTMLAttributes, ReactNode } from "react";
import { ButtonContainer } from "./styles";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement>{
  children: string | ReactNode
}

export function Button({children, ...props}: ButtonProps){
  return(
    <ButtonContainer 
      onClick={props.onClick} 
      className={props.className}
    >
      {children}
    </ButtonContainer>
  )
}