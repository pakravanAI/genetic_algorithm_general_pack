from random import randint


start = 0
finish = 100

class mathmatics_and_data_storage:
    def abs(N):
        if N == 0:
            return 0
        
        if N > 0:
            return N
        
        if N < 0:
            return N - 2*N
        
    def range_calc(fitness_list,delta,N):
        mult = 1
        chips = delta / N
        range_list = [start]
        __start__ = fitness_list[0]
        for i in range(N):
            range_list.append(start + (chips * mult))
            mult = mult + 1
        
        return range_list

    class array():

        def make():
            array_base = []
            return []
        
        def add(item,contaner):
            
            if contaner != dict:
                ValueError

            contaner.append(item)


       

        

class GA_general:

    #genetic data crator
    def gene(start,finish,cromosomes,sort):
        DNA = []
        #if start is bigger than finish so does not error
        if start > finish:
            for i in range(cromosomes):
                DNA.append(randint(finish,start))
        #if start is smaller than finish so does not error
        elif finish > start:
            for i in range(cromosomes):
                DNA.append(randint(start,finish))
        else:
            ValueError




    def sort_gene(start,finish,DNA):
            if start > finish:
                DNA.sort()
                DNA.reverse()
                return DNA
            
            elif finish > start:
                DNA.sort()
                return DNA



    def fitness_calc(gene):
        check_number = 0
        check_out = 0
        for i in range(len(gene)):
            check_out = check_out + gene[check_number]
            check_number = check_number + 1
        
        return check_out
        

    def offspring(gene1,gene2):
        offspringDNA = []
        copy_number = 0
        cut_number = randint(1,len(gene1)-1)
        if randint(0,100)>50:

            for i in range(cut_number):
                offspringDNA.append(gene1[copy_number])

            for i in range(len(gene2)-cut_number):
                offspringDNA.append(gene2[copy_number])

        else:

            for i in range(cut_number):
                offspringDNA.append(gene2[copy_number])

            for i in range(len(gene1)-cut_number):
               offspringDNA.append(gene1[copy_number])


        return offspringDNA


    def mutation(rate, gene):
        copy_checker = 0
        for i in range(len(gene)):
            if randint(0,100)<rate or randint(0,100)==rate:
                gene[copy_checker] = randint(start,finish)
            copy_checker = copy_checker + 1

        return gene


class N_slection():


    def fit_list(gene_array):
         check_place = 0
         gene_array_fitness = []

         for i in range(len(gene_array)):
            gene_array_fitness.append(GA_general.fitness_calc(gene_array[check_place]))
            check_place = check_place + 1

         return gene_array_fitness

    def delta_F(gene_array):
        
        gene_array_fitness = N_slection.fit_list(gene_array)

        

        gene_array_fitness.sort()
        F_high = gene_array_fitness[-1]
        F_low = gene_array_fitness[0]

        delta = mathmatics_and_data_storage.abs(F_high - F_low)

        return delta
    
    def del_low_fit(fit_list ,gene_list ,rate):
        check = 0

        if (not rate > 1) and (not rate < 0):
            ValueError


        lst_2 = gene_list
        lst_2.sort()
        least = lst_2[0]
        most = lst_2[-1]

        minmum_fitness_index = most * rate + least

        for i in range(len(gene_list)):
            if gene_list[check] < minmum_fitness_index:
                gene_list[check] = 0
                fit_list[check] = 0

            check = check + 1

        return gene_list



    def export(gene_list):
        check = 0
        export_list = []

        for i in range(len(gene_list)):
            if not gene_list[check] == 0:
                export_list.append(gene_list[check])

        return export_list
    
class SSlection():

    def tier_genes(gene_list ,fit_list ,range_list):
        check = 0
        check_squerd = 0
        tierd_genes = []
        for i in range(len(gene_list)):
            for i in range(len(range_list)):

                if fit_list[check] > range_list[check_squerd]:
                    check_squerd = check_squerd + 1

                else:
                    tierd_genes.append(check_squerd)
                    check_squerd = 0
                
            check = check + 1


    def offspring_rate(parant1 ,parant2):
        round(parant1 + parant2 / 4)


    def mate_finder(gene_list, tier_list):
        tier_range = 2

        genes = gene_list.copy()
        tiers = tier_list.copy()

        pairs = []
        singles = []

        while len(genes) > 0:
            found = False

            for j in range(1, len(genes)):
                if abs(tiers[0] - tiers[j]) <= tier_range:
                    pairs.append([genes[0], genes[j]])

                    # Remove mate first (higher index)
                    genes.pop(j)
                    tiers.pop(j)

                    # Remove current gene
                    genes.pop(0)
                    tiers.pop(0)

                    found = True
                    break

            if not found:
                singles.append(genes.pop(0))
                tiers.pop(0)

        

        return pairs

                    

#thanck you for seeing this it has been fun making this
#i would say go tell your friends about this cool repo but if you are reading this i dont think you will have friends(in case you do tell them)

    




