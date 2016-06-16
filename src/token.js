export function getToken () {
  return window.localStorage.getItem('token')
}

export function setToken (token) {
  return window.localStorage.setItem('token', token)
}

export function removeToken () {
  return window.localStorage.removeItem('token')
}
