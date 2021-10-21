<template>
  <div id="app">
    <!--img src="./assets/logo.png"-->
    <router-view/>
  </div>
</template>

<script>
import AOS from '../node_modules/aos/dist/aos.js';
import { datadogRum } from '@datadog/browser-rum';
export default {
  name: 'App',
  beforeCreate() {
    AOS.init();
  },
  created(){
    datadogRum.init({
          applicationId: '5c19ff1f-62dc-467c-8294-f1d54c6583fc',
          clientToken: 'pub953963662d5f76b93bb0370a71113128',
          site: 'datadoghq.com',
          service:'vue-app',
          // Specify a version number to identify the deployed version of your application in Datadog 
          version: '1.0.0',
          sampleRate: 100,
          trackInteractions: true,
          allowedTracingOrigins:["http://localhost:8000"]
        });
  }
}
</script>

<style>
@import '../node_modules/aos/dist/aos.css';
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
