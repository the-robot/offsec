# System-wide .bashrc file for interactive bash(1) shells.

# To enable the settings / commands in this file for login shells as well,
# this file has to be sourced in /etc/profile.

# If not running interactively, don&#39;t do anything
[ -z &#34;$PS1&#34; ] &amp;&amp; return

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z &#34;${debian_chroot:-}&#34; ] &amp;&amp; [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, overwrite the one in /etc/profile)
# but only if not SUDOing and have SUDO_PS1 set; then assume smart user.
if ! [ -n &#34;${SUDO_USER}&#34; -a -n &#34;${SUDO_PS1}&#34; ]; then
  PS1=&#39;${debian_chroot:+($debian_chroot)}\u@\h:\w\$ &#39;
fi

# Commented out, don&#39;t overwrite xterm -T &#34;title&#34; -n &#34;icontitle&#34; by default.
# If this is an xterm set the title to user@host:dir
#case &#34;$TERM&#34; in
#xterm*|rxvt*)
#    PROMPT_COMMAND=&#39;echo -ne &#34;\033]0;${USER}@${HOSTNAME}: ${PWD}\007&#34;&#39;
#    ;;
#*)
#    ;;
#esac

# enable bash completion in interactive shells
#if ! shopt -oq posix; then
#  if [ -f /usr/share/bash-completion/bash_completion ]; then
#    . /usr/share/bash-completion/bash_completion
#  elif [ -f /etc/bash_completion ]; then
#    . /etc/bash_completion
#  fi
#fi

# sudo hint
if [ ! -e &#34;$HOME/.sudo_as_admin_successful&#34; ] &amp;&amp; [ ! -e &#34;$HOME/.hushlogin&#34; ] ; then
    case &#34; $(groups) &#34; in *\ admin\ *|*\ sudo\ *)
    if [ -x /usr/bin/sudo ]; then
	cat &lt;&lt;-EOF
	To run a command as administrator (user &#34;root&#34;), use &#34;sudo &lt;command&gt;&#34;.
	See &#34;man sudo_root&#34; for details.
	
	EOF
    fi
    esac
fi

# if the command-not-found package is installed, use it
if [ -x /usr/lib/command-not-found -o -x /usr/share/command-not-found/command-not-found ]; then
	function command_not_found_handle {
	        # check because c-n-f could&#39;ve been removed in the meantime
                if [ -x /usr/lib/command-not-found ]; then
		   /usr/lib/command-not-found -- &#34;$1&#34;
                   return $?
                elif [ -x /usr/share/command-not-found/command-not-found ]; then
		   /usr/share/command-not-found/command-not-found -- &#34;$1&#34;
                   return $?
		else
		   printf &#34;%s: command not found\n&#34; &#34;$1&#34; &gt;&amp;2
		   return 127
		fi
	}
fi
