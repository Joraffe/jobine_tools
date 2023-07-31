<script setup>
import LandingItem from '@shared/components/LandingItem.vue'
import BlurbJobine from '@home/components/blurbs/BlurbJobine.vue'
import ImageJobine from '@home/components/images/ImageJobine.vue'
</script>

<template>
  <main>
    <div class="section">
      <LandingItem>
        <template #image>
          <ImageJobine></ImageJobine>
        </template>
        <template #blurb>
          <BlurbJobine></BlurbJobine>
        </template>
      </LandingItem>
    </div>
  </main>
</template>
