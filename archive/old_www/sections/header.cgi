#!/usr/bin/haserl
<%
	# sections/header.cgi
	#
	# Copyright 2011 Jake Moreman <me@jakemoreman.co.uk>
	#
	# This program is free software; you can redistribute it and/or modify
	# it under the terms of the GNU General Public License as published by
	# the Free Software Foundation; either version 2 of the License, or
	# (at your option) any later version.
	#
	# This program is distributed in the hope that it will be useful,
	# but WITHOUT ANY WARRANTY; without even the implied warranty of
	# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	# GNU General Public License for more details.
	#
	# You should have received a copy of the GNU General Public License
	# along with this program; if not, write to the Free Software
	# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
	# MA 02110-1301, USA.
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
		"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<title><%= $ptitle %> | <%= $sitename %></title>
		<meta http-equiv="content-type" content="text/html;charset=utf-8" />
		<link rel="stylesheet" type="text/css" href="css/reset.css" />
		<link rel="stylesheet" type="text/css" href="css/framework.css" />
		<link rel="stylesheet" type="text/css" href="css/style.css" />
		<script type="text/javascript" src="js/jquery.js"></script>
		<script type="text/javascript">
		$(document).ready(function () {
			$('div#menu li').hover(
				function () {
				//show its submenu
				$('ul', this).show();

				},
				function () {
				//hide its submenu
				$('ul', this).hide();
				}
			);
		});
		</script>
	</head>

	<body class="main">
		<div id="container" class="container_12">
			<div id="header" class="grid_12">
				<h1><%= $sitename %></h1>
				<h2><%= $sitedescription %></h2>
			</div>
			
			<div id="menu" class="grid_12">
				<ul id="nav">
					<li><a href="#">Home/Status</a></li>
					<li><a href="#">Storage</a>
						<ul>
							<li><a href="#">Drives</a></li>
							<li><a href="#">Shares</a></li>
						</ul>
					</li>
					<li><a href="#">Services</a>
						<ul>
							<li><a href="#">Samba</a></li>
							<li><a href="#">NFS</a></li>
							<li><a href="#">FTP</a></li>
							<li><a href="#">HTTP</a></li>
							<li><a href="#">DNS/DHCP</a></li>
						</ul>
					</li>
					<li><a href="#">Extras</a>
						<ul>
							<li><a href="#">Downloads</a></li>
						</ul>
					</li>
					<li><a href="#">Diagnostics</a>
						<ul>
							<li><a href="#">Logs</a></li>
							<li><a href="#">Process list</a></li>
							<li><a href="#">Hardware Information</a></li>
						</ul>
					</li>
				</ul>
			</div>
			
			<div id="content" class="grid_12">
