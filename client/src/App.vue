<template>
  <div id="app">
    <Navbar/>
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
  margin-top: 80px;
}
</style>
