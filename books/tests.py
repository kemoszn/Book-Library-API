# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category


class CategoryTests(APITestCase):
    def create_category(self, name):
        url = reverse('category-list')
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response

    def test_create_and_retrieve_category(self):
        """
        Ensure we can create a new Category and then retrieve it
        """
        new_category_name = 'New Book Category'
        response = self.create_category(new_category_name)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(
            Category.objects.get().name,
            new_category_name)
        print("PK {0}".format(Category.objects.get().pk))


    def test_create_duplicated_category(self):
        """
        Ensure we can create a new Category.
        """
        url = reverse('category-list')
        new_category_name = 'New Category'
        data = {'name': new_category_name}
        response1 = self.create_category(new_category_name)
        self.assertEqual(
            response1.status_code,
            status.HTTP_201_CREATED)
        response2 = self.create_category(new_category_name)
        self.assertEqual(
            response2.status_code,
            status.HTTP_400_BAD_REQUEST)

    def test_retrieve_categories_list(self):
        """
        Ensure we can retrieve a category
        """
        new_category_name = 'New Category'
        self.create_category(new_category_name)
        url = reverse('category-list')
        response = self.client.get(url, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)
        self.assertEqual(
            response.data['count'],
            1)
        self.assertEqual(
            response.data['results'][0]['name'],
            new_category_name)

    def test_update_category(self):
        """
        Ensure we can update a single field for a category
        """
        new_category_name = 'Initial Name'
        response = self.create_category(new_category_name)
        url = reverse(
            'category-detail',
            None,
            {response.data['pk']})
        updated_category_name = 'Updated Category Name'
        data = {'name': updated_category_name}
        patch_response = self.client.patch(url, data, format='json')
        self.assertEqual(
            patch_response.status_code,
            status.HTTP_200_OK)
        self.assertEqual(
            patch_response.data['name'],
            updated_category_name)
            '''
    def test_filter_category_by_name(self):
        """
        Ensure we can filter a category by name
        """
        category_name1 = 'First category name'
        self.create_category(category_name1)
        caregory_name2 = 'Second category name'
        self.create_category(category_name2)
        filter_by_name = { 'name' : category_name1 }
        url = '{0}?{1}'.format(
        reverse('category-list'),
        urlencode(filter_by_name))
        response = self.client.get(url, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)
        self.assertEqual(
            response.data['count'],
            1)
        self.assertEqual(
            response.data['results'][0]['name'],
            category_name1)
        '''
