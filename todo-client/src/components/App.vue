<script setup>
import { ref, onMounted } from 'vue';

const todoTitle = ref('');
const deadline = ref('');
const todoList = ref([]);

onMounted(() => {
  console.log('mounted', todoList.value);
});

const addTodo = () => {
  if (todoTitle.value === '') {
    alert('Please enter a todo');
    return;
  }
  const newTodo = {
    title: todoTitle.value,
    done: false,
    deadline: deadline.value,
  };
  todoList.value.push(newTodo);
  console.log(todoList.value);
  todoTitle.value = '';
  deadline.value = '';
};

const handleDelete = (todo) => {
  const index = todoList.value.indexOf(todo);
  todoList.value.splice(index, 1);
};
</script>

<template>
  <main class="app">
    <section class="greeting">
      <h2 class="title">Create To do</h2>
    </section>
    <section class="create-todo ">    
    <form @submit.prevent="addTodo">
        <label
          >What is your To Do:
          <input type="text" v-model="todoTitle" placeholder="add todo here" />
        </label>
        <label
          >What is a deadline:
          <input type="date" v-model="deadline" />
        </label>
        <button type="submit">Add To Do</button>
      </form>
    </section>
    <section class="todo-list">
      <h3>TO DO LIST</h3>
      <div class="list">
        <div
          v-for="todo in todoList"
          :class="`todo-item ${todo.done && 'done'}`"
        >
        <label>
          <input type="checkbox" value="personal" v-model="todo.done"></input>
          <span :class="`buble personal`"></span>
        </label>
          <input class="todo content" type="text" v-model="todo.title"/>
          <input class="todo content" type="date" v-model="todo.deadline"/>
          <div class="actions">
            <button type="button" class="delete" @click="handleDelete(todo)">
              DELETE
            </button>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>
