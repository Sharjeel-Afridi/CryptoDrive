import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import Auth from './components/Auth'
import { createBrowserRouter,RouterProvider } from 'react-router-dom'
import './index.css'

const appRouter = createBrowserRouter([

  {
    
    "path": "/",
    "element": <Auth />
    
  },
  {
    "path": "/home",
    "element": <App />
  }
  
  ]
)




ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={appRouter}/>
);
