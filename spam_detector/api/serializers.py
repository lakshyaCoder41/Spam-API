from rest_framework import serializers
from .models import User, Contact, PhoneNumber


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password=validated_data.pop('password',None)
        obj=self.Meta.model(**validated_data)

        if password is not None:
            obj.set_password(password)

        obj.save()
        return obj
        

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'phone_number', 'email')

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ('id', 'number', 'is_spam', 'owner_name')
