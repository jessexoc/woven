#!/usr/bin/env python

from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management.color import no_style

from fabric import state 
from fabric.main import _merge
from fabric.network import normalize

from woven.main import setup_environ

class WovenCommand(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--noinput', action='store_false', dest='interactive', default=True,
            help='Do NOT prompt for input (except password entry if required)'),
        make_option('-r', '--reject-unknown-hosts',
            action='store_true',
            default=False,
            help="reject unknown hosts"
        ),
    
        make_option('-D', '--disable-known-hosts',
            action='store_true',
            default=False,
            help="do not load user known_hosts file"
        ),
        make_option('-u', '--user',
            default=state._get_system_username(),
            help="username to use when connecting to remote hosts"
        ),
    
        make_option('-p', '--password',
            default=None,
            help="password for use with authentication and/or sudo"
        ),
    
        make_option('-H', '--hosts',
            default=[],
            help="comma-separated list of hosts to operate on"
        ),
    
        make_option('-R', '--roles',
            default=[],
            help="comma-separated list of roles to operate on"
        ),
        
    )
    help = ""
    requires_model_validation = False
    name = __name__.split('.')[-1]
  
    def handle_host(self, *args, **options):
        """
        This will be executed per host - override in subclass
        """
    
    def handle(self, *args, **options):
        """
        Initializes the fabric environment
        """
        self.style = no_style()
        #manage.py execution specific variables
        #verbosity 0 = No output at all, 1 = woven output only, 2 = Fabric outputlevel = everything except debug
        state.env.verbosity = int(options.get('verbosity', 1))
        #show_traceback = options.get('traceback', False)
        state.env.INTERACTIVE = options.get('interactive')
        
        #Fabric options
        #Django passes in a dictionary instead of the optparse options objects
        for option in options:
            state.env[option] = options[option]

        #This next section is taken pretty much verbatim from fabric.main
        #so we follow an almost identical but more limited execution strategy
        
        # Handle --hosts, --roles (comma separated string => list)
        for key in ['hosts', 'roles']:
            if key in state.env and isinstance(state.env[key], str):
                state.env[key] = state.env[key].split(',')
        
        #We now need to load django project woven settings into env
        #This is the equivalent to module level execution of the fabfile.py.
        #If we were using a fabfile.py then we would include setup_environ()
        setup_environ(settings)
        
        #Back to the standard execution strategy
        # Set current command name (used for some error messages)
        state.env.command = self.name
        # Set host list (also copy to env)
        state.env.all_hosts = hosts = _merge(state.env.hosts,state.env.roles)
        # If hosts found, execute the function on each host in turn
        for host in hosts:
            # Preserve user
            prev_user = state.env.user
            
            # Split host string and apply to env dict
            #TODO - This section is replaced by network.interpret_host_string in Fabric 1.0
            username, hostname, port = normalize(host)
            state.env.host_string = host
            state.env.host = hostname
            state.env.user = username
            state.env.port = port
            #print 'normalized',username, hostname, port
            # Log to stdout
            if state.env.verbosity:
                print("[%s] Executing task '%s'" % (host, self.name))
            # Actually run command
            #commands[name](*args, **kwargs)
            # Put old user back
            state.env.user = prev_user




  


