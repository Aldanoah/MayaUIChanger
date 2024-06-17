
                /*-----QWidget------------------------------------------------------------------------------------------------------------------------------------*/ 
                QWidget
                {
                    background-color: rgb(30,30,50);
                    color: rgb(94,246,255);
                    selection-color: rgb(94,246,255); 
                    selection-background-color: rgb(247,80,70);
                    font-family: rajdhani;
                    font-weight: bold;
                    font-size: 13px;
                }
                          
                /*-----QTableView------------------------------------------------------------------------------------------------------------------------------------*/ 
                QTableView, QTreeView
                {
                background-color: rgb(48,48,48);
                }   
                                 
                /*-----QComboBox------------------------------------------------------------------------------------------------------------------------------------*/
                QComboBox {
                    color: rgb(29, 237, 131);
                    background-color: rgb(0,0,0);
                    border-radius: 0.2em;
                    padding-left: 6px;           
                    min-width: 7em;
                }
                                 
                QComboBox:on
                {
                    color: rgb(94,246,255);
                    background-color: rgb(123,39,39);
                }
                
                QComboBox:disabled 
                {
                    background-color: rgb(14,11,18);
                    color: rgb(123,39,39);
                }
                                 
                QComboBox:hover,QPushButton:hover 
                {
                    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0W, y2: 1, stop: 0 #f75049, stop: 1 #f75049);
                }
                                   
                QComboBox::down-arrow
                {
                    image: url('E:/Maya/Scripts/Images/Arrow-204-16.ico');
                    width: 8px;
                    height: 8px;
                }
                
                QComboBox::drop-down
                {
                    width: 15px;
                    border-radius: 0.2em;
                    border-left-width: 0px;    
                }
                
                /*-----QMenu------------------------------------------------------------------------------------------------------------------------------------*/            
                QMenu
                {
                    background-color: transparent;
                }
                                 
                QMenu::item
                {
                    background-color: transparent;
                }
                
                QMenu::separator
                {
                    height:0px;
                    margin-left:5px;
                    margin-right:5px;
                }

                QMenuBar
                {
                    background-color: transparent;
                    spacing:2px;
                    border: 1px;
                }
                                 
                QMenuBar::item 
                {
	                background-color: transparent;
                }
                                 
                QMenuBar::item:selected 
                {
                    color: rgb(94,246,255);
                    background-color: rgb(123,39,39);
                    border-style: outset;
                    border-radius: 0.2em; 
                }
                                 
                /*-----QTabBar------------------------------------------------------------------------------------------------------------------------------------*/                       
                QTabBar::tab
                {
	                border-width: 1px;
	                padding: 5px;
	                padding-left: 10px;
	                padding-right: 10px;
                    border-top-left-radius: 0.3em;
                    border-top-right-radius: 0.3em;
                    border-bottom-style: solid; 
                }  
                
                QTabBar::tab:selected {
                    border-style: solid;
                    color: rgb(94,246,255);
                    background-color: rgb(14,11,18);   
                }
                
                QTabBar::tab:!selected 
                {
                    color: rgb(29,237,131);
                    background-color: rgb(14,11,18);          
                } 

                QTabBar::tab:hover:!selected 
                {
                    color: rgb(94,246,255);
                    background-color: rgb(123,39,39);
                }  

                QTabBar::tab:last
                {
                    border-top-right-radius: 0em;
	                margin-right: 0; 
                }   

                /*-----QTabWidget------------------------------------------------------------------------------------------------------------------------------------*/
                QTabWidget::pane 
                {
                    background-color: rgb(14,11,18);
                } 
                
                /*-----QTextEdit------------------------------------------------------------------------------------------------------------------------------------*/
                QTextEdit 
                {
                    color: rgb(255,255,255);
                    background-color: rgb(14,11,18);
                }
                                 
                QTextEdit:!editable 
                {
                    background-color: rgb(14,11,18);
                }

                /*-----QScrollBar-----------------------------------------------------------------------------------------------------------------------------------*/               
                QScrollBar 
                {
                    color: rgb(255,255,255); 
                    background-color: rgb(247,80,73);        
                }
                
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical 
                {
                    background-color: rgb(14,11,18);      
                }
                
                QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal 
                {
                    background-color: rgb(14,11,18); 
                }
                                 
                /*-----QSlider-----------------------------------------------------------------------------------------------------------------------------------*/
                QSlider 
                {
                    background-color: rgb(247,80,73);        
                }
                                 
                QSlider::handle 
                {
                    background-color: rgb(94,246,255);        
                }
                
                QSlider::add-page:horizontal:disabled 
                {
                    background-color: rgb(123,39,39);
                }
                
                QSlider::sub-page:horizontal:disabled 
                {
                    background-color: rgb(247,80,73); 
                }
                                 
                /*-----QCheckBox------------------------------------------------------------------------------------------------------------------------------------*/                
                QCheckBox
                {
	                background-color: transparent;
                }
                                 
                QCheckBox::indicator 
                {
                    width: 12px;
                    height: 12px;
                }

                QCheckBox::indicator:checked
                {
                    image: url('E:/Maya/Scripts/Images/checkmark-16.ico');
                    background-color: rgb(247,80,70);
                    border-radius: 0.2em;  
                } 
                                             
                QCheckBox::indicator:unchecked 
                {
                    background-color: rgb(14,11,18);
                    border-radius: 0.2em;  
                }   
                    
                /*-----QLineEdit------------------------------------------------------------------------------------------------------------------------------------*/
                QLineEdit
                {
                    color: rgb(29, 237, 131);
                    background-color: rgb(14,11,18);
                    border-color: rgb(61,61,61);
                    border-radius: 0.3em;
                    padding: 0px;
                }
                                 
                /*-----QLabel------------------------------------------------------------------------------------------------------------------------------------*/                
                QLabel 
                {
                    color: rgb(94,246,255);
                    background-color: transparent;
                }
                
                /*-----QProgressBar------------------------------------------------------------------------------------------------------------------------------------*/ 
                QProgressBar 
                {
                    background-color: #424242;
                    border: 1px solid #373737;
                    padding: 0px;
                    text-align: right;
                }
                                 
                QProgressBar::chunk {
                    background-color: #5680c2;
                    border: 1px solid #373737;
                }
                                 
            """)

            # cycle the background color to black
            cycle_background_color_to_black()
