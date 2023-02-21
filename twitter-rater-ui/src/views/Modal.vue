<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <slot name="header"> Disclaimer </slot>
      </header>

      <section class="modal-body">
        <slot name="body">
          By proceeding to use this application, you consent to being a subject
          in a study by team of researchers from University of Oulu. Your
          Twitter information (only public accounts), results, and feedback will
          be stored. The collected Twitter information is limited to public data
          available via Twitter API. The stored data will be deleted after the
          study.
        </slot>
      </section>

      <footer class="modal-footer">
        <slot name="footer">
          <!-- This is the default footer! -->
        </slot>
        <button type="button" class="btn-green" @click="close">Accept</button>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: "Modal",
  methods: {
    close() {
      this.$emit("close");
    },
  },
};
</script>
<style>
.modal-backdrop {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: #ffffff;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
  max-width: 70%;
}

.modal-footer {
  padding: 15px;
  display: flex;
  max-width: 40%;
  margin: auto;
}

.modal-header {
  padding: 15px;
  display: flex;
  margin: 0;
  position: relative;
  border-bottom: 1px solid #eeeeee;
  color: #4aae9b;
  justify-content: center;
}

.modal-footer {
  border-top: 1px solid #eeeeee;
  flex-direction: column;
  justify-content: flex-end;
}

.modal-body {
  position: relative;
  padding: 25px;
  text-align: justify;
}

.btn-close {
  position: absolute;
  top: 0;
  right: 0;
  border: none;
  font-size: 20px;
  padding: 10px;
  cursor: pointer;
  font-weight: bold;
  color: #4aae9b;
  background: transparent;
}

.btn-green {
  color: white;
  background: #4aae9b;
  border: 1px solid #4aae9b;
  border-radius: 2px;
  padding: 10px;
}
</style>
