from django.test import TestCase
from .models import Candidatos

# Create your tests here.
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

# =======================================================================================
#                   tests verbose name labels class candidato
# =======================================================================================


class CandidatosModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Candidatos.objects.create(nome ='fulano', email='exemplo@server.com')

    # ========================================================================
    #                           TESTEANDO  OS LABELS 
    # ========================================================================
    def test_nome_label(self):
        candidato = Candidatos.objects.get(id=1)
        field_label = candidato._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')
    
    def test_cpf_label(self):
        candidato = Candidatos.objects.get(id=1)
        field_label = candidato._meta.get_field('cpf').verbose_name
        self.assertEquals(field_label, 'cpf')

    def test_email_label(self):
        candidato=Candidatos.objects.get(id=1)
        field_label = candidato._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'Email')

    def test_disp_trab_imed_label(self):
        candidato=Candidatos.objects.get(id=1)
        field_label = candidato._meta.get_field('disp_trab_imed').verbose_name
        self.assertEquals(field_label, 'Disponibilidade Imediata de Trabalho')

    def test_pret_salarial(self):
        candidato = Candidatos.objects.get(id=1)
        field_label = candidato._meta.get_field('pret_salarial').verbose_name
        self.assertEquals(field_label, 'Pretenção Salarial')

    # =========================================================================
    #                   TESTANDO RESTRICOES DOS CAMPOS 
    # =========================================================================

    def test_email_max_length(self):
        candidato = Candidatos.objects.get(id=1)
        max_length = author._meta.get_field('email').max_length
        self.assertEquals(max_length, 100)

    def test_cpf_max_length(self):
        candidato = Candidatos.objects.get(id=1)
        max_length = author._meta.get_field('cpf').max_length
        self.assertEquals(max_length, 11)
    
    def test_disp_trab_imed_max_length(self):
        candidato = Candidatos.objects.get(id=1)
        max_length = author._meta.get_field('disp_trab_imed').max_length
        self.assertEquals(max_length, 1)
    
    def test_nome_max_length(self):
        candidato = Candidatos.objects.get(id=1)
        max_length = author._meta.get_field('nome').max_length
        self.assertEquals(max_length, 100)

    ''' MUdar depois 
    def test_pret_salarial_max_length(self):
        candidato = Candidatos.objects.get(id=1)
        max_length = author._meta.get_field('pret_salarial').max_length
        self.assertEquals(max_length, 100)'''

    def test_idade_max_length(self):
        candidato = Candidatos.objects.get(id=1)
        MinValueValidator = author._meta.get_field('idade').MinValueValidator
        self.assertEquals(MinValueValidator, 18)


    def test_get_absolute_url(self):
        candidato = Candidatos.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(candidato.get_absolute_url(), '/candidato/1')

# =====================================================================================
#                                   VALIDANDO VIEWS 
# =====================================================================================

class CandidatosListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_candidatos = 5

        for candidatos_id in range(number_of_candidatos):
            Candidatos.objects.create(
                nome =f'Ericles Miller {candidatos_id}',
                email=f'ericles@gmail.com {candidatos_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/app/inicio/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/boasVindas.html')

    #=============================================================================

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/app/cadastro/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/candidato/cadastro.html')

    #==============================================================================
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/app/candidatos/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index_candidato'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index_candidato'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/candidato/index.html')

    # =============================================================================
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/app/editar/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('editar'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('editar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/candidato/editar_cadastro.html')

    # ==============================================================================
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/app/excluir/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('excuir'))
        self.assertEqual(response.status_code, 200)


    #================================================================================
    def test_pagination_is_five(self):
        response = self.client.get(reverse('candidatos'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['candidatos_list']) == 5)

    def test_lists_all_candidatos(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('candidatos')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['author_list']) == 5)


# ====================================================================================
#                                  Test view and forms 
# ====================================================================================

import uuid

class RenewCandidatoInstancesViewTest(TestCase):
    def setUp(self):
        
        #create a candidato
        test_candidato1 = Candidatos.objects.create(nome = 'Fulano',email='fulano@gmail.com', cpf='40200214758',
        pret_salarial='45000', disp_trab_imed='s', idade= 19)

        test_candidato2 = Candidatos.objects.create(nome = 'Ciclano',email='ciclano@gmail.com', cpf='402002546781',
        pret_salarial='1000', disp_trab_imed='n', idade= 33)
        # Create genre as a post-step
        genre_objects_for_candidato = Genre.objects.all()
        test_candiato.genre.set(genre_objects_for_candidato) # Direct assignment of many-to-many types not allowed.
        test_candidato.save()

        # listagem candidatos test
        

