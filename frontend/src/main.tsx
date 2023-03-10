import React from 'react'
import ReactDOM from 'react-dom/client'
import { ThemeProvider } from 'styled-components'
import { Router } from './app/Router'
import { BrowserRouter } from 'react-router-dom'
import { GlobalStyle } from './styles/global'
import { defaultTheme } from './styles/themes/defaultTheme'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <ThemeProvider theme={ defaultTheme }>
      <BrowserRouter>
        <Router />
        <GlobalStyle />
      </BrowserRouter>
    </ThemeProvider>
  </React.StrictMode>,
)
