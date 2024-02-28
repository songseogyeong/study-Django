const moreButton = document.getElementById("more");
    let page = 1
    const getList = (callback) => {
        fetch(`http://127.0.0.1:8000/post/list/${page}`)
        .then((response) => response.json())
        .then((posts) => {
            if(callback){
                callback(posts)
            }
        })
    }


    const showList = (post_info) => {
        if(!post_info.hasNext){
            moreButton.style.display = 'none'
        }
        let posts = post_info.posts
        const table = document.querySelector("table");
        posts.forEach((post) => {
            table.innerHTML += `
                <tr>
                    <td>${post.id}</td>
                    <td><a href="/post/detail/?id=${post.id}">${post.post_title}</a></td>
                    <td>${post.post_view_count}</td>
                    <td>${post.member_name}</td>
                </tr>
            `
        });
    }

    getList(showList);

    moreButton.addEventListener("click", (e) => {
        page ++;
        getList(showList);
    });