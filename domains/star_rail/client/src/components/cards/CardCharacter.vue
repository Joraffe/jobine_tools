<script setup>
import Card from '@shared/components/Card.vue';

const props = defineProps({links: Array})

props.links = [
  { name: 'All Characters', route: '/star-rail/character' },
]
</script>

<template>
  <Card :links="links">
    <template #image>
      <img src="@starRail/assets/images/star_rail_characters.png" />
    </template>
    <template #content>
      Search for information on Star Rail Characters!
    </template>
  </Card>
</template>
