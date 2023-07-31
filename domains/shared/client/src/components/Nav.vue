<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <!-- This is following the materialize.css navbar template -->
  <nav>
    <div class="nav-wrapper teal lighten-1">
      <a href="#" class="brand-logo">Logo</a>
      <ul id="nav-mobile" class="right hide-on-med-and-down">
        <li><RouterLink to="/star_rail">Star Rail</RouterLink></li>
        <li><RouterLink to="/">Home</RouterLink></li>
      </ul>
    </div>
  </nav>
</template>
