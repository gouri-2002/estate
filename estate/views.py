from django.shortcuts import render,redirect

from django.views.generic import View

from estate.forms import EstateForm

from estate.models import Estate

class EstateCreateView(View):

    template_name="estate_add.html"

    form_class=EstateForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES)

        if form_instance.is_valid():

            form_instance.save()


            return redirect("estate-list")
        
        
        return render(request,self.template_name,{"form":form_instance})
    
class EstateListView(View):

    template_name="estate_list.html"
    
    def get(self,request,*args,**kwargs):

        qs=Estate.objects.all()
        
        return render(request,self.template_name,{"data":qs})



class EstateDetailView(View):
    
    template_name="estate_details.html"

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Estate.objects.get(id=id)

        return render(request,self.template_name,{"data":qs})


class EstateDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Estate.objects.get(id=id).delete()
        
        return redirect("estate-list")


class EstateUpdateView(View):

    template_name="estate_update.html"

    form_class=EstateForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        estate_object=Estate.objects.get(id=id)

        form_instance=self.form_class(instance=estate_object)

        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        estate_objects=Estate.objects.get(id=id)
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data,files=request.FILES,instance=estate_objects)
        
        if form_instance.is_valid():
            
            form_instance.save()

            
            return  redirect("estate-list")
        
        
        return render(request,self.template_name,{"form":form_instance})








