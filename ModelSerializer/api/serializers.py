from rest_framework import serializers
from .models import Student
# Modelserializer validation   validators , field level validation, object lavel validations all thess work in same modelserializer as normal serializer 

# all method of crud operation working correctly for modelserializer  
class StudentSerializer(serializers.ModelSerializer):

    def start_with_a(value):
        if value.lower()[0] != 'a':
            raise serializers.ValidationError("Name does not start with 'A' " )

    name=serializers.CharField(validators=[start_with_a])
    # first way
    # name=serializers.CharField(read_only=True)  # read_only property tells data is only can be read not write
    class Meta:
        model=Student
        fields=['id','name','roll_no','city']
        # read_only_fields=['city']   # second way
        #third way
        extra_kwargs={'name':{'read_only':True}}   # specify property of a single or multiple fields 


    # field level validation
    def validate_roll_no(self,value):
        if value>100:
            raise serializers.ValidationError("Seat full ")
        return value

    # object level validation
    def validate(self, data):
        nm=data.get('name')
        ct=data.get('city')
        if ct.lower() =='delhi' and nm.lower() =='aakash':
            return data
        raise serializers.ValidationError('City and Name are wrong')
