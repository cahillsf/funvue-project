<template>
    <div class="toolbar" role="banner">
        <span id="welcome">{{ msg }}</span>
        <div class="spacer"></div>
        <vk-button size="small" class="menu-button" type="primary">500</vk-button>
        <vk-button size="small" class="menu-button" type="primary">400</vk-button>
        <vk-button size="small" class="menu-button" type="primary" @click="doSomething">doSomething</vk-button>
        <vk-button size="small" class="menu-button" type="primary" @click="$refs.childModal.showModal()">Login</vk-button>
        <login-modal ref="childModal"></login-modal>
    </div>

</template>

<script>
import '@vuikit/theme';
import { Button, ButtonLink} from '../../node_modules/vuikit/lib/button';
import LoginModal from './LoginModal.vue'
export default {
  name: 'TopToolbar',
  components: {
      LoginModal,
      VkButton: Button,
      VkButtonLink: ButtonLink
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',

    }
  },
  methods: {
    doSomething() {
      this.msg= 'TopToolbar!;'
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.spacer {
  flex: 1;
}

.toolbar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-around;
  background-image: linear-gradient(#1a46a5, #289128);
  color: white;
  font-weight: 600;
}

.menu-button{
  margin-right: 2%;
}

#welcome{
  margin-left: 3%;
  font-size: 18px;
}

</style>
