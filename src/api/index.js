export const apiUrl = 'http://localhost:8000/api/'
import session from './session'
import localforage from 'localforage'
import Vue from 'vue'

export default {
  logIn (credentials) { return session.post(apiUrl + `auth/login/`, credentials) },
  getHomeJsonData (params) {
    return new Promise(async function(resolve, reject) {
      Vue.prototype.$insProgress.start()
      var response = await session.get(apiUrl + `home_json/`, { params })
      resolve(response.data)
      Vue.prototype.$insProgress.finish()
    });
  },
  getHeroList (params) {
    return session.get(apiUrl + `hero/`, { params });
  },
  async getHeroDetail (slug) {
    var heroes = await localforage.getItem('hero.heroes')
    var hero = heroes[slug]
    if (hero) {
      return hero
    } else {
      var res = await session.get(apiUrl + `hero/${slug}/`);
      heroes[slug] = res.data
      localforage.setItem('hero.heroes', heroes)
      return res.data
    }
  },
  getEquipmentList (params) {
    return session.get(apiUrl + `equipment/`, { params });
  },
  buyHero (equipment_id) {
    return session.get(apiUrl + `buy-hero/`, { hero_id: hero_id });
  },
  buyEquipment (equipment_id) {
    return session.get(apiUrl + `buy-equipment/`, { equipment_id: equipment_id });
  },
}
