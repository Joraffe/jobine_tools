<script setup>
import LandingItem from '@shared/components/LandingItem.vue'
import BlurbStarRail from '@starRail/components/blurbs/BlurbStarRail.vue'
import ImagesstarRail from '@starRail/components/images/ImageStarRail.vue'
</script>

<template>
  <LandingItem>
    <template #image>
      <ImagesstarRail></ImagesstarRail>
    </template>
    <template #blurb>
      <BlurbStarRail></BlurbStarRail>
    </template>
  </LandingItem>
</template>
