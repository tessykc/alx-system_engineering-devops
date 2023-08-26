# installs the package flask using puppet
package { 'flask':
  ensure          => version:'2.1.0',
  provider        => 'pip3',
  

 
}
