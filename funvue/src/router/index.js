import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AnotherPage from '@/components/AnotherPage'
import CreateAccount from '@/components/CreateAccount'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/nextpage',
      name: 'AnotherPage',
      component: AnotherPage
    },
    {
      path: '/createaccount',
      name: 'CreateAccount',
      component: CreateAccount
    }
  ]
})
