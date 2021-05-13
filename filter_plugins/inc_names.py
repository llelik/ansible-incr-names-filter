#!/usr/bin/python
import re

class FilterModule(object):
    def filters(self):
        return {'new_name': self.increase_name}

    def increase_name(self, str2increase, specifier):
        index_dict = {}
        res_name = ''
        i=0
        j=0
        segments = []
      
       
        #'3DEDA{099,1}_030_{23,2}DOT'     3DEDA099_030_23_DOT
        

        ## find specifiers
        spec_list = re.findall('{\w+,\d+}',specifier)

        ## find indeces for specifiers
        index_spec_list = re.finditer('{\w+,\d+}',specifier)
        match_indeces = [m.start(0) for m in index_spec_list]

        
        ## find the rest parts of string name 
        not_spec_list = re.split('{\w+,\d+}',specifier)

        ## find indeces for NOT specifiers
        #index_no_spec_list = re.finditer('^(?!{\w+,\d+})',specifier)
        #no_match_indeces = [n.start(0) for n in index_no_spec_list]

        for segment in not_spec_list:
            segments.append(str2increase.find(segment))

        
        index_dict = dict(zip(match_indeces,spec_list))
        non_index_dict = dict(zip(segments,not_spec_list))






        print(not_spec_list)
        
        print(index_dict)
        print(non_index_dict)

        

        #res_name = specifier[0:5]+ str(int(spec_list[0].split(',')[0]) + int(spec_list[0].split(',')[1]))
        #print(res)
        return res_name    
