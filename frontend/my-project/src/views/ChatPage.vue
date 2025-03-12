<template>
    <div class="chat-container">
      <!-- 头部导航栏 -->
      <header class="header">
        <div class="logo">DeepSeek</div>
        <div class="tagline">Your AI Assistant</div>
        <div class="user-settings">
          <img src="user-icon.png" alt="User Icon" class="user-icon" />
        </div>
      </header>
  
      <!-- 主体内容区 -->
      <main class="main-content">
        <div class="chat-history">
          <div v-for="(message, index) in messages" :key="index" :class="['message', message.type]">
            <div class="message-bubble" :class="message.type + '-bubble'">
              <markdown>{{ message.text }}</markdown>
            </div>
            <div class="actions" v-if="message.type === 'ai'">
              <button @click="copyToClipboard(message.text)">复制</button>
              <button @click="sendFeedback">反馈</button>
            </div>
          </div>
        </div>
      </main>
  
      <!-- 底部输入区 -->
      <footer class="footer">
        <textarea v-model="message" placeholder="输入消息..." rows="3"></textarea>
        <div class="footer-actions">
          <button @click="attachFile">附件</button>
          <button @click="viewHistory">历史</button>
          <button @click="sendMessage">发送</button>
        </div>
        <div class="model-version">模型版本：GPT-4</div>
      </footer>
    </div>
  </template>
  
  <script>
  import markdownIt from 'markdown-it';
  
  export default {
    data() {
      return {
        message: '',
        messages: [],
      };
    },
    methods: {
      copyToClipboard(text) {
        navigator.clipboard.writeText(text);
      },
      sendFeedback() {
        console.log('反馈发送成功！');
      },
      attachFile() {
        console.log('附件功能');
      },
      viewHistory() {
        console.log('查看历史');
      },
      sendMessage() {
        if (this.message.trim()) {
          // 将用户消息添加到消息列表
          this.messages.push({ type: 'user', text: this.message });
          this.message = '';
  
          // 模拟 AI 回复
          setTimeout(() => {
            this.messages.push({ type: 'ai', text: 'AI 回复：' + this.message });
          }, 1000);
        }
      },
    },
    components: {
      markdown: {
        functional: true,
        render(h, context) {
          const md = markdownIt();
          const renderedMarkdown = md.render(context.children[0]);
          return h('div', {
            domProps: {
              innerHTML: renderedMarkdown,
            },
          });
        },
      },
    },
  };
  </script>
  
  <style scoped>
  .chat-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    font-family: Arial, sans-serif;
  }
  
  /* 头部导航栏 */
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
  }
  
  .logo {
    font-size: 1.5rem;
    font-weight: bold;
  }
  
  .tagline {
    font-size: 1rem;
    font-style: italic;
  }
  
  .user-settings .user-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
  }
  
  /* 主体内容区 */
  .main-content {
    flex: 1;
    padding: 20px;
    overflow-y: auto;
    background-color: #f4f4f4;
  }
  
  .chat-history {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .message-bubble {
    max-width: 60%;
    padding: 10px;
    border-radius: 10px;
    font-size: 1rem;
  }
  
  .user-bubble {
    background-color: #42b983;
    color: white;
    align-self: flex-end;
  }
  
  .ai-bubble {
    background-color: #f2f2f2;
    color: black;
    align-self: flex-start;
  }
  
  .actions button {
    margin-top: 5px;
    padding: 5px;
    font-size: 0.8rem;
    background-color: #42b983;
    color: white;
    border-radius: 5px;
  }
  
  /* 底部输入区 */
  .footer {
    background-color: #fff;
    padding: 20px;
    border-top: 1px solid #ddd;
  }
  
  textarea {
    width: 100%;
    padding: 10px;
    font-size: 1rem;
    border-radius: 10px;
    border: 1px solid #ccc;
  }
  
  .footer-actions button {
    padding: 10px 20px;
    margin-right: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .footer-actions button:hover {
    background-color: #45a049;
  }
  
  .model-version {
    font-size: 0.8rem;
    color: #888;
    margin-top: 10px;
    text-align: center;
  }
  </style>
  