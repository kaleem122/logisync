import TaskCard from "../components/TaskCard"
import TaskForm from "../components/TaskForm"
import {useState, useEffect} from 'react';


function Tasks(){

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
    
      <div className = "max-w-3xl mx-auto">
        <h2 className= "text-2xl font-bold text-white mb-6">Your Tasks</h2>
        
        
      <TaskForm onTaskAdded = {handleTaskAdded}/>

      <div className="grid grid-cols-1 gap-6 mt-8">
        {tasks.map(task => (
          <TaskCard key = {task.id} action = {task.action} status={task.status}/>
        ))}
      </div>
      
      </div>
    
  )
}
export default Tasks