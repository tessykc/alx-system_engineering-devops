# installs the package flask using puppet
package { 'flask':
  ensure          => installed, version:'2.1.0',
  provider        => 'pip3',
  install_options => [
    { '--index-url' => 'https://pypi.mycorp.com'
    }]

 
}
