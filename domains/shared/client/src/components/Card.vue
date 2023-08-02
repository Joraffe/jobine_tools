<script setup>
import { RouterLink } from 'vue-router'

const props = defineProps({links: Array})
</script>

<template>
  <div class="row">
    <div class="col s6">
      <div class="card">
        <div class="card-image">
          <slot name="image"></slot>
        </div>
        <div class="card-content">
          <slot name="content"></slot>
        </div>
        <div class="card-action">
          <template v-for="link in links">
            <RouterLink :to="link.route">{{ link.name }}</RouterLink>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>
