export default {
  items: [
    {
      name: 'Dashboard',
      url: '/dashboard',
      icon: 'icon-speedometer',
    },
    {
      title: true,
      name: 'Facilities',
      wrapper: {            // optional wrapper object
        element: '',        // required valid HTML5 element tag
        attributes: {}        // optional valid JS object with JS API naming ex: { className: "my-class", style: { fontFamily: "Verdana" }, id: "my-id"}
      },
      class: ''             // optional class names space delimited list for title item ex: "text-center"
    },
    {
      name: 'All Facilities',
      url: '/theme/colors',
      icon: 'icon-globe',
    },
    {
      title: true,
      name: 'Administration',
      wrapper: {
        element: '',
        attributes: {},
      },
    },
    {
      name: 'Admin Manager',
      url: '/base/breadcrumbs',
      icon: 'icon-puzzle',
    },
  ],
};
