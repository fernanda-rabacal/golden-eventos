import { Outlet } from "react-router-dom";
import { Footer } from "../../components/Footer/Footer";
import { Header } from "../../components/Header/Header";
import { LayoutContainer, TopContainer } from "./styles";

export function DefaultLayout() {
  return(
    <LayoutContainer>
      <TopContainer>
        <Header />
        <Outlet />
      </TopContainer>
      
      <Footer />
    </LayoutContainer>

  )
}