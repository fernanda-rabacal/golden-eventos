import { HeaderContainer, LoginWrapper, SearchWrapper } from "./styles";
import { Input } from "../Input";
import { MagnifyingGlass } from "phosphor-react";
import { useTheme } from "styled-components";
import Logo from "../../assets/logo.svg";

export function Header() {
  const {colors} = useTheme()


  return(
    <HeaderContainer>
      <div className="logo-and-search">
        <img src={Logo} />
        <SearchWrapper>
          <MagnifyingGlass size={18} weight="bold" color={colors["base-yellow"]} />
          <Input type="search" placeholder="Encontre o evento que deseja.." />
        </SearchWrapper>
      </div>
      <LoginWrapper>
        <button>Faça Login</button>
        <button>Cadastre-se</button>
      </LoginWrapper>
    </HeaderContainer>
  )
}