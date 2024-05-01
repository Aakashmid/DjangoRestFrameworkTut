from rest_framework import serializers
from .models import Student


# Validators : we can create method for specific field and pass its name as validators argument in that field serilization
def start_with_a(value):
    if value.lower()[0] != 'a':
        raise serializers.ValidationError("Name does not start with 'A' " )

class StudentSerilizers(serializers.Serializer):
    name=serializers.CharField(max_length=50,validators=[start_with_a])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)     #** used to unpack dictionary key value pair 
    

    # Field validataion 
    # syntax  : def validate_(field name)(self,value ):  # here value is this field value
    # example
    def validate_roll(self,value):
        if value>100:
            raise serializers.ValidationError("Seat full ")
        return value
    
    
    # Object level validation  : for validation of whole data
    def validate(self, data):
        nm=data.get('name')
        ct=data.get('city')
        if len(ct)>4 and len(nm)>4:
            return data
        raise serializers.ValidationError('City and Name must be greater thant length 4')  # error json is "{'non_field_errors': ['Name and city first letter is wrong ']}"

