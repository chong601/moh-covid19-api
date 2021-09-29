from flask_restx import Namespace, Resource

api = Namespace('miscellaneous', 'Additional information about this website')

@api.route('/about_me')
class ShillTime(Resource):
    def get(self):
        
        shill_time = {
            "github_repo": "https://github.com/chong601/moh-covid19-api",
            "creator": "Chong Jin Yi",
            "github_profile": "https://github.com/chong601",
            "hosted_on": "OVHcloud",
            "hoster_website": "https://www.ovh.com/asia",
            "support_me": "https://www.buymeacoffee.com/chong601",
            "open_to_work": True,
            "preferred_work" : [
                "Python Software Developer",
                "Systems Administration",
                "Network Administration",
                "DevOps Engineer",
                "Datacenter Technician"
            ]
        }

        return shill_time
