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
      '@shared': fileURLToPath(new URL('./src', import.meta.url)),
      // When adding new domains (and to keep their source code co-located in said domain),
      // Add an alias here so it's easier to import to the "shared" build process,
      // since the "shared" domain is what is building the static/public/dist files
      '@home': fileURLToPath(new URL('../../home/client/src', import.meta.url))
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
