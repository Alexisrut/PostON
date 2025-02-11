<script setup>
  import TitleView from './Title.vue';
  import ExplLeftView from './ExplLeft.vue';
  import ExplRightView from './ExplRight.vue';
  import FAQView from './FAQ.vue';
  import ConnectUsView from './ConnectUs.vue';
</script>

<template>
    <div class="container">
        <div class="section">
            <TitleView />
        </div>
        
        <div class="section">
            <ExplLeftView />
        </div>
        
        <div class="section">
            <ExplRightView />
        </div>
        
        <div class="section">
            <FAQView />
        </div>

        <div class="section">
            <ConnectUsView />
        </div>
    </div>
</template>

<script>
export default {
  // Your component logic
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  width: 100%;
  padding: 20px 0;
}

.section {
  width: 100%;
  max-width: 1440px; /* Adjust this value based on your design needs */
  margin: 0 auto;
  padding: 25px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Optional: Add responsive breakpoints */
@media (max-width: 768px) {
  .section {
    padding: 30px 15px;
    max-width: 100%;
  }
}

@media (max-width: 480px) {
  .section {
    padding: 20px 10px;
  }
}
</style>