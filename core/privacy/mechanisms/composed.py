from core.privacy.mechanisms.commons import GaussianMechanism
from core.privacy.mechanisms.noisy import NoisyMechanism
from autodp.transformer_zoo import ComposeGaussian, Composition
from autodp.mechanism_zoo import ExactGaussianMechanism


class ComposedNoisyMechanism(NoisyMechanism):
    def __init__(self, 
                 noise_scale: float, 
                 mechanism_list: list[NoisyMechanism], 
                 coeff_list: list[float]=None,
                 weight_list: list[float]=None,
                 ):
        super().__init__(noise_scale)
        if coeff_list is None:
            coeff_list = [1] * len(mechanism_list)
        if weight_list is None:
            weight_list = [1,1,4]
        self.params = {
            'noise_scale': noise_scale, 
            'mechanism_list': mechanism_list, 
            'coeff_list': coeff_list,
            'weight_list': weight_list
        }

        
        
        # final_zip = list(zip(mechanism_list, weight_list))
        # lst_ns = [noise_scale] *3
        # for i in range(len(final_zip)):
        #         if i == 0: 
        #             mechanism_list1 = [mech.update(weight * lst_ns[1]) for mech, weight in [final_zip[i]]]
        #         if i == 1: 
        #             mechanism_list2 = [mech.update(weight * lst_ns[2]) for mech, weight in [final_zip[i]]] 
        #         if i == 2:
        #             mechanism_list3 = [mech.update(weight * lst_ns[0]) for mech, weight in [final_zip[i]]] 

        # mechanism_list = mechanism_list1 + mechanism_list2 + mechanism_list3
        #print(noise_scale)
            


        mechanism_list = [mech.update(weight * noise_scale) for mech, weight in zip(mechanism_list, weight_list)]
        mech = Composition()(mechanism_list, coeff_list)
        self.set_all_representation(mech)
        #print(mechanism_list)
        #print(list(zip(mechanism_list, weight_list)))
        #print("length", len(list(zip(mechanism_list, weight_list))))
        #print(mech)


        


class ComposedGaussianMechanism(NoisyMechanism):
    def __init__(self, 
                 noise_scale: float, 
                 mechanism_list: list[GaussianMechanism], 
                 coeff_list: list[float]
                 ):
        super().__init__(noise_scale)
        self.params = {'noise_scale': noise_scale, 'mechanism_list': mechanism_list, 'coeff_list': coeff_list}
        mechanism_list = [mech.update(noise_scale) for mech in mechanism_list]
        gm_list = [ExactGaussianMechanism(sigma=mech.params['noise_scale']) for mech in mechanism_list]
        mech = ComposeGaussian()(gm_list, coeff_list)
        self.set_all_representation(mech)
        #print("noise scale", noise_scale )
        #print("mechanism_list", mechanism_list)
        #print('coeff_list', coeff_list)
        #print("gm list", gm_list)
