# Ubuntu 20.04

These are for Intel CPU and Nvidia GPU.

1. Update base software
    
    ```
    sudo apt update && sudo apt -y upgrade && sudo apt -y autoremove
    ```

2. Add `files/Home/aptsources-cleanup.pyz` (handles duplicate entries in apt)

    ```
    cp files/Home/aptsources-cleanup.pyz ~/aptsources-cleanup.pyz
    chmod a+x ~/aptsources-cleanup.pyz
    sudo ~/aptsources-cleanup.pyz
    ```

3. Remove unnecessary installed apps from *Ubuntu Software*.

4. Remove *snap*.

    ```
    # List installed snap packages
    snap list 

    # On my current install the following order is used to remove all packages
    sudo snap remove canonical-livepatch
    sudo snap remove gtk-common-themes
    sudo snap remove gnome-3-34-1804
    sudo snap remove snap-store
    sudo snap remove core18
    sudo umount /snap/core/10577
    sudo snap remove core
    sudo snap remove snapd
    sudo apt purge -y snapd
    rm -rf ~/snap
    sudo rm -rf /snap /var/snap /var/lib/snapd
    ```

5. Disable *Tracker* (it indexes all the things on the system, so if you install a dataset will a lot of files it will index each of those and consume a lot of space, may even bug to consume all space)

    ```
    systemctl --user mask tracker-store.service tracker-miner-fs.service tracker-miner-rss.service tracker-extract.service tracker-miner-apps.service tracker-writeback.service
    tracker reset --hard
    sudo reboot

    # Use the output of these commands to check if tracker is disabled
    tracker status
    tracker daemon
    ```

6. Copy `files/Pictures` to `~/Pictures` and set `exoplanet.tif` as wallpaper.

    ```
    cp files/Pictures/* ~/Pictures/*
    ```
    
7. Goto *Software & Updates* and make following changes
    
    - Ubuntu Software
        - Download from main server
    - Updates
        - For other packages, subscribe to (Security updates only)
        - Automatically check for updates (Never)
        - When there are other updates (Display every two weeks)
        - Notify me of a new Ubuntu version (Never)
        
8. Customize *Settings*
    - Bluetooth (off)
    - Appearance
        - Window colors (Dark)
        - Auto-hide the Dock (True)
        - Icon size (38)
    - Notifications
        - Lock screen notifications (off)
    - Search (off)
    - Privacy
        - Connectivity (off)
        - Location Services (off)
        - File History & Trash
            - File History (off) 
            - Automatically Delete Temporary Files (on)
            - Automatically Delete Period (7 days)
        - Screen Lock
            - Black Screen Delay (Never)
            - Automatic Screen Lock (off)
            - Lock screen on suspend (off)
        - Diagnostics (Never)
        - Power
            - Dim screen when inactive (off)
            - Blank Screen (Never)
            - Automatic suspend (off)
        - Mouse & Touchpad
            - Mouse Speed (middle)
            - Natural scrolling (off)
            - Touchpad natural scrolling (on)
            - Touchpad speed (~60%)
            - Edge scrolling (off)
        
9. Install useful things
    
    ```
    sudo apt install gnome-tweaks tree ubuntu-restricted-extras vlc terminator htop git curl tmux
    ```
    
10. Change settings in *Tweaks*
    - General
        - Animations (off)
    - Appearance
        - Applications (Adwaita-dark)
        - Cursor (DMZ-White)
        - Icons (Yaru)
        - Sound (Yaru)
    - Extensions
        - Desktop icons (on) in settings turn off personal folder and trash icon
    - Fonts
        - Interface Text (Ubuntu Mono Regular 12)
    - Keyboard & Mouse
        - Pointer Location (on)
        - Middle Click Paster (off)
        - Touchpad Disable while Typing (on)
        - Addional Layout Options -> Caps Lock behavior -> Swap ESC and Caps Lock
    - Top Bar
        - Battery Percentage (on)
        - Weekday (on)
        - Date (on)
        - Seconds (off)
        
11. `ibus-setup` then under Emoji tab disable that shortcut.

