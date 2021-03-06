<?php

/*
	controllers/admin.php

	Copyright 2011 Jake Moreman <me@jakemoreman.co.uk>

	This program is free software; you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation; either version 2 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program; if not, write to the Free Software
	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
	MA 02110-1301, USA.
*/

if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class Admin extends CI_Controller {

	public function index()
	{	
		if($this->session->userdata('logged_in'))
			redirect('admin/status', 'redirect', 302);
		else
			redirect('user/login', 'redirect', 302);
	}
	
	public function status()
	{	
		$this->load->library('status');
		
		$data['title'] = 'Admin';
		$data['app'] = 'HotNAS';
		$data['slogan'] = 'A lightweight NAS Linux distribution';
		
		$data['hostname'] = file_get_contents('/etc/hostname');
		$data['version'] = file_get_contents('/etc/br-version');
		$data['build_date'] = 'TODO';
		
		$this->load->view('header', $data);
		$this->load->view('admin/status', $data);
		$this->load->view('footer', $data);
		
	}
	
	public function diagnostics($subsection)
	{
		switch($subsection)
		{
			case 'logs':
				$this->load->library('files');
				
				$data['title'] = 'Diagnostic - Logs';
				$data['app'] = 'HotNAS';
				$data['slogan'] = 'A lightweight NAS Linux distribution';
				
				if($this->input->post('filename'))
				{
					$data['filecontents'] = file_get_contents($this->input->post('filename'));
					$data['filename'] = $this->input->post('filename');
				}
				else
				{
					$data['filecontents'] = file_get_contents('/var/log/messages');
					$data['filename'] = 'messages';
				}
				
				$this->load->view('header', $data);
				$this->load->view('admin/diagnostics/logs', $data);
				$this->load->view('footer', $data);
				break;
			default:
				$data['title'] = 'Unknown page';
				$data['app'] = 'HotNAS';
				$data['slogan'] = 'A lightweight NAS Linux distribution';
				
				$this->load->view('header', $data);
				$this->load->view('footer', $data);
		}
	}
}
?>
