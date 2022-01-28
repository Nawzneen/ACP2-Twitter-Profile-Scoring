import json
import copy
from os import remove
import os.path
import random
import time

from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRequestError, TwitterConnectionError
from os.path import exists
from datetime import datetime
from common.logger import logger

import tas.tokens as osenv

bearer_token = osenv.bearer_token


def get_params(max_results=100, next_token=''):
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    params = {"tweet.fields": "attachments,author_id,context_annotations,conversation_id,created_at,entities,"
                              "geo,id,in_reply_to_user_id,lang,public_metrics,"
                              "possibly_sensitive,referenced_tweets,"
                              "reply_settings,source,text,withheld", 'max_results': max_results}
    if not next_token == '':
        params['pagination_token'] = next_token
    return params


def get_api():
    """
    Method required by bearer token authentication.
    """
    return TwitterAPI(osenv.consumer_key, osenv.consumer_secret, osenv.access_token, osenv.access_secret,
                      api_version='2')


def getTimelineByID(id=2244994945, max_results = 100):
    try:
        url = f'users/:{id}/tweets'
        params = get_params(max_results= max_results)
        api = get_api()
        while True:
            tweets = api.request(url, params)
            
            if tweets.status_code == 200:
                results = tweets.json()
                if 'data' in results.keys():
                    logger.info(tweets.get_quota())
                    return results['data']
                else:
                    return None
            else:
                reset = int(tweets.headers['x-rate-limit-reset'])
                reset = datetime.fromtimestamp(reset)
                logger.info("Sleep until:" + str(reset))
                nowt = datetime.now()
                diff = reset - nowt
                time.sleep(diff.total_seconds() + 2)

            # while 'next_token' in tweets.json()['meta'] and count < 2:
            #     next_token = tweets.json()['meta']['next_token']
            #     params = get_params(next_token=next_token)
            #     tweets = api.request(url, params)
            #     results.extend(tweets.json()['data'])
            #     count = count + 1

    except TwitterRequestError as e:
        logger.info('Request error')
        logger.info(e.status_code)
        for msg in iter(e):
            logger.info(msg)

    except TwitterConnectionError as e:
        logger.info('Connection error')
        logger.info(e)

    except Exception as e:
        logger.info('Exception')
        logger.info(e)


def getUserById(id=2244994945):
    try:
        url = f'users/:{id}'
        params = {"user.fields": "created_at,description,entities,id,location,name,pinned_tweet_id,"
                                 "profile_image_url,protected,public_metrics,url,username,verified,withheld"}
        api = get_api()
        while True:
            user = api.request(url, params)
            if user.status_code == 200:
                results = user.json()
                if 'data' in results.keys():
                    logger.info(user.get_quota())
                    return results['data']
                else:
                    return None
            else:
                reset = int(user.headers['x-rate-limit-reset'])
                reset = datetime.fromtimestamp(reset)
                logger.info("Sleep until:" + str(reset))
                nowt = datetime.now()
                diff = reset - nowt
                time.sleep(diff.total_seconds() + 2)

    except TwitterRequestError as e:
        logger.info('Request error')
        logger.info(e.status_code)
        for msg in iter(e):
            logger.info(msg)

    except TwitterConnectionError as e:
        logger.info('Connection error')
        logger.info(e)

    except Exception as e:
        logger.info('Exception')
        logger.info(e)

def getUserByName(name='jack'):
    try:
        url = f'users/by/username/:{name}'
        params = {"user.fields": "created_at,description,entities,id,location,name,pinned_tweet_id,"
                                 "profile_image_url,protected,public_metrics,url,username,verified,withheld"}
        api = get_api()
        while True:
            user = api.request(url, params)            
            if user.status_code == 200:
                results = user.json()
                if 'data' in results.keys():
                    logger.info(user.get_quota())
                    return results['data']
                else:
                    return None
            else:                
                reset = int(user.headers['x-rate-limit-reset'])
                reset = datetime.fromtimestamp(reset)
                logger.info("Sleep until:" + str(reset))
                nowt = datetime.now()
                diff = reset - nowt
                time.sleep(diff.total_seconds() + 2)
    except TwitterRequestError as e:
        logger.info('Request error')
        logger.info(e.status_code)
        for msg in iter(e):
            logger.info(msg)

    except TwitterConnectionError as e:
        logger.info('Connection error')
        logger.info(e)

    except Exception as e:
        logger.info('Exception')
        logger.info(e)

def getSingleUserByName(name='jack'):
    try:
        url = f'users/by/username/:{name}'
        params = {"user.fields": "created_at,description,entities,id,location,name,pinned_tweet_id,"
                                 "profile_image_url,protected,public_metrics,url,username,verified,withheld"}
        api = get_api()
        while True:
            user = api.request(url, params)            
            if user.status_code == 200:
                results = user.json()
                if 'data' in results.keys():
                    logger.info(user.get_quota())
                    return results['data']
                else:
                    return None
            elif user.status_code == 400:
                return 404
            else:                
                return None

    except TwitterRequestError as e:
        logger.info('Request error')
        logger.info(e.status_code)
        for msg in iter(e):
            logger.info(msg)

    except TwitterConnectionError as e:
        logger.info('Connection error')
        logger.info(e)

    except Exception as e:
        logger.info('Exception')
        logger.info(e)



