<template>
    <div class="toolbar" role="banner">
        <span id="welcome">{{ msg }}</span>
        <div class="spacer"></div>
        <vk-button size="small" class="menu-button" type="primary">500</vk-button>
        <vk-button size="small" class="menu-button" type="primary">400</vk-button>
        <vk-button size="small" class="menu-button" type="primary" @click="doSomething">doSomething</vk-button>
        <vk-button size="small" class="menu-button" type="primary" @click="$refs.childModal.showModal()">Login</vk-button>
        <router-link to="/createaccount">
          <vk-button size="small" class="menu-button" type="primary">Create Account</vk-button>
        </router-link>
        <login-modal ref="childModal"></login-modal>
        <div class="icon-div">
          <vk-menu id="menu-icon"></vk-menu>
          <img id="menu-icon2" src="../assets/icons8-menu.svg"/>
        </div>
    </div>

</template>

<script>
import '@vuikit/theme';
import { Button, ButtonLink} from '../../node_modules/vuikit/lib/button';
import { Icon, IconButton } from '../../node_modules/vuikit/lib/icon';
import { IconMenu } from '@vuikit/icons'
import LoginModal from './LoginModal.vue';
export default {
  name: 'TopToolbar',
  components: {
      LoginModal,
      VkButton: Button,
      VkButtonLink: ButtonLink,
      VkMenu: IconMenu,
      VkIcon: Icon,
      VkIconButton: IconButton
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

.icon-div{
  display: none;
}

.menu-button{
  margin-right: 2%;
}

#welcome{
  margin-left: 3%;
  font-size: 18px;
}

@media only screen and (max-width: 650px){
  .menu-button{
    display: none;
  }

  .icon-div{
    display: block;
  }

  #menu-icon{
    width: 20%;
    height: 30%;
  }
  #menu-icon2{
    width: 5vw;
    height: 5vh;
    padding: 2px;
  }

}
</style>
