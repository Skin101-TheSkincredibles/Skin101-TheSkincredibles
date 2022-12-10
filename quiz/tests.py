from django.test import TestCase
from productdisplay.models import SkinCareItem,Tags
from quiz.views import Quiz

class QuizTestCase(TestCase):

    def setUp(self):

        Tags.objects.create(name='oily')
        oily = Tags.objects.get(name='oily')

        Tags.objects.create(name='sensitive')
        sensitive = Tags.objects.get(name='sensitive')

        Tags.objects.create(name='acne')
        acne = Tags.objects.get(name='acne')

        Tags.objects.create(name='dry')
        dry = Tags.objects.get(name='dry')

        Tags.objects.create(name='normal')
        normal = Tags.objects.get(name='normal')


        SkinCareItem.objects.create(name="Normal Toner",type="toner",tags=[normal],price="10.000")
        SkinCareItem.objects.create(name="Oil Dry Toner",type="toner",tags=[oily,dry],price="10.000")
        SkinCareItem.objects.create(name="Sensitive Toner",type="toner",tags=[sensitive],price="10.000")
        SkinCareItem.objects.create(name="Sensitive Acne Toner",type="toner",tags=[sensitive,acne],price="10.000")
        SkinCareItem.objects.create(name="Sensitive Acne Dry Toner",type="toner",tags=[sensitive,acne,dry],price="10.000")

    def test_quiz_validity(self):
        items = []
        nt = SkinCareItem.objects.get(name="Normal Toner")
        items.append(nt)

        odt = SkinCareItem.objects.get(name="Oil Dry Toner")
        items.append(odt)

        st = SkinCareItem.objects.get(name="Sensitive Toner")
        items.append(st)

        sat = SkinCareItem.objects.get(name="Sensitive Acne Toner")
        items.append(sat)

        sadt = SkinCareItem.objects.get(name="Sensitive Acne Dry Toner")
        items.append(sadt)

        quiz = Quiz()
        quiz.set_toner(items)

        oily = Tags.objects.get(name='oily')
        sensitive = Tags.objects.get(name='sensitive')
        acne = Tags.objects.get(name='acne')
        dry = Tags.objects.get(name='dry')
        normal = Tags.objects.get(name='normal')


        self.assertEqual(quiz.generate_recomendation([normal],'toner')[0], nt)
        self.assertEqual(quiz.generate_recomendation([oily,dry],'toner')[0], odt)
        self.assertEqual(quiz.generate_recomendation([sensitive],'toner')[0], st)
        self.assertEqual(quiz.generate_recomendation([sensitive,acne],'toner')[0], sat)
        self.assertEqual(quiz.generate_recomendation([sensitive,acne,dry],'toner')[0], sadt)