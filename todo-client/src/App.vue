<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import axios from 'axios';

const todos = ref([]);
const name = ref('');
const deadline = ref('');
const time = ref('');
const message = ref('');

const input_content = ref('');
const input_deadline = ref('');
const input_time = ref('');

const todos_asc = computed(() =>
  todos.value.sort((a, b) => {
    return a.createdAt - b.createdAt;
  })
);

let socket = new WebSocket(`ws://127.0.0.1:8000/ws`);

socket.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.event === 'Send') {
    console.log('Received message:', data.message);
    message.value = data.message;
  }
};

socket.onopen = () => {
  console.log('WebSocket connection is open.');
};
socket.onclose = (event) => {
  console.log('WebSocket connection is closed.', event);
};
socket.onerror = (error) => {
  console.error('WebSocket error:', error);
};

watch(
  // ====================    delete
  todos,
  (newVal) => {},
  {
    deep: true,
  }
);

const addTodo = async () => {
  if (input_content.value.trim() === '') {
    return;
  }
  const inputDateTime = `${input_deadline.value}T${input_time.value}:00`;
  const deadlineDate = new Date(inputDateTime);
  deadlineDate.setUTCHours(deadlineDate.getUTCHours());
  console.log(input_time.value);
  const newTodo = {
    body: input_content.value,
    completed: false,
    deadline: deadlineDate,
  };
  await fetchAddTodo(newTodo);
  await fetchData();
};

const removeTodo = async (todo) => {
  await fetchDeleteTodo(todo);
  await fetchData();
};

const editTodo = async (todo) => {
  await fetchEditTodo(todo);
  // await fetchData();
};

onMounted(() => {
  fetchData();
  socket.onopen = () => {
    console.log('Connected to the server');
  };
});

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

const formatDate = (date) => {
  const options = {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
  };
  const adjustedDate = new Date(date);
  adjustedDate.setHours(adjustedDate.getHours());
  return adjustedDate.toLocaleDateString('en-US', options);
};
</script>

<template>
  <main class="app">
    <section class="greeting">
      <h2 class="title">What's up</h2>
    </section>

    <section class="create-todo">
      <h3>CREATE A TODO</h3>

      <form id="new-todo-form" @submit.prevent="addTodo">
        <h4>What's on your todo list?</h4>
        <input
          type="text"
          name="content"
          id="content"
          placeholder="e.g. make a To Do"
          v-model="input_content"
        />
        <input
          type="date"
          name="content"
          id="deadline"
          v-model="input_deadline"
        />
        <input type="time" name="time" id="time" v-model="input_time" />
        <input type="submit" value="Add todo" />
      </form>
    </section>

    <section class="todo-list">
      <h3>TODO LIST</h3>
      <div class="list" id="todo-list">
        <div class="error-message" v-if="message">{{ message }}</div>
        <div
          v-for="todo in todos_asc"
          :class="`todo-item ${todo.done && 'done'}`"
        >
          <label>
            <input
              type="checkbox"
              v-model="todo.completed"
              @change="editTodo(todo)"
            />
            <span :class="`bubble personal`"></span>
          </label>
          <div class="todo-content">
            <input type="text" v-model="todo.body" on />
            <span class="deadline">{{ formatDate(todo.deadline) }}</span>
            <!-- <input type="date" v-model="todo.deadline" /> -->
          </div>
          <div class="actions">
            <button class="delete" @click="removeTodo(todo.id)">Delete</button>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>
