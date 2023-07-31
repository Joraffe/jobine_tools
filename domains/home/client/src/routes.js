const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@home/views/HomeView.vue'),
  },
];


export default routes;
