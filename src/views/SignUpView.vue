<script setup>
import SignUp from '../components/SignUpForm.vue'
</script>

<template>
  <main>
    <div class="container">
      <SignUp />
    </div>
  </main>
</template>

<style scoped>
main {
  background-color: #f5f5f5;
  min-height: 100vh;
  display: flex;
  align-items: flex-end;
  padding: 2rem;
}

.container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border-radius: 20px;
  border: 2px solid black;
  background-color: #f5f5f5; /* Optional background color */
}

.image-container {
  flex-shrink: 0;
  margin-top: auto; /* Pushes image to bottom */
}

.bottom-image {
  max-height: 400px; /* Adjust based on your needs */
  width: auto;
  max-width: 100%;
  object-fit: contain;
}

/* Responsive design */
@media (max-width: 768px) {
  main {
    padding: 1rem;
    align-items: center;
  }

  .container {
    flex-direction: column;
    align-items: center;
  }

  .image-container {
    order: -1; /* Move image above form on mobile */
    margin-top: 0;
    max-width: 300px;
  }
}
</style>