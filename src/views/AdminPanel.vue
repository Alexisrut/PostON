<template>
    <div class="registration-container">
        <div class="registration-wrapper">
            <div class="registration-form">
                <Admin />
            </div>
            
            <div class="registration-image">
                <img src="../assets/person_with_phone.png" class="centered-image">
            </div>
        </div>
    </div>
</template>


<script>
import Admin from '../components/AdminPanel.vue'

export default {
  components: {
    Admin
  }
}
</script>

<style scoped>
.registration-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 2rem;
  background-color: #f5f5f5; /* Optional background color */
}

.registration-wrapper {
  display: flex;
  gap: 4rem;
  max-width: 1200px;
  width: 100%;
  align-items: center;
}

.registration-form {
  flex: 1;
  max-width: 500px; /* Adjust based on your form width */
}

.registration-image {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.centered-image {
  max-width: 100%;
  height: auto;
  max-height: 600px; /* Adjust based on your image aspect ratio */
  object-fit: contain;
}

/* Responsive layout */
@media (max-width: 992px) {
  .registration-wrapper {
    flex-direction: column;
    gap: 2rem;
    text-align: center;
  }

  .registration-form {
    width: 100%;
    max-width: 100%;
    padding: 0 1rem;
  }

  .registration-image {
    width: 80%;
    margin: 0 auto;
  }
}

@media (max-width: 576px) {
  .registration-container {
    padding: 1rem;
  }
  
  .registration-image {
    width: 100%;
  }
}
</style>