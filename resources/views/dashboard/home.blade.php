@extends('layouts.app')

@section('title', 'Dashboard')

@section('left_nav')
    @include('partials.left_nav')
@endsection

<!-- Right Panel -->
@section('right_nav')
<div id="right-panel" class="right-panel">
    @include('partials.header')
</div>
@endsection
