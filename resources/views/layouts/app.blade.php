<!doctype html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang=""> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8" lang=""> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9" lang=""> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang=""> <!--<![endif]-->
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Pharmacy Recommendation Engine - @yield('title')</title>
    <meta name="description" content="Sufee Admin - HTML5 Admin Template">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="apple-touch-icon" href="apple-icon.png">
    <link rel="shortcut icon" href="favicon.ico">

    <link rel="stylesheet" href="{{ URL::asset('admin-dashboard/assets/css/normalize.css') }}">
    <link rel="stylesheet" href="{{ URL::asset('admin-dashboard/assets/css/bootstrap.min.css') }}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css">
    <link rel="stylesheet" href="{{ URL::asset('admin-dashboard/assets/css/themify-icons.css') }}">
    <link rel="stylesheet" href="{{ URL::asset('admin-dashboard/assets/css/flag-icon.min.css') }}">
    <link rel="stylesheet" href="{{ URL::asset('admin-dashboard/assets/css/cs-skin-elastic.css') }}">
    <!-- <link rel="stylesheet" href="assets/css/bootstrap-select.less"> -->
    <link rel="stylesheet" href="{{ URL::asset('admin-dashboard/assets/scss/style.css') }}">
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,600,700,800' rel='stylesheet' type='text/css'>
    <!-- <script type="text/javascript" src="https://cdn.jsdelivr.net/html5shiv/3.7.3/html5shiv.min.js"></script> -->
</head>
<body>
@section('left_nav')
    This is the left navigation. Override in inherited template.
@show

<div id="right-panel" class="right-panel">
    @yield('content')
</div>

<script src="{{ URL::asset('admin-dashboard/assets/js/vendor/jquery-2.1.4.min.js') }}"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js"></script>
<script src="{{ URL::asset('admin-dashboard/assets/js/main.js') }}"></script>
<script src="{{ URL::asset('admin-dashboard/assets/js/plugins.js') }}"></script>
</body>
</html>
