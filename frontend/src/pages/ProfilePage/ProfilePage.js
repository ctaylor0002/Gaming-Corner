import React, { useState, useEffect } from 'react';
import useAuth from '../../hooks/useAuth';
import LikeButton from "../../components/Buttons/LikeButton/LikeButton";
import axios from 'axios';
import '../ProfilePage/ProfilePage.css'
import DislikeButton from '../../components/Buttons/DislikeButton/DislikeButton';
import UsersTable from './components/UsersTable/UsersTable';
import MyPosts from '../../components/MyPosts/MyPosts';
import FollowingPosts from '../../components/FollowingPosts/FollowingPosts';


const ProfilePage = (props) => {
   
    const [user, token] = useAuth();
    const [posts, setPosts] = useState([]);
    const [userPosts, setUserPosts] = useState([]);
    const [followers, setFollowers] = useState([]);
    const [following, setFollowing] = useState([]);
  
    // Here I think I will show there picture with an option to change it
    // Plus I think I will have a followers tab
    // Plus I think I will have a following tab
   
    useEffect(() => {

        getRecentPosts();
        getUserPosts();

        // fetchNewPosts();
        // fetchFollowers();
        
      }, [])

        async function getRecentPosts() {
            try {
                let postsResponse = await axios.get(`http://127.0.0.1:8000/api/posts/${user.id}/`);

                let tempPostsResponse = postsResponse.data;

                tempPostsResponse = tempPostsResponse.filter(function(el) {
            
                    return el.user.id != user.id
                });
                //tempPostsResponse.slice(0,19); // Limits to 20 posts (I may move this to the backend)
                setPosts(tempPostsResponse);
            } catch (error) {
                console.log(error.response.data);
            }
        }

        async function deletePost(id) {
            let response = await axios.delete(`http://127.0.0.1:8000/api/posts/delete/${id}`);
            getRecentPosts();
        }

        async function getFollowers() {
            try {
                let followersResponse = await axios.get('http://127.0.0.1:8000/api/followers/list/', {
                    headers: {
                        Authorization : "Bearer " + token,
                    },
                });
                console.log(followersResponse.data);
                setFollowers(followersResponse);
            } catch (error) {
                console.log(error.response.data);
            }
        }

        async function getFollowing() {
            try {
                let followingResponse = await axios.get(`http://127.0.0.1:8000/api/followers/`, {
                    headers: {
                        Authorization : "Bearer " + token,
                    },
                });

                setFollowing(followingResponse.data);
            } catch (error) {
                console.log(error.response.data);
            }
        }

        async function getUserPosts() {
            let tempMyPosts = posts.filter(function(el) {
            
                return el.user.id === user.id
            });
            setUserPosts(tempMyPosts);
            console.log(tempMyPosts)
        }

        async function getFollowingPosts() {
            let tempPosts = [];

            for(let i = 0; i < following.length; i++) {

                let posts = posts.filter(function(el) {

                return el.user.id === following[i].follower_user.id
                });   

            tempPosts = tempPosts.concat(following);
            // console.log(testPosts)
        
            }
        
  
            setPosts(tempPosts);
            console.log(posts)
        }

        async function likeOrDislikePost(id, type, data) {
            try {
                let followingResponse = await axios.patch(`http://127.0.0.1:8000/api/posts/type/${id}?type=${type}&value=${data}`, { type : data}, {
                    headers: {
                        Authorization : "Bearer " + token,
                    },
                });
                getRecentPosts();
            } catch (error) {
                console.log(error.response.data);
            }
        }

        // const dislikePost = async () => {
        //     try {
                
        //     } catch (error) {
                
        //     }
        // }
   
    return ( 
        <div className='profile-container'>
            <FollowingPosts  posts={posts} likeOrDislikePost={likeOrDislikePost} />
            <MyPosts userPosts={userPosts} deletPost={deletePost} />

            {/* <div className='profile-contatiner-posts'>
                <div className='profile-contatiner-create-post'>
                    <form>
                        <h3>Make a Post</h3>
                        <input type='text' placeholder='What game do you plan to talk about!'></input>
                        <button type='submit'>Post</button>
                    </form>
                    <h3>My Posts</h3>
                    <div>
                        {myPosts &&
                            myPosts.map((post) => {
                                return (
                                <div>
                                    <div className="container-post">
                                        {console.log(post)}
                                        <div className="container-post-user">
                                            <h3 key={post.id}>{post.user.username}</h3>
                                        </div>
                                        <div className="container-post-content">
                                            <p key={post.id}>{post.post_content}</p>
                                        </div>
                                        <div className='delete-button'>
                                            <a className='delete-button-tag' key={post.id} onClick={() => deletePost(post.id)}>Delete</a>

                                        </div>
                                    </div>
                                </div>
                                )
                                })}
                        
                    </div>
                        
                </div>
            </div> */}
                <div className='profile-contatiner-modify-profile'>
            
                </div>
                

            <div className='profile-container-followers-followed'>
                <UsersTable />
            </div>

       </div>
    );

       

}
 
export default ProfilePage;