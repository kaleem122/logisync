import TaskCard from "./components/TaskCard"
import TaskForm from "./components/TaskForm"
import {useState, useEffect} from 'react';


function App(){

  const [tasks, setTasks] = useState([])

  useEffect(() => {
    fetch("http://localhost:8000/tasks")
    .then(response => response.json())
    .then(data => setTasks(data));
  }, []);
  function handleTaskAdded(newTask){
    setTasks([...tasks, newTask]);
  }
  return(
    <div>
      <h1>Logisync Relocation Manager</h1>
      <TaskForm onTaskAdded = {handleTaskAdded}/>
      {tasks.map(task => (
        <TaskCard key = {task.id} action = {task.action} status = {task.status} />
      ))}

    </div>
  )
}
export default App