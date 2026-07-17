import {BrowserRouter, Routes, Route, Link} from 'react-router-dom'; 
import Tasks from './pages/Tasks';

function App() {
  return(
    <BrowserRouter>
      <div className = "min-h-screen bg-slate-900 text-slate-100 p-8 font-sans">
        <h1 className = "text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-purple-500 tracking-tight"> Logisync Relocation Manager</h1>
        <nav className="mt-4 space-x-6">
          <Link to = "/" className = "text-indigo-400 font-bold hover:text-indigo-300 transition">Tasks</Link>
          <Link to = "/assets" className = "text-slate-400 hover:text-white transition">Assets</Link>
        </nav>


      

      <Routes>
        <Route path = "/" element = {<Tasks/>}/>
        <Route path = "/assets" element = {<h2>Assets Page coming soon</h2>}/>
      </Routes>

      </div>
    
    </BrowserRouter>
  );
}
export default App;