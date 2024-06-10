import axios from 'axios';

const fetchData = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/todos/');
    todos.value.length = 0;
    todos.value.push(...response.data);
  } catch (error) {
    console.log(error);
  }
};

const fetchAddTodo = async (todo) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/todos/', todo);
  } catch (error) {
    console.log(error);
  }
};

const fetchEditTodo = async (todo) => {
  // console.log(todo);
  try {
    const response = await axios.patch(
      `http://127.0.0.1:8000/api/todos/${todo.id}/`,
      todo
    );
  } catch (error) {
    console.log(error);
  }
};

const fetchDeleteTodo = async (id) => {
  try {
    await axios.delete(`http://127.0.0.1:8000/api/todos/${id}/`);
  } catch (error) {
    console.log(error);
  }
};

export { fetchDeleteTodo, fetchEditTodo, fetchAddTodo, fetchData };
