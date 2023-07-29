import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";


const getFirebaseConfig = () => {
  return {
    apiKey: "AIzaSyBVo4_iuBGp_5zgd-dAVa2trUHkjaU08OU",
    authDomain: "jobine-tools.firebaseapp.com",
    projectId: "jobine-tools",
    storageBucket: "jobine-tools.appspot.com",
    messagingSenderId: "1085980448363",
    appId: "1:1085980448363:web:381080a0a541b4ea25032e",
    measurementId: "G-RMC11HMRLR"
  }
};

const getFirebase = () => {
  const config = getFirebaseConfig();

  const app = initializeApp(config);
  const analytics = getAnalytics(app);
  const auth = getAuth(app);

  return {
    app: app,
    analytics: analytics,
    auth: auth,
  };
}


export default getFirebase;
