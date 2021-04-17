import pandas as pd
import logging
from time import strftime
import matplotlib.pyplot as plt
import pickle
import json

# =======================================================
#
# =======================================================
def clean_article(article):
    """ Text """    

    article_str = str(article)
    article_str = article_str[12:]
    article_str = article_str[:-26]
    
    return article_str

# =======================================================
#
# =======================================================
def clean_article_new(article,src_type):
    """ Text """    

    article_str = str(article)
    
    if src_type == "newsroom":    
        article_str = article_str[2:]
        article_str = article_str[:-1]

    if src_type == "multi_news":    
        article_str = article_str[2:]
        article_str = article_str[:-6]
        
    if src_type == "cnn_dailymail":    
        article_str = article_str[2:]
        article_str = article_str[:-1]
                   
    return str(article_str)
# =======================================================
#
# =======================================================

# =======================================================
#
# =======================================================
def clean_high_new(article,src_type):
    """ Text """    

    article_str = str(article)
    
    if src_type == "newsroom":    
        article_str = article_str[2:]
        article_str = article_str[:-1]

    if src_type == "multi_news":    
        article_str = article_str[2:]
        article_str = article_str[:-1]
        
    if src_type == "cnn_dailymail":    
        article_str = article_str[2:]
        article_str = article_str[:-1]
                       
    return str(article_str)
# =======================================================
#
# =======================================================