<template>
  <div id="webcrumbs">
    <div class="w-[900px] bg-white rounded-xl shadow-lg p-8 flex flex-row">
      <div>
        <div class="mb-8">
          <h2 class="text-2xl font-bold mb-2 dark-text">Создание аккаунта</h2>
          <p class="text-neutral-600">Зарегестрируйте сегодня, чтобы получить доступ к всем возможностям PostON!</p>
        </div>
        
        <!-- Error Message -->
        <div v-if="errorMessage" class="dark-text mb-4 p-4 bg-red-100 text-red-700 rounded-lg">
          {{ errorMessage }}
        </div>
        
        <!-- Success Message -->
        <div v-if="successMessage" class="dark-text mb-4 p-4 bg-green-100 text-green-700 rounded-lg">
          {{ successMessage }}
        </div>

        <form @submit.prevent="handleSubmit" class="space-y-6">
          <div class="flex gap-4">
            <div class="w-1/2">
              <label class="block text-sm font-medium mb-2 dark-text">Имя</label>
              <input v-model="formData.firstName" type="text" 
                    class="dark-text w-full px-4 py-2 rounded-lg border border-neutral-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 outline-none" 
                    required>
            </div>
            <div class="w-1/2">
              <label class="dark-text block text-sm font-medium mb-2">Фамилия</label>
              <input v-model="formData.lastName" type="text" 
                    class="dark-text w-full px-4 py-2 rounded-lg border border-neutral-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 outline-none" 
                    required>
            </div>
          </div>
          <div>
            <label class="dark-text block text-sm font-medium mb-2">Электронная почта</label>
            <input v-model="formData.email" type="email" 
                  class="dark-text w-full px-4 py-2 rounded-lg border border-neutral-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 outline-none" 
                  required>
          </div>
          <div>
            <label class="dark-text block text-sm font-medium mb-2">Пароль</label>
            <input v-model="formData.password" type="password" 
                  class="dark-text w-full px-4 py-2 rounded-lg border border-neutral-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 outline-none" 
                  required>
          </div>
          <div class="flex items-center gap-2">
            <input v-model="formData.agreement" type="checkbox" 
                  class="dark-text w-4 h-4 rounded border-neutral-300 text-blue-600 focus:ring-blue-500 transition duration-200" 
                  required>
            <label class="dark-text text-sm">Я согласен с <a href="#" class="text-blue-600">условиями использования</a></label>
            <p class="text-sm text-center mt-6 dark-text"> Don&#x27;t have an account yet? <a href="../signin" class="text-primary font-semibold">Register for free</a> </p> 
          </div>
          
          <button type="submit" 
                  :disabled="loading"
                  class="w-full bg-blue-600 text-white font-medium py-3 rounded-lg hover:bg-blue-700 active:bg-blue-800 transition duration-200 disabled:bg-blue-400 disabled:cursor-not-allowed">
            <span v-if="!loading">Создать аккаунт</span>
            <span v-else>Загрузка...</span>
          </button>
          <!-- Social login buttons remain unchanged -->
        </form>
      </div> 
      <div class="w-[50%] flex items-center justify-center pl-8"> 
            <img src="../assets/sitting.png">
      </div> 
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      formData: {
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        agreement: false
      },
      errorMessage: '',
      successMessage: '',
      loading: false
    };
  },
  methods: {
    async handleSubmit() {
      this.errorMessage = '';
      this.successMessage = '';
      this.loading = true;

      try {
        const response = await axios.post('http://localhost:8000/register', {
          first_name: this.formData.firstName,
          last_name: this.formData.lastName,
          email: this.formData.email,
          password: this.formData.password,
          agreement: this.formData.agreement
        });

        if (response.status === 201) {
          this.successMessage = 'Registration successful! Redirecting...';
          // Redirect to signin page after 2 seconds
          setTimeout(() => {
            window.location.href = response.data.redirect;
          }, 2000);
        }
      } catch (error) {
        if (error.response) {
          // The request was made and the server responded with a status code
          switch (error.response.status) {
            case 400:
              this.errorMessage = error.response.data.detail || 'Registration failed';
              break;
            case 500:
              this.errorMessage = 'Server error, please try again later';
              break;
            default:
              this.errorMessage = 'An unexpected error occurred';
          }
        } else {
          this.errorMessage = 'Network error, please check your connection';
        }
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
  @import url(https://fonts.googleapis.com/css2?family=Lato&display=swap);
  
  @import url(https://fonts.googleapis.com/css2?family=Open+Sans&display=swap);
  
  @import url(https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css);
  
  /*! tailwindcss v3.4.11 | MIT License | https://tailwindcss.com*/
  .pl-8 {
    padding-left: 8px;
  }
  .dark-text {
    color: #000;
  }
  #webcrumbs .font-semibold {
    font-weight: 600;
  }
  #webcrumbs .text-primary {
    --tw-text-opacity: 1;
    color: rgb(97 27 248 / var(--tw-text-opacity));
  }
  *,
  :after,
  :before {
    border: 0 solid #e5e7eb;
    box-sizing: border-box;
  }
  :after,
  :before {
    --tw-content: "";
  }
  :host,
  html {
    line-height: 1.5;
    -webkit-text-size-adjust: 100%;
    font-family:
      Open Sans,
      ui-sans-serif,
      system-ui,
      sans-serif,
      Apple Color Emoji,
      Segoe UI Emoji,
      Segoe UI Symbol,
      Noto Color Emoji;
    font-feature-settings: normal;
    font-variation-settings: normal;
    -moz-tab-size: 4;
    tab-size: 4;
    -webkit-tap-highlight-color: transparent;
  }
  body {
    line-height: inherit;
    margin: 0;
  }
  hr {
    border-top-width: 1px;
    color: inherit;
    height: 0;
  }
  abbr:where([title]) {
    text-decoration: underline dotted;
  }
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    font-size: inherit;
    font-weight: inherit;
  }
  a {
    color: inherit;
    text-decoration: inherit;
  }
  b,
  strong {
    font-weight: bolder;
  }
  code,
  kbd,
  pre,
  samp {
    font-family:
      ui-monospace,
      SFMono-Regular,
      Menlo,
      Monaco,
      Consolas,
      Liberation Mono,
      Courier New,
      monospace;
    font-feature-settings: normal;
    font-size: 1em;
    font-variation-settings: normal;
  }
  small {
    font-size: 80%;
  }
  sub,
  sup {
    font-size: 75%;
    line-height: 0;
    position: relative;
    vertical-align: baseline;
  }
  sub {
    bottom: -0.25em;
  }
  sup {
    top: -0.5em;
  }
  table {
    border-collapse: collapse;
    border-color: inherit;
    text-indent: 0;
  }
  button,
  input,
  optgroup,
  select,
  textarea {
    color: inherit;
    font-family: inherit;
    font-feature-settings: inherit;
    font-size: 100%;
    font-variation-settings: inherit;
    font-weight: inherit;
    letter-spacing: inherit;
    line-height: inherit;
    margin: 0;
    padding: 0;
  }
  button,
  select {
    text-transform: none;
  }
  button,
  input:where([type="button"]),
  input:where([type="reset"]),
  input:where([type="submit"]) {
    -webkit-appearance: button;
    background-color: transparent;
    background-image: none;
  }
  :-moz-focusring {
    outline: auto;
  }
  :-moz-ui-invalid {
    box-shadow: none;
  }
  progress {
    vertical-align: baseline;
  }
  ::-webkit-inner-spin-button,
  ::-webkit-outer-spin-button {
    height: auto;
  }
  [type="search"] {
    -webkit-appearance: textfield;
    outline-offset: -2px;
  }
  ::-webkit-search-decoration {
    -webkit-appearance: none;
  }
  ::-webkit-file-upload-button {
    -webkit-appearance: button;
    font: inherit;
  }
  summary {
    display: list-item;
  }
  blockquote,
  dd,
  dl,
  figure,
  h1,
  h2,
  h3,
  h4,
  h5,
  h6,
  hr,
  p,
  pre {
    margin: 0;
  }
  fieldset {
    margin: 0;
  }
  fieldset,
  legend {
    padding: 0;
  }
  menu,
  ol,
  ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  dialog {
    padding: 0;
  }
  textarea {
    resize: vertical;
  }
  input::placeholder,
  textarea::placeholder {
    color: #9ca3af;
    opacity: 1;
  }
  [role="button"],
  button {
    cursor: pointer;
  }
  :disabled {
    cursor: default;
  }
  audio,
  canvas,
  embed,
  iframe,
  img,
  object,
  svg,
  video {
    display: block;
    vertical-align: middle;
  }
  img,
  video {
    height: auto;
    max-width: 100%;
  }
  [hidden] {
    display: none;
  }
  *,
  :after,
  :before {
    --tw-border-spacing-x: 0;
    --tw-border-spacing-y: 0;
    --tw-translate-x: 0;
    --tw-translate-y: 0;
    --tw-rotate: 0;
    --tw-skew-x: 0;
    --tw-skew-y: 0;
    --tw-scale-x: 1;
    --tw-scale-y: 1;
    --tw-pan-x: ;
    --tw-pan-y: ;
    --tw-pinch-zoom: ;
    --tw-scroll-snap-strictness: proximity;
    --tw-gradient-from-position: ;
    --tw-gradient-via-position: ;
    --tw-gradient-to-position: ;
    --tw-ordinal: ;
    --tw-slashed-zero: ;
    --tw-numeric-figure: ;
    --tw-numeric-spacing: ;
    --tw-numeric-fraction: ;
    --tw-ring-inset: ;
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgba(59, 130, 246, 0.5);
    --tw-ring-offset-shadow: 0 0 #0000;
    --tw-ring-shadow: 0 0 #0000;
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;
    --tw-blur: ;
    --tw-brightness: ;
    --tw-contrast: ;
    --tw-grayscale: ;
    --tw-hue-rotate: ;
    --tw-invert: ;
    --tw-saturate: ;
    --tw-sepia: ;
    --tw-drop-shadow: ;
    --tw-backdrop-blur: ;
    --tw-backdrop-brightness: ;
    --tw-backdrop-contrast: ;
    --tw-backdrop-grayscale: ;
    --tw-backdrop-hue-rotate: ;
    --tw-backdrop-invert: ;
    --tw-backdrop-opacity: ;
    --tw-backdrop-saturate: ;
    --tw-backdrop-sepia: ;
    --tw-contain-size: ;
    --tw-contain-layout: ;
    --tw-contain-paint: ;
    --tw-contain-style: ;
  }
  ::backdrop {
    --tw-border-spacing-x: 0;
    --tw-border-spacing-y: 0;
    --tw-translate-x: 0;
    --tw-translate-y: 0;
    --tw-rotate: 0;
    --tw-skew-x: 0;
    --tw-skew-y: 0;
    --tw-scale-x: 1;
    --tw-scale-y: 1;
    --tw-pan-x: ;
    --tw-pan-y: ;
    --tw-pinch-zoom: ;
    --tw-scroll-snap-strictness: proximity;
    --tw-gradient-from-position: ;
    --tw-gradient-via-position: ;
    --tw-gradient-to-position: ;
    --tw-ordinal: ;
    --tw-slashed-zero: ;
    --tw-numeric-figure: ;
    --tw-numeric-spacing: ;
    --tw-numeric-fraction: ;
    --tw-ring-inset: ;
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgba(59, 130, 246, 0.5);
    --tw-ring-offset-shadow: 0 0 #0000;
    --tw-ring-shadow: 0 0 #0000;
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;
    --tw-blur: ;
    --tw-brightness: ;
    --tw-contrast: ;
    --tw-grayscale: ;
    --tw-hue-rotate: ;
    --tw-invert: ;
    --tw-saturate: ;
    --tw-sepia: ;
    --tw-drop-shadow: ;
    --tw-backdrop-blur: ;
    --tw-backdrop-brightness: ;
    --tw-backdrop-contrast: ;
    --tw-backdrop-grayscale: ;
    --tw-backdrop-hue-rotate: ;
    --tw-backdrop-invert: ;
    --tw-backdrop-opacity: ;
    --tw-backdrop-saturate: ;
    --tw-backdrop-sepia: ;
    --tw-contain-size: ;
    --tw-contain-layout: ;
    --tw-contain-paint: ;
    --tw-contain-style: ;
  }
  #webcrumbs .absolute {
    position: absolute;
  }
  #webcrumbs .relative {
    position: relative;
  }
  #webcrumbs .inset-0 {
    inset: 0;
  }
  #webcrumbs .mb-2 {
    margin-bottom: 6px;
  }
  #webcrumbs .mb-4 {
    margin-bottom: 6px;
  }
  #webcrumbs .mb-8 {
    margin-bottom: 24px;
  }
  #webcrumbs .ml-1 {
    margin-left: 3px;
  }
  #webcrumbs .block {
    display: block;
  }
  #webcrumbs .flex {
    display: flex;
  }
  #webcrumbs .h-4 {
    height: 12px;
  }
  #webcrumbs .w-1\/2 {
    width: 50%;
  }
  #webcrumbs .w-4 {
    width: 12px;
  }
  #webcrumbs .w-\[900px\] {
    width: 950px;
  }
  #webcrumbs .w-full {
    width: 100%;
  }
  #webcrumbs .flex-1 {
    flex: 1 1 0%;
  }
  #webcrumbs .flex-row {
    flex-direction: row;
  }
  #webcrumbs .items-center {
    align-items: center;
  }
  #webcrumbs .justify-center {
    justify-content: center;
  }
  #webcrumbs .justify-between {
    justify-content: space-between;
  }
  #webcrumbs .gap-2 {
    gap: 6px;
  }
  #webcrumbs .gap-4 {
    gap: 12px;
  }
  #webcrumbs :is(.space-y-6 > :not([hidden]) ~ :not([hidden])) {
    --tw-space-y-reverse: 0;
    margin-bottom: calc(18px * var(--tw-space-y-reverse));
    margin-top: calc(18px * (1 - var(--tw-space-y-reverse)));
  }
  #webcrumbs .rounded {
    border-radius: 12px;
  }
  #webcrumbs .rounded-lg {
    border-radius: 24px;
  }
  #webcrumbs .rounded-xl {
    border-radius: 36px;
  }
  #webcrumbs .border {
    border-width: 1px;
  }
  #webcrumbs .border-t {
    border-top-width: 1px;
  }
  #webcrumbs .border-neutral-300 {
    --tw-border-opacity: 1;
    border-color: rgb(202 202 202 / var(--tw-border-opacity));
  }
  #webcrumbs .bg-blue-600 {
    --tw-bg-opacity: 1;
    background-color: rgb(37 99 235 / var(--tw-bg-opacity));
  }
  #webcrumbs .bg-white {
    --tw-bg-opacity: 1;
    background-color: rgb(255 255 255 / var(--tw-bg-opacity));
  }
  #webcrumbs .p-8 {
    padding: 24px;
  }
  #webcrumbs .px-4 {
    padding-left: 12px;
    padding-right: 12px;
  }
  #webcrumbs .py-2 {
    padding-bottom: 6px;
    padding-top: 6px;
  }
  #webcrumbs .py-2\.5 {
    padding-bottom: 7.5px;
    padding-top: 7.5px;
  }
  #webcrumbs .py-3 {
    padding-bottom: 9px;
    padding-top: 9px;
  }
  #webcrumbs .text-center {
    text-align: center;
  }
  #webcrumbs .text-2xl {
    font-size: 39px;
    line-height: 50.7px;
  }
  #webcrumbs .text-sm {
    font-size: 22.75px;
    line-height: 34.125px;
  }
  #webcrumbs .text-xl {
    font-size: 32.5px;
    line-height: 45.5px;
  }
  #webcrumbs .font-bold {
    font-weight: 700;
  }
  #webcrumbs .font-medium {
    font-weight: 500;
  }
  #webcrumbs .text-blue-600 {
    --tw-text-opacity: 1;
    color: rgb(37 99 235 / var(--tw-text-opacity));
  }
  #webcrumbs .text-neutral-500 {
    --tw-text-opacity: 1;
    color: rgb(153 153 153 / var(--tw-text-opacity));
  }
  #webcrumbs .text-neutral-600 {
    --tw-text-opacity: 1;
    color: rgb(127 127 127 / var(--tw-text-opacity));
  }
  #webcrumbs .text-white {
    --tw-text-opacity: 1;
    color: rgb(255 255 255 / var(--tw-text-opacity));
  }
  #webcrumbs .shadow-lg {
    --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1),
      0 4px 6px -4px rgba(0, 0, 0, 0.1);
    --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color),
      0 4px 6px -4px var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000),
      var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
  }
  #webcrumbs .outline-none {
    outline: 2px solid transparent;
    outline-offset: 2px;
  }
  #webcrumbs .transition {
    transition-duration: 0.15s;
    transition-property: color, background-color, border-color,
      text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter,
      backdrop-filter;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  }
  #webcrumbs .duration-200 {
    transition-duration: 0.2s;
  }
  #webcrumbs {
    font-family: Open Sans !important;
    font-size: 26px !important;
  }
  #webcrumbs .hover\:bg-blue-700:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(29 78 216 / var(--tw-bg-opacity));
  }
  #webcrumbs .hover\:bg-neutral-50:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(247 247 247 / var(--tw-bg-opacity));
  }
  #webcrumbs .hover\:text-blue-700:hover {
    --tw-text-opacity: 1;
    color: rgb(29 78 216 / var(--tw-text-opacity));
  }
  #webcrumbs .focus\:border-transparent:focus {
    border-color: transparent;
  }
  #webcrumbs .focus\:ring-2:focus {
    --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0
      var(--tw-ring-offset-width) var(--tw-ring-offset-color);
    --tw-ring-shadow: var(--tw-ring-inset) 0 0 0
      calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);
    box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow),
      var(--tw-shadow, 0 0 #0000);
  }
  #webcrumbs .focus\:ring-blue-500:focus {
    --tw-ring-opacity: 1;
    --tw-ring-color: rgb(59 130 246 / var(--tw-ring-opacity));
  }
  #webcrumbs .active\:bg-blue-800:active {
    --tw-bg-opacity: 1;
    background-color: rgb(30 64 175 / var(--tw-bg-opacity));
  }
  
</style>