function like(post_id) {
  const likeCount = document.getElementById(`likes-count-${post_id}`);
  const likeButton = document.getElementById(`like-button-${post_id}`);

  fetch(`/like-post/${postId}`, { method: "POST" })
    .then((res) => res.json())
    .then((data) => {
      likeCount.innerHTML = data["likes"];
      if (data["liked"] === true) {
        likeButton.className = "fas fa-thumbs-up";
      } else {
        likeButton.className = "far fa-thumbs-up";
      }
    }).catch((e) => alert("Could not like post."));
}
