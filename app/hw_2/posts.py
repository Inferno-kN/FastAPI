from __future__ import annotations
from datetime import datetime, timezone
from annotated_types import MinLen, MaxLen
from fastapi import FastAPI, HTTPException, status, Depends
from markdown_it.common.html_re import comment
from pydantic import BaseModel, Field
from typing import Annotated, List


app = FastAPI()

# POSTS = {
#     "id": int,
#     "title": str,
#     "description": str,
#     "created_at": datetime,
#     "comments": [
#         {
#             "id": int,
#             "text": str,
#             "created_at": datetime
#         }
#     ]
# }


POSTS: List[Post] = []
NEXT_POST_ID = 1
NEXT_COMMENT_ID = 1


class Comment(BaseModel):
    id: int
    text: Annotated[str, MinLen(5)]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class CreatePost(BaseModel):
    title: Annotated[str, MinLen(5), MaxLen(255)]
    description: Annotated[str, MinLen(5)]


class CreateComment(BaseModel):
    text: Annotated[str, MinLen(5)]


class Post(CreatePost):
    id: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    comments: list[Comment]


async def check_post(post_id: int):
    for post in POSTS:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


async def check_comment(comment_id: int, post: Post = Depends(check_post)):
    for comment in post.comments:
        if comment.id == comment_id:
            return comment
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")


@app.post("/posts/{post_id}/comments", status_code=status.HTTP_201_CREATED, summary='Создаение коммента под постом', response_model=Comment)
async def create_comment(data: CreateComment, post: Post = Depends(check_post)):
    global NEXT_COMMENT_ID
    new_comment = Comment(id=NEXT_COMMENT_ID, text=data.text)
    post.comments.append(new_comment)
    NEXT_COMMENT_ID += 1
    return new_comment


@app.delete("/posts/{post_id}/comments/{comment_id}", summary="Удаляем комментарий", response_model=Comment)
async def delete_comment(comment: Comment = Depends(check_comment), post: Post = Depends(check_post)):
    post.comments.remove(comment)
    return comment


@app.put("/posts/{post_id}/comments/{comment_id}", summary="Обновляем комментарий", response_model=Comment)
async def update_comment(data: CreateComment, comment: Comment = Depends(check_comment)):
    comment.text = data.text
    return comment


@app.get("/posts/{post_id}/comments", summary='Получение всех комментов по айди поста', response_model=List[Comment])
async def get_comments(post: Post = Depends(check_post)):
    return post.comments


@app.get("/posts/{post_id}/comments/{comment_id}", summary="Получение коммента", response_model=Comment)
async def get_comment(comment: Comment = Depends(check_comment)):
    return comment



@app.get("/posts", summary='Получение всех постов', response_model=List[Post])
async def get_posts():
    return POSTS


@app.get("/posts/{post_id}", summary='Получение поста по его айди', response_model=Post)
async def get_post(post: Post = Depends(check_post)):
    return post


@app.post("/posts", status_code=status.HTTP_201_CREATED, summary='Создание поста', response_model=Post)
async def create_post(data: CreatePost):
    global NEXT_POST_ID
    post = Post(id=NEXT_POST_ID, comments=[], title=data.title, description=data.description)
    POSTS.append(post)
    NEXT_POST_ID += 1
    return post


@app.put("/posts/{post_id}", summary='Обновление поста', response_model=Post)
async def update_post(data: CreatePost, post: Post = Depends(check_post)):
    post.title = data.title
    post.description = data.description
    return post


@app.delete("/posts/{post_id}", summary='Удаление поста', response_model=Post)
async def delete_post(post: Post = Depends(check_post)):
    POSTS.remove(post)
    return post