12. Setup Vscode

    - Download from this [link](https://code.visualstudio.com/docs/?dv=linux64_deb)
    - `sudo dpkg -i code*.deb && sudo apt install -f` to install vscode
    - Extensions
        - Bracket Pair Colorizer `ext install CoenraadS.bracket-pair-colorizer-2`
        - Code Spell Checker
        - Github Markdown Preview
        - Gruvbox Theme (Gruvbox Dark Hard)
        - Markdown PDF
        - Python
        - Python Docstring Generator
        - vscode-icons
        - YAML
    - Settings
        - Editor: Font Size (14)
        - Editor: Font Family (add 'PowerlineSymbols')
        - Files: Exclude (\*\*/\_\_pycache\_\_, \*\*/.ipynb\_checkpoints, \*\*/.vscode, \*\*/\*\*.pyc)
        - Code Lens (off)
        - Editor: Accept Suggestion on Enter (off)
        - Minimap (off)
    - Select `flake8` as linter

13. Latex

    ```
    sudo apt install texlive-full
    
    # klatexformula (to convert equations to images)
    sudo apt install klatexformula
    
    # texmaker
    # Link to download: https://www.xm1math.net/texmaker/download.html
    sudo dkg -i texmaker*.deb
    sudo apt install -f
    ```

14. PDFSamBasic install [link](https://pdfsam.org/download-pdfsam-basic/)
    
    ```
    sudo dpkg -i pdfsam*.deb
    sudo apt install -f
    ```

15. Google chrome install

    ```
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - 
    sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
    sudo apt update
    sudo apt install google-chrome-stable
    ```

 16. Setup terminator
    - Profiles (General)
        - Use the system fixed width font (off)
        - Font (Ubuntu Mono Regular 13)
        - Allow bold text (on)
        - Show titlebar (off)
    - Profiles (Colors)
        - Built-in schemes (Gruvbox dark)
    - Profiles (Background)
        - Transparent background
        - 0.86 transparency
    - Profiles (Scrolling)
        - Scrollback (7000)
    - Right click (show scrollbar off)

17. Nvidia setup

    - Driver setup

        ```
        sudo add-apt-repository ppa:graphics-drivers/ppa
        sudo apt install nvidia-driver-455
        ```

18. General ubuntu setup
    - Organize dock icons as (Files, Chrome, VsCode, Shutter, Discord, Nvidia X Server, PDFSam, klatexformula)

    - Install Shutter (screenshot app)

        ```
        sudo add-apt-repository ppa:linuxuprising/shutter
        sudo apt install shutter
        ```

    - Gimp

        ```
        sudo add-apt-repository ppa:ubuntuhandbook1/gimp
        sudo apt install gimp gimp-gmic
        ```

    - Discord

        ```
        # Download .deb from https://discord.com/
        sudo dpkg -i discord*.deb
        sudo apt install -f
        ```

    - Create folders
        - Desktop/Temp
        - Desktop/Data
        - Desktop/Computer
        - Desktop/Github
        - Desktop/Github/working
        - Desktop/Github/install_packages

    - Add folders to sidebar
        - Desktop/Github/blog
        - Desktop/Github/deep_learning
        - Desktop/Data
        - Desktop/Github
        - Desktop/Temp

19. Github setup

    ```
    ssh-keygen -t rsa -b 4096 -C "kushajreal@gmail.com"
    ssh-add ~/.ssh/id_rsa
    cat ~/.ssh/id_rsa.pub

    # Paste the key in Settings -> SSH and GPG keys -> New SSH key
    ```

20. Jekyll setup

    ```
    sudo apt-get install ruby-full build-essential zlib1g-dev
    gem install jekyll bundler
    ```

20. ohmyzsh setup

    - Install zsh and ohmyzsh

        ```
        sudo apt install zsh
        chsh -s $(which zsh)
        sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
        sudo apt install fonts-powerline
        ```

    - Configure `.zshrc`.

        ```
        export PATH=$HOME/bin:/usr/local/bin:$PATH
        HYPHEN_INSENSITIVE="true"
        DISABLE_UPDATE_PROMPT="true"
        COMPLETION_WAITING_DOTS="true"
        DISABLE_UNTRACKED_FILES_DIRTY="true"
        export LANG=en_US.UTF-8

        # Change to nvim
        if [[ -n $SSH_CONNECTION ]]; then
            export EDITOR='nvim'
        else
            export EDITOR='nvim'
        fi

        export ARCHFLAGS="-arch x86_64"
        ```

    - Powerlevel10k setup

        * Download these 4 files and then double-click to install the fonts 
            - [MesloLGS NF Regular.ttf](
                https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf)
            - [MesloLGS NF Bold.ttf](
                https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf)
            - [MesloLGS NF Italic.ttf](
                https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf)
            - [MesloLGS NF Bold Italic.ttf](
                https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf)

        * In Vscode, Goto Settings and add `MesloLGS NF` font family.
        * In terminator, select `MesloLGS NF Regular` font.
        * `git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k`
        * Set `ZSH_THEME="powerlevel10k/powerlevel10k"` in `~/.zshrc`.
        * Follow the instructions to configure. To configure manually edit `~/.p10k.zsh` or run `p10k configure`
        * To update powerlevel10k use this command, `git -C ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k pull` (Restart zsh, do not use `source ~/.zshrc`)
        * To show only `prev_dir/current_dir` in prompt make the following changes in `~/.p10k.zsh`

            ```
            typeset -g POWERLEVEL9K_SHORTEN_STRATEGY=1
            typeset -g POWERLEVEL9K_SHORTEN_DIR_LENGTH=2
            ```
    - .zshrc and .bashrc add
        
        ```
        alias update_ubuntu='sudo apt update && sudo apt upgrade && sudo apt autoremove'
        alias update_conda='conda update --all'

        alias hub='cd ~/Desktop/Github'
        alias temp='cd ~/Desktop/Temp'
        alias blog='cd ~/Desktop/Github/blog'
        alias dl='cd ~/Desktop/Github/deep_learning'
        alias note='jupyter notebook'

        alias vim='nvim'
        alias nvimdiff='nvim -d'
        alias vimdiff='nvim -d'

        export GEM_HOME="$HOME/gems"
        export PATH="$HOME/gems/bin:$PATH"

        alias nvim='~/AppImages/nvim.appimage'
        ```
21. Neovim setup
    
    * Download latest appimage from https://github.com/neovim/neovim/releases. Place in ~/AppImages.
    
        ```
        chmod u+x ~/AppImages/nvim.appimage
        mkdir ~/.config/nvim
        cd ~/.config/nvim
        touch init.vim

        # Download vim-plug
        curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
        pip install pynvim
        npm install -g neovim
        ```

    * Install coc plugins

        ```
        :CocInstall: coc-html coc-css coc-json coc-markdownlint coc-pyright coc-sh coc-yaml
        ```

    * CocConfig. Type `:CocConfig` and copy below stuff

        ```
        {
            "python.linting.enabled":true,
            "python.linting.flake8Enabled":true
        }
        ```
    * Run `:PlugInstall`
    * Useful things
        * :PlugUpdate :- Update all the plugins
        * :PlugUpgrade :- Upgrade vim-plug
        * :PlugInstall :- To install plugins


22. `.gitconfig`

    ```
    [user]
        email = kushajreal@gmail.com
        name = KushajveerSingh
    [diff]
        tool = default-difftool
    [difftool "default-difftool"]
        cmd = code --wait --diff $LOCAL $REMOTE
    [color]
        ui = auto
    [alias]
        log = log --all --graph --decorate --date=relative
    ```

23. Conda setup

    * Download miniconda from https://docs.conda.io/en/latest/miniconda.html

        ```
        bash Miniconda*.sh
        conda update --all
        ```

    * Use `shell.bash` in .bashrc and `shell.zsh` in .zshrc for conda config
    * Add condarc

        ```
        echo "channel_priority: false" > ~/.condarc
        ```
    * Install random packages

        ```
        conda install -c conda-forge nodejs
        pip install pynvim autopep8 flake8
        ```
    * Install packages

        ```
        # Base libraries
        pip install numpy matplotlib pandas scikit-learn

        # PyTorch https://pytorch.org/
        conda install pytorch torchvision cudatoolkit=11.0 -c pytorch
        pip install tensorboard

        # Documentation packages
        npm install -g katex
        pip install sphinx sphinxcontrib.katex

        # pytorch geometric
        pip install torch-scatter -f https://pytorch-geometric.com/whl/torch-1.7.0+cu110.html
        pip install torch-sparse -f https://pytorch-geometric.com/whl/torch-1.7.0+cu110.html
        pip install torch-cluster -f https://pytorch-geometric.com/whl/torch-1.7.0+cu110.html
        pip install torch-spline-conv -f https://pytorch-geometric.com/whl/torch-1.7.0+cu110.html
        pip install torch-geometric
        ```

24. tmux

    * Default shortcuts

        ```
        # Panes
        (C-b) + " -> Horizontal pane
        (C-b) + % -> Vertical pane
        (C-b) + z -> Zoom into a pane (repeat for reverse)
        
        # Windows
        (C-b) + c -> New window
        (C-b) + 2 -> Move to second window
        (C-b) + & -> Kill a window
        (C-b) + , -> Rename a window

        # Sessions
        (C-b) + d -> Detach from a session
        tmux ls -> Get a list of running tmux s  essions
        tmux attach -t 1 -> Connect to session 1 (that we got from above)
        (C-b) + $ -> Rename session name
        tmux new -s 'session_name' -> Create a new session
        ```

    * Config file in `~/.tmux.conf`

        ```
        # Use Ctrl-a as prefix
        set-option -g prefix C-a
        unbind-key C-a
        bind-key C-a send-prefix

        # Set base index of windows to 1
        set -g base-index 1

        # Automatically set window title
        set-window-option -g automatic-rename on
        set-option -g set-titles on

        # Enable color in terminal
        set -g default-terminal screen-256color

        # Enable mouse mode
        setw -g mouse on
        setw -g monitor-activity on

        # Easy config reload
        bind-key r source-file ~/.tmux.conf \; display-message "~/.tmux.conf reloaded"

        # No delay for escape key press
        set -sg escape-time 0

        # Use shift+arrows to switch windows
        bind -n S-Left previous-window
        bind -n S-Right next-window

        # Use terminator shortcuts for new panes
        bind-key e split-window -h
        bind-key o split-window -v

        # THEME
        set -g status-bg black
        set -g status-fg white
        set -g window-status-current-bg white
        set -g window-status-current-fg black
        set -g window-status-current-attr bold
        set -g status-interval 60
        set -g status-left-length 30
        set -g status-left '#[fg=green](#S) #(whoami)'
        set -g status-right '#[fg=yellow]#(cut -d " " -f 1-3 /proc/loadavg)#[default] #[fg=white]%H:%M#[default]'
        ```