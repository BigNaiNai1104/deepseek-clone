<template>
    <div class="chat-container">
      <!-- 左侧导航栏 -->
      <div class="sidebar">
        <img src="@/assets/history-icon.png" alt="历史记录" class="history-icon" @click="toggleHistory" />
        <img src="@/assets/logout-icon.png" alt="退出" class="logout-icon" @click="logout" />
      </div>
  
      <!-- 聊天主界面 -->
      <div class="chat-main">
        <h1 class="chat-title">我是 DeepSeek，很高兴见到你！</h1>
        <p class="chat-subtitle">我可以帮你写代码、读文件、写作各种创意内容，清晰你的任务交给我吧~</p>
        
        <div class="chat-box">
          <div v-for="(message, index) in messages" :key="index" class="message">
            <strong>{{ message.user }}:</strong> {{ message.text }}
          </div>
        </div>
  
        <!-- 输入框区域 -->
        <div class="input-area">
          <input v-model="newMessage" placeholder="输入消息..." @keyup.enter="sendMessage" />
          <button @click="sendMessage">发送</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  
  export default {
    setup() {
      const messages = ref([]);
      const newMessage = ref("");
      const showHistory = ref(false);
      const router = useRouter();
  
      const sendMessage = () => {
        if (newMessage.value.trim() !== "") {
          messages.value.push({ user: "Me", text: newMessage.value });
          newMessage.value = "";
        }
      };
  
      const logout = () => {
        localStorage.removeItem("token");
        router.push("/login");
      };
  
      const toggleHistory = () => {
        showHistory.value = !showHistory.value;
        console.log("历史记录打开状态:", showHistory.value);
      };
  
      return {
        messages,
        newMessage,
        sendMessage,
        logout,
        toggleHistory,
        showHistory,
      };
    },
  };
  </script>
  
  <style scoped>
  .chat-container {
    display: flex;
    height: 100vh;
    background-color: #f8f9fa;
  }
  
  /* 左侧导航栏样式 */
  .sidebar {
    width: 80px;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-right: 1px solid #ddd;
    padding-top: 20px;
    gap: 15px;
  }
  
  .history-icon, .logout-icon {
    width: 40px;
    height: 40px;
    cursor: pointer;
  }
  
  .chat-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 20px;
    text-align: center;
  }
  
  .chat-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 5px;
  }
  
  .chat-subtitle {
    font-size: 16px;
    color: #666;
    margin-bottom: 20px;
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
  