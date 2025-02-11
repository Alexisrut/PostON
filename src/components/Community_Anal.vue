<template>
    <div className="flex-1 p-4 grid grid-cols-2 gap-4">
        <div className="bg-white rounded-md shadow-md p-4 col-span-1">
            <div className="space-y-4">
                <div className="flex flex-col">
                    <label className="text-sm font-medium mb-1">Personal Information</label>
                    <textarea
                        className="w-full h-[100px] border border-neutral-200 rounded-lg p-3 resize-none focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all"
                        placeholder="Enter your personal information..."
                    />
                </div>
                <div className="flex flex-col">
                    <label className="text-sm font-medium mb-1">Professional Experience</label>
                    <textarea
                        className="w-full h-[100px] border border-neutral-200 rounded-lg p-3 resize-none focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all"
                        placeholder="Enter your professional experience..."
                    />
                </div>
                <div className="flex flex-col">
                    <label className="text-sm font-medium mb-1">Additional Comments</label>
                    <textarea
                        className="w-full h-[100px] border border-neutral-200 rounded-lg p-3 resize-none focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all"
                        placeholder="Enter any additional comments..."
                    />
                </div>
                <button className="w-full py-3 bg-primary-500 text-white rounded-lg font-semibold hover:bg-primary-600 transform hover:scale-[1.02] transition-all duration-200 shadow-lg hover:shadow-xl">
                    Submit Analysis
                </button>
            </div>
        </div>
        <div className="bg-white rounded-md shadow-md p-4 col-span-1">
            <div className="flex justify-between items-center mb-4">
                <h2 className="font-bold text-lg">Analysis Results</h2>
                <span className="material-symbols-outlined cursor-pointer hover:text-primary-500 transition-colors">
                    refresh
                </span>
            </div>
            <div className="h-[400px] overflow-y-auto border border-neutral-200 rounded-lg p-4">
                <div className="space-y-4">
                    <div className="p-3 bg-neutral-50 rounded-lg hover:bg-neutral-100 transition-all">
                        <h3 className="font-semibold">Key Insights</h3>
                        <p className="text-sm text-neutral-600 mt-1">Analysis results will appear here</p>
                    </div>
                    <div className="p-3 bg-neutral-50 rounded-lg hover:bg-neutral-100 transition-all">
                        <h3 className="font-semibold">Statistics</h3>
                        <p className="text-sm text-neutral-600 mt-1">Statistical data will be shown here</p>
                    </div>
                    <div className="p-3 bg-neutral-50 rounded-lg hover:bg-neutral-100 transition-all">
                        <h3 className="font-semibold">Recommendations</h3>
                        <p className="text-sm text-neutral-600 mt-1">Recommendations based on analysis</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    @import url(https://fonts.googleapis.com/css2?family=Lato&display=swap);

    @import url(https://fonts.googleapis.com/css2?family=Open+Sans&display=swap);

    @import url(https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200);

    /*! tailwindcss v3.4.11 | MIT License | https://tailwindcss.com*/
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
    #webcrumbs .col-span-1 {
    grid-column: span 1 / span 1;
    }
    #webcrumbs .mb-4 {
    margin-bottom: 12px;
    }
    #webcrumbs .mt-1 {
    margin-top: 3px;
    }
    #webcrumbs .mt-4 {
    margin-top: 12px;
    }
    #webcrumbs .flex {
    display: flex;
    }
    #webcrumbs .grid {
    display: grid;
    }
    #webcrumbs .hidden {
    display: none;
    }
    #webcrumbs .h-\[200px\] {
    height: 200px;
    }
    #webcrumbs .h-\[400px\] {
    height: 400px;
    }
    #webcrumbs .h-\[40px\] {
    height: 40px;
    }
    #webcrumbs .w-\[1200px\] {
    width: 1200px;
    }
    #webcrumbs .w-\[40px\] {
    width: 40px;
    }
    #webcrumbs .w-\[60px\] {
    width: 60px;
    }
    #webcrumbs .w-full {
    width: 100%;
    }
    #webcrumbs .flex-1 {
    flex: 1 1 0%;
    }
    #webcrumbs .transform {
    transform: translate(var(--tw-translate-x), var(--tw-translate-y))
        rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y))
        scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
    }
    #webcrumbs .cursor-pointer {
    cursor: pointer;
    }
    #webcrumbs .resize-none {
    resize: none;
    }
    #webcrumbs .grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
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
    #webcrumbs .gap-2 {
    gap: 6px;
    }
    #webcrumbs .gap-4 {
    gap: 12px;
    }
    #webcrumbs :is(.space-y-4 > :not([hidden]) ~ :not([hidden])) {
    --tw-space-y-reverse: 0;
    margin-bottom: calc(12px * var(--tw-space-y-reverse));
    margin-top: calc(12px * (1 - var(--tw-space-y-reverse)));
    }
    #webcrumbs .overflow-y-auto {
    overflow-y: auto;
    }
    #webcrumbs .rounded-full {
    border-radius: 9999px;
    }
    #webcrumbs .rounded-lg {
    border-radius: 24px;
    }
    #webcrumbs .rounded-md {
    border-radius: 18px;
    }
    #webcrumbs .border {
    border-width: 1px;
    }
    #webcrumbs .border-2 {
    border-width: 2px;
    }
    #webcrumbs .border-dashed {
    border-style: dashed;
    }
    #webcrumbs .border-neutral-200 {
    --tw-border-opacity: 1;
    border-color: rgb(224 224 224 / var(--tw-border-opacity));
    }
    #webcrumbs .border-neutral-300 {
    --tw-border-opacity: 1;
    border-color: rgb(202 202 202 / var(--tw-border-opacity));
    }
    #webcrumbs .bg-neutral-100 {
    --tw-bg-opacity: 1;
    background-color: rgb(238 238 238 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-neutral-50 {
    --tw-bg-opacity: 1;
    background-color: rgb(247 247 247 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-neutral-900 {
    --tw-bg-opacity: 1;
    background-color: rgb(70 70 70 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-primary-500 {
    --tw-bg-opacity: 1;
    background-color: rgb(115 65 255 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-red-500 {
    --tw-bg-opacity: 1;
    background-color: rgb(239 68 68 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-white {
    --tw-bg-opacity: 1;
    background-color: rgb(255 255 255 / var(--tw-bg-opacity));
    }
    #webcrumbs .object-contain {
    object-fit: contain;
    }
    #webcrumbs .p-3 {
    padding: 9px;
    }
    #webcrumbs .p-4 {
    padding: 12px;
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
    #webcrumbs .py-4 {
    padding-bottom: 12px;
    padding-top: 12px;
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
    #webcrumbs .text-lg {
    font-size: 29.25px;
    line-height: 43.875px;
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
    #webcrumbs .font-semibold {
    font-weight: 600;
    }
    #webcrumbs .text-neutral-400 {
    --tw-text-opacity: 1;
    color: rgb(177 177 177 / var(--tw-text-opacity));
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
    }
    #webcrumbs .shadow-lg,
    #webcrumbs .shadow-md {
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000),
        var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
    }
    #webcrumbs .shadow-md {
    --tw-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
        0 2px 4px -2px rgba(0, 0, 0, 0.1);
    --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color),
        0 2px 4px -2px var(--tw-shadow-color);
    }
    #webcrumbs .transition-all {
    transition-duration: 0.15s;
    transition-property: all;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    }
    #webcrumbs .transition-colors {
    transition-duration: 0.15s;
    transition-property: color, background-color, border-color,
        text-decoration-color, fill, stroke;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    }
    #webcrumbs .duration-200 {
    transition-duration: 0.2s;
    }
    #webcrumbs {
    font-family: Open Sans !important;
    font-size: 26px !important;
    }
    #webcrumbs :is(.bg-neutral-50) {
    color: rgba(0, 0, 0, 0.9) !important;
    }
    #webcrumbs :is(.bg-neutral-100) {
    color: rgba(0, 0, 0, 0.9) !important;
    }
    #webcrumbs :is(.bg-neutral-900) {
    color: hsla(0, 0%, 100%, 0.9) !important;
    }
    #webcrumbs :is(.bg-primary-500) {
    color: hsla(0, 0%, 100%, 0.9) !important;
    }
    #webcrumbs .hover\:scale-\[1\.02\]:hover {
    --tw-scale-x: 1.02;
    --tw-scale-y: 1.02;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y))
        rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y))
        scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
    }
    #webcrumbs .hover\:border-primary-500:hover {
    --tw-border-opacity: 1;
    border-color: rgb(115 65 255 / var(--tw-border-opacity));
    }
    #webcrumbs .hover\:bg-neutral-100:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(238 238 238 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:bg-primary-600:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(99 27 255 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:text-primary-500:hover {
    --tw-text-opacity: 1;
    color: rgb(115 65 255 / var(--tw-text-opacity));
    }
    #webcrumbs .hover\:shadow-xl:hover {
    --tw-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1),
        0 8px 10px -6px rgba(0, 0, 0, 0.1);
    --tw-shadow-colored: 0 20px 25px -5px var(--tw-shadow-color),
        0 8px 10px -6px var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000),
        var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
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
    #webcrumbs .focus\:ring-primary-500:focus {
    --tw-ring-opacity: 1;
    --tw-ring-color: rgb(115 65 255 / var(--tw-ring-opacity));
    }
</style>