                /*-----QWidget------------------------------------------------------------------------------------------------------------------------------------*/ 
                QWidget
                {
                    background-color: rgb(192, 192, 192);
                    color: rgb(216,216,216);
                    selection-color: rgb(254,254,254);
                    selection-background-color: rgb(86,128,194);
                    font-family: DejaVuSans;
                    font-size: 12px;
                }
                                 
                /*-----QTableView------------------------------------------------------------------------------------------------------------------------------------*/ 
                QTableView, QTreeView
                {
                background-color: rgb(59,59,59);
                }   

                /*-----QComboBox------------------------------------------------------------------------------------------------------------------------------------*/                          
                QComboBox 
                {
                    color: rgb(216,216,216);
                    background-color: rgb(59,59,59);
                    border-radius: 0.2em;
                    padding-left: 6px;           
                    min-width: 7em;
                }
                
                QComboBox:on
                {
                    background-color: rgb(67,97,143);
                }
                                 
                QComboBox:disabled 
                {
                    background-color: #323232;
                    color: #8a8a8a;
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
                    background-color: rgb(82,82,82);
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
                    color: rgb(37,37,37);
                }
                                 
                QMenuBar::item:selected 
                {
                    color: rgb(225,225,225);
                    background-color: rgb(94,132,191);
                    border-style: outset;
                    border-radius: 0.2em; 
                }
                          
                /*-----QTabBar------------------------------------------------------------------------------------------------------------------------------------*/                
                QTabBar::tab 
                {
	                border-width: 1px;
	                border-bottom: none;
	                padding: 5px;
	                padding-left: 10px;
	                padding-right: 10px;
                    border-top-left-radius: 0.3em;
                    border-top-right-radius: 0.3em;
                    border-bottom-style: solid; 
                }   
                                   
                QTabBar::tab:selected 
                {
                    color: rgb(40,40,40);
                    background-color: rgb(179,179,179);
                    border-style: solid;
                    border-width: 1px;
                    border-color: #373737;
                    border-bottom-color: #424242;            
                }

                QTabBar::tab:!selected 
                {
                    color: rgb(33,33,33);
                    background-color: rgb(139,139,139);            
                }

                QTabBar::tab:hover:!selected 
                {
                    color: rgb(33,33,33);
                    background-color: rgb(146,146,146);
                }
                                 
                QTabBar::tab:last
                {
                    border-top-right-radius: 0.3em;
	                margin-right: 0; 
                }
                
                /*-----QTabWidget------------------------------------------------------------------------------------------------------------------------------------*/                                     
                QTabWidget::pane 
                {
                    top: 1px;
                    background-color: rgb(179,179,179);
                }
                                 
                /*-----QTextEdit------------------------------------------------------------------------------------------------------------------------------------*/ 
                QTextEdit 
                {
                    color: rgb(149, 214, 000);
                    background-color: rgb(29,29,29);
                }
                
                QTextEdit:!editable 
                {
                    background-color: rgb(29,29,29);
                }

                /*-----QScrollBar------------------------------------------------------------------------------------------------------------------------------------*/             
                QScrollBar
                {
                    margin: 0px;
                    padding: 0px;   
                }
                
                QScrollBar:vertical 
                {
                    border: 1px solid #3D3A3A;
                    background-color: none;
                    width: 13px;
                }
                                 
                QScrollBar:horizontal 
                {
                    border: 1px solid #3D3A3A;
                    background-color: none;
                    height: 13px;
                }
                                 
                QScrollBar::handle:vertical {
                    background-color: #545454;
                    border-radius: 4px;

                }
                QScrollBar::handle:horizontal {
                    background-color: #545454;
                    border-radius: 4px;
                }

                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background-color: rgb(146,146,146);
                }

                QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                    background-color: rgb(146,146,146);
                }

                /*-----QSlider------------------------------------------------------------------------------------------------------------------------------------*/                
                QSlider 
                {
                    background-color: rgb(84,84,84);        
                }
                                 
                QSlider::handle 
                {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #fff, stop:1 #ddd);
                    border: 1px solid #444;
                }
                            
                QSlider::sub-page:horizontal 
                {
                    background: rgb(71,114,179);
                }
                                 
                QSlider::handle:horizontal:hover
                {
                    background: rgb(71,114,179);
                    border-radius: 0px;
                }
                                 
                QSlider::add-page:horizontal:disabled 
                {
                    background: rgb(40,40,40);
                    border-color: #999;
                }
                                 
                QSlider::handle:horizontal:disabled 
                {
                    background: #eee;
                    border: 1px solid #aaa;
                    border-radius: 4px;
                }
                
                /*-----QCheckBox------------------------------------------------------------------------------------------------------------------------------------*/ 
                QCheckBox
                {
	                color: rgb(37,37,37);
                }

                QCheckBox::indicator 
                {
                    width: 12px;
                    height: 12px;
                }
                           
                QCheckBox::indicator:checked
                {
                    image: url('E:/Maya/Scripts/Images/checkmark-16.ico');
                    background-color: rgb(71,114,179);
                    border-radius: 0.2em;  
                }  

                QCheckBox::indicator:unchecked 
                {
                    background-color: rgb(84,84,84);
                    border-radius: 0.2em;  
                }
                                 
                /*-----QRadioButton------------------------------------------------------------------------------------------------------------------------------------*/ 
                QRadioButton
                {
	                color: rgb(37,37,37);
                }   

                /*-----QLineEdit------------------------------------------------------------------------------------------------------------------------------------*/                 
                QLineEdit
                {
                    color: rgb(195,195,195);
                    background-color: rgb(59,59,59);
                    border: 1px solid #404040;
                    border-color: rgb(61,61,61);
                    border-radius: 0.3em;
                    padding: 0px;
                }

                /*-----QLabel------------------------------------------------------------------------------------------------------------------------------------*/                
                QLabel 
                {
                    color: rgb(37,37,37);
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

                /*-----QMessageBox------------------------------------------------------------------------------------------------------------------------------------*/ 
                QMessageBox 
                {
                    color: rgb(179,179,179);
                    background-color: rgb(192, 192, 192);
                } 

                /*-----QPushButton------------------------------------------------------------------------------------------------------------------------------------*/   
                QPushButton 
                {
                    color: rgb(37,37,37);
                    background-color: rgb(192, 192, 192);
                }