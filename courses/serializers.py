from rest_framework import serializers
from .models import Courses, CourseIntrest
from service.serializers import ProgrammingTechSerializer


class CoursesSerializer(serializers.ModelSerializer):
    technology = ProgrammingTechSerializer(many=True)

    class Meta:
        model = Courses
        fields = "__all__"


class CourseIntrestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseIntrest
        fields = "__all__"
