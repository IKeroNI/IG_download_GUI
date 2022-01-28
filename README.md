# Instagram Downloader
Simple downloader for pictures from instagram based on instaloader module. Python 3.9.2

You don't need to specify paths for session files, or folder for photos.

##### If it's your first time use, it's necessary to check "firts time use" chechbox.

To select from whose accounts you want to download, open List1 and List 2 (for private accounts, your account need to have permission to see them),
or List 3 (for non-private accounts).
To setup your accounts to for login, press Open Accounts or Private Accounts button. Private Accounts are used for List1 and List2 accounts.
Note that only 1 name account for line is required, starting from 4th one.

There are 3 different options to download:
regular - For list1, download all stories, photos and videos, even if there is already that file in download directory.
          For List2 include stories and videos, but don't overwrite same posts.
          For List3, download photos, but stop download after reaching first exact post on disk (starting from newest ones).
          ![GUI_look](https://i.imgur.com/YE8fi7y.png)
          
        
        
        
by date: [Download from interval needs to be checked] - download all photos from a given period.   
         ![GUI_look](https://i.imgur.com/36Yhysr.png)
         
         
         
by percentage: [Turn on long download needs to be checked] - downloading 0-100% of photos on accounts, sorted by likes of the post, descending.
               Recommended for 50+ photo per account download, to avoid instagram to stop account from downloading.
![GUI_look](https://i.imgur.com/5O3CTuT.png)
                
