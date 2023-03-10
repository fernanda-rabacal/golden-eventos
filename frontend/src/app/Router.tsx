import { Routes, Route, Navigate } from "react-router-dom";
import { DefaultLayout } from "../layouts/DefaultLayout";
import { LoginPage } from "../pages/Login/Login";

export function Router() {
  return(
    <Routes>
      <Route path="/" element={<DefaultLayout />}>
        <Route path="/" element={<Navigate replace to="/login" />} />
        <Route path="/login" element={<LoginPage />}/>
      </Route>
    </Routes>
  )
}