def getFollowing(id=2244994945):
    try:
        api = get_api()
        logger.info(str(id))
        url = f'users/:{id}/following'
        params = {'max_results': 1000}
        # Get following
        while True:
            following = api.request(url, params)
            if following.status_code == 200:
                results = following.json()
                if 'data' in results.keys():
                    return results['data'], following.get_quota()
                else:
                    return None, None
            else:
                reset = int(following.headers['x-rate-limit-reset'])
                reset = datetime.fromtimestamp(reset)
                logger.info("Sleep until:" + str(reset))
                nowt = datetime.now()
                diff = reset - nowt
                time.sleep(diff.total_seconds() + 2)


    except TwitterRequestError as e:
        logger.info(e.status_code)
        for msg in iter(e):
            logger.info(msg)

    except TwitterConnectionError as e:
        logger.info(e)

    except Exception as e:
        logger.info(e)


idlistPath = 'idList2.txt'
iterationIDListPath = 'iterationIDList.txt'
iteratedIndexPath = 'iteratedIndex.txt'


def getIdListForCrawling():
    if exists(idlistPath) and exists(iteratedIndexPath) and exists(iterationIDListPath):
        with open(iterationIDListPath, 'r') as f:
            iterationUserIdList = f.readlines()
            iterationUserIdList = list(map(int, iterationUserIdList))
        with open(idlistPath, 'r') as f:
            results = f.readlines()
            results = list(map(int, results))

        with open(iteratedIndexPath, "r", encoding="utf-8", errors='ignore') as f:
            data = f.readline()
            i = int(data)
        iterated = set(iterationUserIdList[:i])

    else:
        iterationUserIdList = ['580097412',  # Celebrity Chris Evans
                               '813286',  # Former President Barack Obama
                               '141664648',  # Athlete John Cena
                               '2557037323',  # Novelist George RR Martin
                               '4416456732',  # Professor of Neurobiology at Stanford Andrew D. Huberman
                               '44196397',  # CEO of Tesla Elon Musk
                               ]
        iterated = set()
        results = copy.deepcopy(iterationUserIdList)
        i = 0
    while True:
        if i >= 600: break
        if not iterationUserIdList[i] in iterated:
            userprofile = getUserById(iterationUserIdList[i])
            if not userprofile is None:
                if 'protected' in userprofile.keys():
                    if not userprofile["protected"]:
                        fo, quota = getFollowing(iterationUserIdList[i])
                        if not (fo is None and quota is None):
                            logger.info(quota)
                            temp = []
                            for f in fo:
                                if not f['id'] in results:
                                    temp.append(f['id'])
                            results.extend(temp)
                            for k in range(len(temp)):
                                if k <= 5:
                                    iterationUserIdList.append(temp[k])
                            iterated.add(iterationUserIdList[i])

        i = i + 1
        if i % 15 == 0:
            logger.info('writing to txt')
            fileObject = open(idlistPath, 'w')
            for id in results:
                fileObject.write(str(id))
                fileObject.write('\n')
            fileObject.close()

            fileObject = open(iterationIDListPath, 'w')
            for id in iterationUserIdList:
                fileObject.write(str(id))
                fileObject.write('\n')
            fileObject.close()

            fileObject = open(iteratedIndexPath, 'w')
            fileObject.write(str(i))
            fileObject.close()


profilesBase = 'profiles'


def crawlingProfiles():
    if exists(idlistPath):
        with open(idlistPath, 'r') as f:
            results = f.readlines()
            results = list(map(int, results))
        if len(results) == 0:
            logger.info('Empty file')
        else:
            count = len(results)
            for index, id in enumerate(results):
                logger.info(str(id) + '    ' + str(index / count))
                filepath = os.path.join(profilesBase, str(id))
                if exists(filepath):
                    userprofile = getUserById(id)
                    if userprofile is not None:
                        if 'protected' in userprofile.keys():
                            if not userprofile["protected"]:
                                tweets = getTimelineByID(id)
                                userprofile['tweets'] = tweets
                                if len(tweets)>5:
                                    fileObject = open(filepath, 'w+')
                                    json.dump(userprofile, fileObject)
                                    fileObject.close()
                                else:
                                    if exists(filepath):
                                        remove(filepath)
                            else:
                                if exists(filepath):
                                    remove(filepath)

                else:
                    logger.info('Existed' + ' ' + str(id))

    else:
        logger.info('no id list file')

def getProfileByUsername(name = 'jack'):
    userprofile = getUserByName(name)
    if userprofile is not None:
        if 'protected' in userprofile.keys():
            if not userprofile["protected"]:
                tweets = getTimelineByID(int(userprofile['id']), max_results= 20)
                userprofile['tweets'] = tweets
    return userprofile

def getSingleProfileByUsername(name = 'jack'):
    userprofile = getSingleUserByName(name)
    if userprofile is not None and userprofile != 404:
        if 'protected' in userprofile.keys():
            if not userprofile["protected"]:
                tweets = getTimelineByID(int(userprofile['id']), max_results= 20)
                userprofile['tweets'] = tweets
    return userprofile


if __name__ == "__main__":
    #crawlingProfiles()
    logger.info(getProfileByUsername())
