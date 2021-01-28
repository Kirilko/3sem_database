new Vue({
    el: '#orders_app',
    data:{
        search:'',
        data:{},
        indications:[],
        groups:[],
        contraindications:[],
        dd:[],
        ddi:[],
        ddc:[],
        country:[],
        manufacturer:[],
        type:[],
        drug:[],
        specialization:[],
        drugstore:[],
        dds:[],
    },
    created: function (){
        const vm = this
        axios.get('/api/group/').then(function (response){
            vm.groups = response.data
        })
        axios.get('/api/indication/').then(function (response){
            vm.indications = response.data
        })
        axios.get('/api/contraindication/').then(function (response){
            vm.contraindications = response.data
        })
        axios.get('/api/dd/').then(function (response){
            vm.dd = response.data
        })
        axios.get('/api/ddi/').then(function (response){
            vm.ddi = response.data
        })
        axios.get('/api/ddc/').then(function (response){
            vm.ddc = response.data
        })
        axios.get('/api/country/').then(function (response){
            vm.country = response.data
        })
        axios.get('/api/manufacturer/').then(function (response){
            vm.manufacturer = response.data
        })
        axios.get('/api/type/').then(function (response){
            vm.type = response.data
        })
        axios.get('/api/drug/').then(function (response){
            vm.drug = response.data
        })
        axios.get('/api/specialization/').then(function (response){
            vm.specialization = response.data
        })
        axios.get('/api/drugstore/').then(function (response){
            vm.drugstore = response.data
        })
        axios.get('/api/dds/').then(function (response){
            vm.dds = response.data
        })

    },
    methods:{
        change1(data){
            const vm = this
                vm.data={}
                    for(let i in data[0]){
                        vm.data[i]=data[0][i]
                        for(let j in data[1]){
                            if(data[0][i].specialization==data[1][j].id)
                            {
                                vm.data[i].specialization = data[1][j].name
                            }
                        }
                    }
        },
        change2(data){
            const vm=this
            vm.data={}
                    for(let i in data[0]){
                        vm.data[i]=data[0][i]
                        for(let j in data[1]){
                            if(data[0][i].group==data[1][j].id)
                            {
                                vm.data[i].group = data[1][j].name
                            }
                        }
                    }
        },
        change3(data){
            const vm=this
            vm.data={}
                    for(let i in data[0]){
                        vm.data[i]=data[0][i]
                        for(let j in data[1]){
                            if(data[0][i].country==data[1][j].id)
                            {
                                vm.data[i].country = data[1][j].name
                            }
                        }
                    }
        },
        tmp(id,data){
            const vm=this
            vm.data={}
            for(let i in data[3]){
                if(data[3][i].drug_store==id){
                    for(let j in data[0]){
                        if(data[0][j].id==data[3][i].drug){
                            vm.data[i]= {name:'',type:'',price:'',manufacturer:'',shelf_life:''}
                            vm.data[i].name = data[0][j].drug_description
                            vm.data[i].type = data[0][j].type
                            vm.data[i].manufacturer = data[0][j].manufacturer
                            vm.data[i].shelf_life = data[0][j].shelf_life
                            vm.data[i].price = data[3][i].price
                            for(let k in data[1]){
                                if(data[1][k].id==vm.data[i].name){
                                    vm.data[i].name=data[1][k].name
                                }
                            }
                            for(let k in data[4]){
                                if(data[4][k].id==vm.data[i].type){
                                    vm.data[i].type=data[4][k].name
                                }
                            }
                            for(let k in data[5]){
                                if(data[5][k].id==vm.data[i].manufacturer){
                                    vm.data[i].manufacturer=data[5][k].name
                                }
                            }
                        }
                    }
                }
            }
        },
        find(){
            let tmp={}
            let it=0
            for(let i in this.data){

                    if(this.search in this.data[i]){

                        tmp[it]=this.data[i]
                        it++
                    }
                }
            }

    },
    watch:{
        search(){
            this.find()
        }
    }
})