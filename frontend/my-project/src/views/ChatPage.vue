<template>
    <div class="chat-container">
      <div class="chat-box">
        <div v-for="(message, index) in messages" :key="index" class="message">
          <strong>{{ message.user }}:</strong> {{ message.text }}
        </div>
      </div>
      <div class="input-area">
        <input v-model="newMessage" placeholder="输入消息..." @keyup.enter="sendMessage" />
        <button @click="sendMessage">发送</button>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  
  export default {
    setup() {
      const socket = ref(null);  // 用于存储 WebSocket 连接
      const messages = ref([]);  // 存储消息
      const newMessage = ref("");  // 输入框中的新消息
  
      // 建立 WebSocket 连接
      socket.value = new WebSocket("ws://192.168.0.103:9000/ws");  // 修改为后端的 WebSocket 地址
  
      // 接收到的消息处理
      socket.value.onmessage = (event) => {
        messages.value.push({ user: "Server", text: event.data });
      };
  
      // 发送消息
      const sendMessage = () => {
        if (newMessage.value.trim() !== "") {
          socket.value.send(newMessage.value);  // 发送消息到服务器
          messages.value.push({ user: "Me", text: newMessage.value });
          newMessage.value = "";  // 清空输入框
        }
      };
  
      return {
        messages,
        newMessage,
        sendMessage,
      };
    },
  };
  </script>
  
  <style scoped>
  /* 样式保持不变 */
  .chat-container {
    display: flex;
    height: 100vh;
    background-color: #f8f9fa;
  }
  .chat-box {
    flex: 1;
    border: 1px solid #ccc;
    padding: 10px;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    overflow-y: auto;
    min-height: 300px;
    margin-bottom: 15px;
  }
  .input-area {
    display: flex;
    gap: 10px;
  }
  input {
    flex: 1;
    padding: 10px;
    border-radius: 4px;
    border: 1px solid #ccc;
  }
  button {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  </style>
  