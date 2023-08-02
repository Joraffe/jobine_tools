<script setup>
import { ref, onMounted } from 'vue'

const characters = ref([]);

onMounted(async () => {
  const response = await fetch('/star-rail/character/api/all')
  characters.value = await response.json()
})
</script>

<template>
  <div class="container">
    <div class="section">
      <div class="row">
        <div class="col s12">
          <h3>Characters!</h3>
          <ul>
            <li v-for="character in characters">{{ character.name }}</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
