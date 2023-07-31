<script setup>
import { RouterView } from 'vue-router'
import Nav from '@shared/components/Nav.vue'
</script>

<template>
  <Nav></Nav>
  <div class="container">
    <div class="row">
      <main>
        <div class="section">
          <RouterView />
        </div>
      </main>
    </div>
  </div>
</template>
