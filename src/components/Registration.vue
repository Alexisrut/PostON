<template>
    <div id="webcrumbs">
        <div class="w-[900px] min-h-[600px] bg-white rounded-lg shadow-lg flex"> 
            <div class="w-[50%] px-12 py-8 flex flex-col justify-center"> 
                <h1 class="text-3xl font-title text-primary font-semibold mb-1"></h1> 
                <h2 class="text-4xl font-title font-bold mb-12 dark-text">Signin</h2> 
                <form class="flex flex-col gap-6" @submit.prevent="handleSubmit"> 
                    <div> 
                        <label class="block text-sm font-semibold mb-2 dark-text">Email</label> 
                        <input v-model="formData.email" type="email" placeholder="username@gmail.com" class="dark-text w-full p-3 border border-neutral-400 rounded-md" required/> 
                    </div> 
                    <div> 
                        <label class="block text-sm font-semibold mb-2 dark-text">Password</label> 
                        <input v-model="formData.password" type="password" placeholder="password" class="dark-text w-full p-3 border border-neutral-400 rounded-md" required/> 
                    </div> 
                    <a href="#" class="text-sm font-semibold text-primary mt-2">Forgot Password?</a>
                    <button :disabled="loading" class="mt-6 w-full bg-primary text-white py-3 rounded-md">{{ loading ? 'Signing in...' : 'Sign in' }}</button>
                </form> 
                <p class="text-sm text-center mt-6 dark-text"> Don&#x27;t have an account yet? <a href="../signup" class="text-primary font-semibold">Register for free</a> </p> 
            </div> 
            <div class="w-[50%] flex items-center justify-center"> 
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
          email: '',
          password: ''
        },
        loading: false,
        errorMessage: ''
      };
    },
    methods: {
      async handleSubmit() {
        this.loading = true;
        this.errorMessage = '';
        
        try {
          const response = await axios.post(
            'http://localhost:8000/signin',
            {
              email: this.formData.email,
              password: this.formData.password
            },
            {
              headers: {
                'Content-Type': 'application/json'
              }
            }
          );

          // Store token and redirect
          localStorage.setItem('access_token', response.data.access_token);
          this.$router.push(response.data.redirect);
          
        } catch (error) {
          this.errorMessage = error.response?.data?.detail || 'Login failed';
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
  .dark-text {
    color: #000;
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
  #webcrumbs .inset-y-0 {
    bottom: 0;
    top: 0;
  }
  #webcrumbs .right-0 {
    right: 0;
  }
  #webcrumbs .mx-4 {
    margin-left: 12px;
    margin-right: 12px;
  }
  #webcrumbs .my-6 {
    margin-top: 9px;
  }
  #webcrumbs .mb-1 {
    margin-bottom: 3px;
  }
  #webcrumbs .mb-12 {
    margin-bottom: 36px;
  }
  #webcrumbs .mb-2 {
    margin-bottom: 6px;
  }
  #webcrumbs .mr-2 {
    margin-right: 6px;
  }
  #webcrumbs .mt-2 {
    margin-top: 6px;
  }
  #webcrumbs .mt-6 {
    margin-top: 10px;
  }
  #webcrumbs .block {
    display: block;
  }
  #webcrumbs .flex {
    display: flex;
  }
  #webcrumbs .h-full {
    height: 100%;
  }
  #webcrumbs .min-h-\[600px\] {
    min-height: 600px;
  }
  #webcrumbs .w-\[50\%\] {
    width: 50%;
  }
  #webcrumbs .w-\[900px\] {
    width: 900px;
  }
  #webcrumbs .w-full {
    width: 100%;
  }
  #webcrumbs .flex-grow {
    flex-grow: 1;
  }
  #webcrumbs .flex-row {
    flex-direction: row;
  }
  #webcrumbs .flex-col {
    flex-direction: column;
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
  #webcrumbs .gap-4 {
    gap: 12px;
  }
  #webcrumbs .gap-6 {
    gap: 18px;
  }
  #webcrumbs .rounded-lg {
    border-radius: 24px;
  }
  #webcrumbs .rounded-md {
    border-radius: 18px;
  }
  #webcrumbs .rounded-r-lg {
    border-bottom-right-radius: 24px;
    border-top-right-radius: 24px;
  }
  #webcrumbs .border {
    border-width: 1px;
  }
  #webcrumbs .border-t {
    border-top-width: 1px;
  }
  #webcrumbs .border-neutral-400 {
    --tw-border-opacity: 1;
    border-color: rgb(177 177 177 / var(--tw-border-opacity));
  }
  #webcrumbs .bg-primary {
    --tw-bg-opacity: 1;
    background-color: rgb(97 27 248 / var(--tw-bg-opacity));
  }
  #webcrumbs .bg-white {
    --tw-bg-opacity: 1;
    background-color: rgb(255 255 255 / var(--tw-bg-opacity));
  }
  #webcrumbs .object-cover {
    object-fit: cover;
  }
  #webcrumbs .p-3 {
    padding: 9px;
  }
  #webcrumbs .px-12 {
    padding-left: 36px;
    padding-right: 36px;
  }
  #webcrumbs .px-4 {
    padding-left: 12px;
    padding-right: 12px;
  }
  #webcrumbs .py-2 {
    padding-bottom: 6px;
    padding-top: 6px;
  }
  #webcrumbs .py-3 {
    padding-bottom: 9px;
    padding-top: 9px;
  }
  #webcrumbs .py-8 {
    padding-bottom: 24px;
    padding-top: 24px;
  }
  #webcrumbs .text-center {
    text-align: center;
  }
  #webcrumbs .font-title {
    font-family:
      Lato,
      ui-sans-serif,
      system-ui,
      sans-serif,
      Apple Color Emoji,
      Segoe UI Emoji,
      Segoe UI Symbol,
      Noto Color Emoji;
  }
  #webcrumbs .text-3xl {
    font-size: 48.75px;
    line-height: 58.5px;
  }
  #webcrumbs .text-4xl {
    font-size: 58.5px;
    line-height: 67.27499999999999px;
  }
  #webcrumbs .text-sm {
    font-size: 22.75px;
    line-height: 34.125px;
  }
  #webcrumbs .font-bold {
    font-weight: 700;
  }
  #webcrumbs .font-semibold {
    font-weight: 600;
  }
  #webcrumbs .text-primary {
    --tw-text-opacity: 1;
    color: rgb(97 27 248 / var(--tw-text-opacity));
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
  #webcrumbs {
    font-family: Open Sans !important;
    font-size: 26px !important;
  }
  
</style>