<template>
  <div id="app">
    <CatDogClassifier msg="Welcome to Your Vue.js + TypeScript App"/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import CatDogClassifier from './components/CatDogClassifier.vue';
import Navbar from './components/Navbar';

@Component({
  components: {
    CatDogClassifier,
    Navbar,
  },
})
export default class App extends Vue {}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: url('./assets/3732944.jpg');
  height: 100vh;
  background-size: 1100px;
  background-repeat: no-repeat;
  background-position-x: 120%;
  background-position-y: 50%;
}
</style>
