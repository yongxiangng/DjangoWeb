import datetime
from django.test import TestCase
from django.urls import reverse
from posts.models import Post
from awards.models import Award
from projects.models import Project

# Create your tests here.
class SimpleTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/') 
        self.assertEqual(response.status_code, 200)
        
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')
    
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
        
class AboutPageViewTest(TestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/about/')
        self.assertEqual(resp.status_code, 200)
        
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'about.html')

class AwardsPageViewTest(TestCase):
    def setUp(self):
        self.award = Award.objects.create(
            date=datetime.datetime(2020, 5, 17),
            title='A good title',
            description='Nice description',
        )
        
    def test_string_representation(self):
        award = Award(title='A sample title')
        self.assertEqual(str(award), award.title)
        
    def test_award_content(self):
        self.assertEqual(f'{self.award.date}', str(datetime.datetime(2020, 5, 17)))
        self.assertEqual(f'{self.award.title}', 'A good title')
        self.assertEqual(f'{self.award.description}', 'Nice description')
        
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/awards/')
        self.assertEqual(resp.status_code, 200)
        
    def test_award_list_view(self):
        response = self.client.get(reverse('awards'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice description')
        self.assertTemplateUsed(response, 'award.html')

class ProjectsPageViewTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title='A good title',
            abstract='A nice abstract',
            description='Nice description',
            code='https://www.google.com/',
            deployment='https://www.google.com/',
        )
        
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/projects/')
        self.assertEqual(resp.status_code, 200)
    
    def test_string_representation(self):
        project = Project(title='A sample title')
        self.assertEqual(str(project), project.title)
    
    def test_project_content(self):
        self.assertEqual(f'{self.project.title}', 'A good title')
        self.assertEqual(f'{self.project.abstract}', 'A nice abstract')
        self.assertEqual(f'{self.project.description}', 'Nice description')
        self.assertEqual(f'{self.project.code}', 'https://www.google.com/')
        self.assertEqual(f'{self.project.deployment}', 'https://www.google.com/')
        
    def test_award_list_view(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A nice abstract')
        self.assertTemplateUsed(response, 'project.html')
        
    def test_post_detail_view(self):
        response = self.client.get('/projects/1/')
        no_response = self.client.get('/projects/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'project_detail.html')
