<template>
    <div class="navbar">
        <h2>Cat or Dog Classifier</h2>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Navbar extends Vue {}
</script>

<style scoped>
h2 {
    color: white;
}
.navbar {
  background-color: #333;
  position: fixed;
  height: 80px;
  top: 0;
  left: 0;
  width: 100%;
}
</style>

