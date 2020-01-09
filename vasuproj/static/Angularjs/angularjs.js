var myApp = angular.module("myApp", ["ngRoute","ngSanitize"]);

myApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
  });


myApp.controller("myController",function($scope,$http){
  $scope.ddsel="one";	
  $scope.applyFilter=function(colnm){
	  $scope.EnoEnameHttp();
	  $scope.selcol=colnm;
  }
  
   
  $scope.EnoEnameHttp=function(){
	  $http.get('/enoename').then(function(response){
		  
		  $scope.cs90data=response.data;
		  $scope.nm="Success";
	  });
  }
  
  $scope.DMbasedHttp=function(){
	  $scope.unkm='http://127.0.0.1:8000/cs90a/'
	  $http.post($scope.unkm,$scope.ddsel).then(function(response){
		  $scope.cs90data=response.data;
	  });
  }
  
  

  $scope.DMbasedHttp=function(){
	  var dt={
			  "dnm":$scope.ddsel
	  };
	  dn=angular.toJson(dt);
	  dn1=JSON.stringify(dt);
	  $scope.unkm='http://127.0.0.1:8000/cs90a/';
	  $http({
		  method: "POST",
		  url   : $scope.unkm,
		  data  :dn,
		  headers: {'Content-Type': 'application/json'}
	   }).then(function(response){
		       alert('Back === back');
		       $scope.cs90data=response.data;
		       $window.location.href = '/cs90Staff.html';  
	       });
  }
  
  $scope.ddSelect=function(item){
	  $scope.ddsel=item;
	  $scope.DMbasedHttp();
  }
  
  $scope.DmnamesHttp=function(){
	  $http.get('/dmretrieve').then(function(response){
		  $scope.DMdata=response.data;
	  });
	  $http.get('/budgetarea').then(function(response){
		  $scope.appdata=response.data;
	  });
   }

  $scope.appHttp=function(){
	  $http.get('/budgetarea').then(function(response){
			  $scope.appdata=response.data;
		  });
   }


  
  $scope.APbaseHttp=function(x){
	  var dt = $.param({
          ap:x
      });
	  $http.post('http://127.0.0.1:8000/budareaemp/',dt).then(function(response){
		  alert("Back from Plasm ***")
		  $scope.employees=response.data;
		  console.log($scope.employees)
	  });
   }
  
  $scope.apSelect=function(item){
	  alert("In ApSelllect :::",item)
	  $scope.ddsel=item;
	  $event.preventDefault();
	  $scope.APbaseHttp(item);
  }

  
 
     
});


