<template>
  <div class="col s6">
    <slot name="image"></slot>
  </div>
  <div class="col s6">
    <div class="blurb-wrapper valign-wrapper">
      <slot name="blurb"></slot>
    </div>
  </div>
</template>

<style scoped>
.blurb-wrapper {
  height: 500px;
}
</style>
