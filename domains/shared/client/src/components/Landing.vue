<script setup>
import LandingItem from './LandingItem.vue'
import BlurbJobine from './blurbs/BlurbJobine.vue'
import ImageJobine from './images/ImageJobine.vue'
</script>

<template>
  <LandingItem>
    <template #image>
      <ImageJobine></ImageJobine>
    </template>
    <template #blurb>
      <BlurbJobine></BlurbJobine>
    </template>
  </LandingItem>
</template>
