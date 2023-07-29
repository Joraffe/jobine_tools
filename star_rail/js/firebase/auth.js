import { onAuthStateChanged } from "@firebase/auth";

import getFirebase from "./init";


const handleAuthStateChangeSuccess = (user) => {
  // User is signed in, so display the "sign out" button and login info.
  document.getElementById('sign-out').hidden = false;
  document.getElementById('login-info').hidden = false;
  user.getIdToken().then(function (token) {
    // Add the token to the browser's cookies. The server will then be
    // able to verify the token against the API.
    // SECURITY NOTE: As cookies can easily be modified, only put the
    // token (which is verified server-side) in a cookie; do not add other
    // user information.
    document.cookie = "token=" + token;
  });
};


const handleAuthStateChangeError = (error) => {
  console.log(error)
  alert('Unable to log in: ' + error);
}



const addAuthHandlers = () => {
  const firebase = getFirebase();

  // Signing out by clicking "Sign Out"
  document.getElementById('sign-out').onclick = () => {
    firebase.auth.signOut();
  };

  // Handling Auth State Change
  onAuthStateChanged(
    firebase.auth,
    handleAuthStateChangeSuccess,
    handleAuthStateChangeError
  );
};


export default {
  addAuthHandlers: addAuthHandlers,
};
