import axios from 'axios';
import Cookies from 'js-cookie'
const CSRF_COOKIE_NAME = 'csrftoken';
const CSRF_HEADER_NAME = 'X-CSRFToken';
import { setupCache } from 'axios-cache-adapter'
const cache = setupCache({
  maxAge: 15 * 60 * 1000
})

const session = axios.create({
  xsrfCookieName: CSRF_COOKIE_NAME,
  xsrfHeaderName: CSRF_HEADER_NAME,
  adapter: cache.adapter
});
var token = Cookies.get('token')
if (token) {
  session.defaults.headers.Authorization = `JWT ${token}`
}

export default session;
