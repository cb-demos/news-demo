export const userList = [
  {
    username: 'betauser',
    password: 'betauser',
    beta_access: true
  },
  {
    username: 'normaluser',
    password: 'normaluser',
    beta_access: false
  }
]

export const betaAccess = () => {
  if (localStorage.getItem('user') === null) {
    return false
  } else {
    let localUser = {}
    userList.map((user) => {
      if (user.username === localStorage.getItem('user')) {
        localUser = user
      }
    })
    return localUser.beta_access
  }
}

export const isLoggedIn = () => {
  return localStorage.getItem('user') !== null
}
