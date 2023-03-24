

/*
 * ----------------------------------------------------------------------
 *                          Components & Functions                      |
 * ----------------------------------------------------------------------
 */
import React, { useState } from 'react'

import {DefaultPlayer as Video} from 'react-html5video'
import 'react-html5video/dist/styles.css'  
/*
* ----------------------------------------------------------------------
*                              Services & Models                       |
* ----------------------------------------------------------------------
*/



/*
 * ----------------------------------------------------------------------
 *                                Styles                                |
 * ----------------------------------------------------------------------
 */
import './VideoSpace.scss'

/*
 * ----------------------------------------------------------------------
 *                                Images                                |
 * ----------------------------------------------------------------------
 */

function VideoSpace(props) {

  /* --------------------------------------------------------------------
   *                           Constants                                |
   * --------------------------------------------------------------------
   */
  const [model,setModel]=useState(false)
  const {videoUri}=props
  /* --------------------------------------------------------------------
   *                               Props                                |
   * --------------------------------------------------------------------
   */

  /*--------------------------------------------------------------------
  *                                 Data                               |
  * --------------------------------------------------------------------
  */


  /* --------------------------------------------------------------------
   *                             Hooks & States                         |
   * --------------------------------------------------------------------
   */

  /* --------------------------------------------------------------------
   *                             Functions                              |
   * --------------------------------------------------------------------
   */

    
  
  /* --------------------------------------------------------------------
   *                            Effect Hooks                            |
   * --------------------------------------------------------------------
   */

  /* --------------------------------------------------------------------
   *                                 JSX                                |
   * --------------------------------------------------------------------
   */
  return (
    <div className='VideoSpaceContainer'>   
      <div className='video' >
        <div className='video-container'>
        <Video 
          style={{width:'100%'}}
          autoPlay={model}
          controls={['PlayPause','Seek','Time','Volume','Fullscreen']}
        >
          <source src={videoUri} type="video/mp4"/>
        </Video>  
        </div>
      </div>
    </div>
  )
}

export default VideoSpace