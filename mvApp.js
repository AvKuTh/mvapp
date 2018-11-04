Vue.component('friend', {
  props: ['frdata'],
  template: `
<div> 
<li> {{ frdata.name }}</li>
</div>
`
})

Vue.component('fd', {
  props: ['frdet'],
    template:
    `
<div>
 <p> {{frdet.name }}</p>
 <p> {{frdet.email }}</p>
 <p> {{frdet.location }}</p>
</div>
`
})

fListapp = new Vue({
  el: '#fList',
  data: {
    friends: []
  },
    created: function () {
        var vm = this
      axios
          .get('http://www.json-generator.com/api/json/get/cfdlYqzrfS')
            .then(function (response) {
                console.log(response.data[0])
                vm.friends =  response.data
          })
  },
    methods: {
        showDetail: function (frdata) {
            detailApp.set(friend,frdata)
        }}
})


detailApp = new Vue({
    el: '#details',
    data: {
        friend: null
    }, 
    created: function () {
        var vm = this
        axios
          .get('http://www.json-generator.com/api/json/get/cfdlYqzrfS')
          .then(function (response) {
              vm.friend =  response.data[1]
          })
  },
   
    
})

