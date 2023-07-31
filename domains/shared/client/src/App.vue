<script setup>
import { RouterView } from 'vue-router'
import Nav from '@shared/components/Nav.vue'
</script>

<template>
  <Nav></Nav>
  <div class="container">
    <div class="row">
    <RouterView />
    </div>
  </div>
</template>
