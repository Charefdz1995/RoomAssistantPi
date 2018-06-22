from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


TYPE_CHOICES = (
    ('light', 'Light'),
    ('fan', 'Fan'),
    ('door', 'Door'),
)
GPIO_NUM = (
    ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),
('11', '11'),('12', '12'),('13', '13'),('14', '14'),('15', '15'),('16', '16'),('17', '17'),('18', '18'),('19', '19'),('20', '20'),('21', '21'),
('22', '22'),('23', '23'),

)

class alarmform(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the question','type':'text'}))
    email = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the response','type':'text'}))
    phone = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the response','type':'text'}))
    gpio = forms.CharField(widget=forms.Select(attrs={'class':'form-control'},choices=GPIO_NUM))
    buzzer = forms.CharField(widget=forms.Select(attrs={'class':'form-control'},choices=GPIO_NUM))




class deviceform(forms.Form):
    type = forms.CharField(widget=forms.Select(attrs={'class':'form-control'},choices=TYPE_CHOICES))
    gpio = forms.CharField(widget=forms.Select(attrs={'class':'form-control'},choices=GPIO_NUM))
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={
                               'class':'form-control','placeholder':'Enter the name here','type':'text'}))
    oncom = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control', 'placeholder': 'Enter the name here', 'type': 'text'}))
    offcom = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control', 'placeholder': 'Enter the name here', 'type': 'text'}))




    def EnableRouting(self):
        output = None
        if (self.deviceType == 'Router' or self.deviceType == 'Layer3Switch'):
            ENV = Environment(loader=FileSystemLoader(str(MEDIA_ROOT[0]) + "/NetConfTemplates/"))
            template = ENV.get_template("eigrp2.j2")
            links = []
            interfaces = Interface.objects.filter(deviceRef = self)
            topology  = self.topologyRef
            eigrpData = EIGRP.objects.get(TopologyRef=topology)
            nopassive = []
            for interface in interfaces:
                link = Link.objects.get(id=interface.linkRef_id)
                list = Interface.objects.filter(linkRef=link).exclude(pk=interface.id)
                print(list[0].deviceRef.deviceType)
                if (list[0].deviceRef.deviceType !='Layer2Switch'):
                    nopassive.append(interface)
            output = template.render(eigrpIns=eigrpData,Interfaces =interfaces,Device =self,noPassive = nopassive )
        return output