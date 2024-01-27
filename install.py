import os
import time

print("\033[96m" + """
 **       **                                     ********  *******  **********         ******  **      **     **     **********
/**      /**                                    **//////**/**////**/////**///         **////**/**     /**    ****   /////**/// 
/**   *  /**  ******  ****** **********        **      // /**   /**    /**           **    // /**     /**   **//**      /**    
/**  *** /** **////**//**//*//**//**//** *****/**         /*******     /**          /**       /**********  **  //**     /**    
/** **/**/**/**   /** /** /  /** /** /**///// /**    *****/**////      /**          /**       /**//////** **********    /**    
/**** //****/**   /** /**    /** /** /**      //**  ////**/**          /**          //**    **/**     /**/**//////**    /**    
/**/   ///**//****** /***    *** /** /**       //******** /**          /**           //****** /**     /**/**     /**    /**    
//       //  //////  ///    ///  //  //         ////////  //           //             //////  //      // //      //     //     
                            
                       Author : SukaLebok06
               Worm-GPT By Jawa Barat Error Network
\033[0m""")


masuk = input('\033[38mMasukin token lu tod:\033[35m ')

if masuk:
    print('\033[36mSukses memasukan token, sedang menginstall jq')
    time.sleep(2.5)
    os.system('clear')
    os.system(f'export CHATGPT_TOKEN={masuk}')
    os.system('apt install jq')
else:
    print('\033[31mError: Token tidak valid. Silakan masukkan token yang benar.')

exit_choice = input('\033[37mYakin ingin keluar? (yes/no): \033[37m')

if exit_choice.lower() == 'yes':
    print('\033[31mSedang keluar mohon tunggu')
else:
    print('\033[32mTerima kasih! Tetap semangat!\033[0m')
