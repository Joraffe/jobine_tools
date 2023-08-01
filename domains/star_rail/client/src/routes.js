const routes = [
  {
    path: '/star-rail',
    name: 'star-rail',
    component: () => import('@starRail/views/IndexView.vue'),
  },
  {
    path: '/star-rail/character',
    name: 'star-rail-character',
    component: () => import('@starRail/views/characters/CharacterIndexView.vue'),
  },
];


export default routes;
