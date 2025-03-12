<template>
  <div v-if="isVisible" class="modal-overlay" @click.self="closeModal">
    <div class="modal-content">
      <slot></slot>
      <button class="close-btn" @click="closeModal">关闭</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "CustomModal", // 原 "Modal"，改为 "CustomModal" 以符合 Vue 规范
  props: {
    isVisible: Boolean, // 通过 prop 控制是否显示模态框
  },
  emits: ["close"], // 定义 close 事件
  methods: {
    closeModal() {
      this.$emit("close"); // 触发关闭事件
    }
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 300px;
  text-align: center;
}

.close-btn {
  margin-top: 10px;
  padding: 8px 16px;
  background: #42b983;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 4px;
}

.close-btn:hover {
  background: #368f6e;
}
</style>
