from django.shortcuts import render, get_object_or_404,redirect
from .models import Comment,Reply
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .form import CommentForm,ReplyForm
from django.contrib import messages
