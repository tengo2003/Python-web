from flask import Flask, jsonify, request, redirect
from flask_restful import Api, Resource
import validators
import shortuuid
import datetime


urls = {}

class URLShortener(Resource):
    def post(self):
        url = request.json.get('url')
        if not url:
            return {'error': 'URL is required.'}, 400
        if not validators.url(url):
            return {'error': 'Invalid URL.'}, 400
        short_name = shortuuid.uuid()[:7]
        urls[short_name] = {'url': url, 'created': datetime.datetime.utcnow(), 'counter': 0}
        return {'short_url': f'/url/{short_name}'}, 201

class PremiumURLShortener(Resource):
    def post(self, custom):
        url = request.json.get('url')
        if not url:
            return {'error': 'URL is required.'}, 400
        if not validators.url(url):
            return {'error': 'Invalid URL.'}, 400
        if custom in urls:
            return {'error': 'Custom name already in use.'}, 400
        urls[custom] = {'url': url, 'created': datetime.datetime.utcnow(), 'counter': 0}
        return {'short_url': f'/url/{custom}'}, 201

class URLRedirect(Resource):
    def get(self, short_name):
        if short_name not in urls:
            return {'error': 'URL not found.'}, 404
        urls[short_name]['counter'] += 1
        return redirect(urls[short_name]['url'], code=302)

class URLInfo(Resource):
    def get(self, short_name):
        if short_name not in urls:
            return {'error': 'URL not found.'}, 404
        return {'url': urls[short_name]['url'], 'created': urls[short_name]['created'].isoformat(), 'counter': urls[short_name]['counter']}

def delete_old_urls():
    for short_name, data in urls.items():
        if (datetime.datetime.utcnow() - data['created']).days >= 30:
            del urls[short_name]

app = Flask(__name__)
api = Api(app)
api.add_resource(URLShortener, '/url')
api.add_resource(PremiumURLShortener, '/url/<string:custom>')
api.add_resource(URLRedirect, '/<string:short_name>')
api.add_resource(URLInfo, '/url/<string:short_name>')

from threading import Timer
t = Timer(86400.0, delete_old_urls) #