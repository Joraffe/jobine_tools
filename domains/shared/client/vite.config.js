import { fileURLToPath, URL } from 'node:url'
import { rm } from 'node:fs/promises'
import { resolve } from 'path';

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    {
      name: "Cleaning assets folder",
      async buildStart() {
        await rm(resolve(__dirname, '../static/public/dist'), { recursive: true, force: true});
      }
    }
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  build: {
    outDir: '../static',
    assetsDir: 'public/dist',
    manifest: true,
    rollupOptions: {
      input: {
        'home': './src/main.js'
      }
    }
  }
})
