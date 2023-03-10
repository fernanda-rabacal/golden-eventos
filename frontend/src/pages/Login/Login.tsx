import { FormContainer, KeepConnectedContainer, LoginContainer } from "./styles";
import { useState } from "react";
import { Eye, EyeSlash } from "phosphor-react";
import { useTheme } from "styled-components";
import { Input } from "../../components/Input";
import { Button } from "../../components/Button";
import { useForm } from "react-hook-form";

interface ILogin {
  email: string;
  password: string;
}

export function LoginPage() {
  const [showPassword, setShowPassword] = useState(false);
  const { register, handleSubmit } = useForm<ILogin>()
  
  const { colors } = useTheme()

  function login(data: ILogin){
    alert(`Tentei fazer login no email ${data.email}`)
  }

  const handleClickShowPassword = () => {
		setShowPassword((prevValue) => !prevValue);
	};

  document.title = "Login - Golden Eventos"

  return(
    <LoginContainer className="container">
      <h1>Acesse sua conta</h1>
      <FormContainer onSubmit={handleSubmit(login)}>
        <div>
          <label htmlFor="email">Email</label>
          <Input type="email" id="email" required {...register('email')}/>
        </div>
        <div>
          <label htmlFor="password">Senha</label>
          <Input type={showPassword ? "text" : "password"}  id="password" required {...register('password')}/>
          {
            showPassword ? 
            <EyeSlash size={22} onClick={handleClickShowPassword} color={colors["base-yellow"]}/> :
            <Eye size={22} onClick={handleClickShowPassword} color={colors["base-label"]}/>
          }
        </div>
        <KeepConnectedContainer>
          <input type="checkbox" id="keep-connect" />
          <label htmlFor="keep-connect">Mantenha-me conectado</label>
        </KeepConnectedContainer>

        <Button>Login</Button>
        <p>Esqueceu sua senha? <a href="#">Clique aqui</a></p>

        <hr />
        <p className="register">Não possui conta? <a href="#">Cadastre-se!</a></p>
      </FormContainer>
    </LoginContainer>
  )
}