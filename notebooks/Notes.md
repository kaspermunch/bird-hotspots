
# Results outline

## Questions for Jonas

- Is the 100kb bin from 500 to 1500?
- What proporties makes two signatures different (The absolute level can be due to Ne). So differences would need to be difference in shape? Maybe also plot the mean strengths that they are deviations from.

# TODO
- Try to make a more detailed figure showing dependence on CGI distance
- Plot GC* vs integrated bias
  
  
## Abstract
Avian recombination, in absence of location defining protein PRDM9, still occur in hotspots, which are mainly located in regions of the genome with open chromatin and unmethylated nucleotides. We propose a strong connection to replication origins, which have a known preference to co-occur with CGIs, and propose them as the fallback targets that will take over in absence of PRDM9. As previously suggested we confirm that the usage of hotspots seems stable across the entire avian phylogeny, with a few exceptions. The penguins showcase this where the two species in our dataset display presence and absence of substitution bias in hotspot regions respectively. Woodpecker, Turkey Vulture and Ostrich also display absence of bias. This could indicate absence of hotspots altogether or hotspots in different locations, either stable or dynamic.
 

## Figures

## Introduction

- In vertebrates, PRDM9 controll hotspot location
- Loss of PRDMN9 immobilizes hotspots, shown in dogs
- Hotspots lost in ancestor to birds and ??
- LD Hotspots shared among Finches
- Recombination affect substitutions through gBGC.
- This allow us to evaluate hotspot sharing in birs species represented by only a single genome.
- This has been used to show that hotspots are likely shred to some extent across paseriens.
- Here we investigate across all bird orders
- Make new accurate alignment

Meiosis is the essential biological process of forming haploid gametes, which occurs in all sexually reproducing eukaryotes. During meiosis homologous chromosomes get connected by physical links, synapsis, to direct their segregation into germ cells. To ensure correct segregation, at least one synapsis occurs per chromosome or chromosome arm per meiosis. During synapsis, homologous chromosomes exchange genetic material via genetic recombination, which shuffles existing alleles and creates new allelic combinations. New allelic combinations have new fitness values, and recombination thereby interacts with selective pressures by creating a wider array of targets. Distribution of synapsis is highly variable along the genome, but also turns out to be highly punctuate. Narrow regions of recombination hotspots have been identified in humans, and many additional organisms. These regions have up to orders of magnitude increased recombination rate.

Molecular mechanisms behind recombination events have been thoroughly investigated in several species, and they start with a double stranded break (DSB). After cutting the chromosome, the DSB is repaired with the homologous chromosome as a template, in one of several distinct pathways. Synaptic chromosome junctions are resolved as either crossovers, which reciprocally exchange entire chromosome arms, or as non-crossovers, which exchange only chromosome segments that form gene conversion tracts along the homologous chromosome. NCOs are the major outcome of DSB repair, while crossovers occur at a lower frequency. However, crossovers can more readily be identified with comparative genomics methods for detecting and quantifying recombination rate.
 
Many genes have been implicated in recombination, and are conserved across a variety of eukaryotes, but the number of recombination events vary as well as their distribution. Some species have high rates, and others low. Some species have hotspots, others don’t. In species with hotspots the location and intensity vary on many levels, even between individuals. More specifically, mammalian hotspots have been associated with the DNA-binding protein of PRDM9, which describes the location and dynamics of them. Birds lack it, but still display hotspots. Just like dogs with a disrupted gene sequence, altered mice and others. These hotspots are located in open chromatin, more accessible to proteins involved in recombination initiation. These regions have lower cytosine methylation, like CpG islands (CGIs).

Similar to dogs that lack a functional copy of PRDM9, previous analyses of conservation of hotspot locations across avian species have suggested a stable landscape in the absence of PRDM9(Singhal et al. 2015-11-20 ). Specifically, a clade of finches shared hotspots as far back as 20 million years in divergence time. This study intends to expand that observation to include a wider range of birds, which will be represented by the haploid genomes of the 48 species in the b10k consortium’s ordinal level project(Jarvis et al. 2014-Dec-12 ). These species span the entire clade of birds, and enables us to investigate properties of hotspot regions on a broad scale. As we lack the possibility to infer recombination rates directly from this data, we will reconstruct ancestral genomes and map finch hotspots to all genomes and derive their substitution patterns to investigate evidence of hotspot stability.

Genomic nucleotide composition near recombination associated DSBs is affected by the process gBGC, which favors transmission of G and C alleles over A and T alleles in GC:AT mismatches in gene conversion tracts. Regions of elevated recombination innately experience more DSBs, and therefore stronger transmission bias. However, this bias is independent of the fitness value of the transmitted allele. Therefore, the relative strength of the transmission bias in contrast to the selection coefficient of the alternative allele determines whether gBGC increases or decreases natural selection. At high values, gBGC can have substantial negative fitness effects.
 
Replication origins (ORIs) have been heavily implied in the creation and maintenance of CGIs. It is linked to transcription by being initiated in regions transcribed early which are therefore unmethylated and accessible to the replication machinery. The molecular dynamics of this process creates an asymmetric strand bias directed away from the replication origin. The bias is introduced as an effect of ssDNA mutability, which differs between the leading and the lagging strand due to their respective exposure as ssDNA. CpG-dinucleotides created by these mutations will be retained as these regions remain unmethylated. It also enables persistent locations of ORIs, due to transcriptional consistency. This manifests as conserved ORIs across wide ranges of taxa.
 
By using substitution biases as a proxy for recombination rate, stable recombination can be investigated with the compositional and substitutional biases of gBGC and replication. We observe and describe a strong link between recombination and replication, which causes clear compositional biases. We also find patterns that agree with stable hotspots, and highlight a few exceptions that require further scrutiny. We see a common reason behind the lack of evidence in some species.



# Results

### Zebra Finch Hotspots
We obtained recombination rates and hotspot locations inferred in zebra finch from Singhal et al. 2015, where hotspots were inferred for chromosome Z and chromosome 1-15 and 1A and 4A (the 17 largest autosomes, with enough power to detect hotspots due to background recombination rates between 0.0001 and 0.8 rho/bp). Throughout the paper we will refer to these regions as hotspots in all species, even if they have only been inferred in zebra finch. To enable hotspot alignment while maintaining maximum concurrence with the inference procedure, we define the central 1 kb as the hotspot, and the left and right 40kb flanking sequences as the flanks.

### Genome alignment
We adopted a new alignment strategy, which allows for simultaneous alignment and reconstruction of ancestral sequences. Inferring ancestral sequences enables investigations of substitution patterns and other analyses along specific branches of the phylogeny, which helps to pinpoint more precisely between which nodes observed changes occur. The aligner implementing the ancestral reconstruction feature is the Cactus aligner. Cactus requires a phylogenetic tree to use as a template for the alignment process, and then builds the alignment in a bottom-up fashion, aligning less diverged sequences first while inferring their ancestral sequence. It then proceeds to more and more diverged sequences, using the inferred ancestral sequences as new nodes to align. This procedure continues until all sequences have been aligned and all internal nodes in the phylogeny has been inferred.
We aligned the 48 bird genomes from the ordinal level of the bird10k project using the TENT tree from Jarvis et al. 2014 as a guide tree for the backbone of Cactus. The resulting Cactus alignment has several advantages over the MultiZ alignment used in that project. The MultiZ alignment do not reconstruct sequences at internal nodes, had genomes aligned to chicken, and averaged 25% of sequence aligned between genomes. Meanwhile, Cactus do reconstruct sequences at internal nodes, aligns genomes to the closest genome, and averaged 75% of sequence aligned between genomes (Fig. S1B). As we are interested in local patterns of evolution, the divergence-based alignment of Cactus serves as a better resource because it retains more evolutionary information from the sequences.
 
- New alignment: All species align to the others on average around 75% of genome-wide nucleotides (Fig sx). Hotspots align around 10% worse, probably reflecting more diverged sequences. Both genome and hotspots have a similar negative correlation between aligned nucleotides and number of substitutions (Fig sx).
- Number of aligned bases across hotspots.
    - SOM: Jonas alignment figure
    - SOM: Aligned bases
- We filter out windows with less than 300 aligned bases

## Substitution inference
The Cactus alignment allowed us to analyze a larger proportion of genomic sequence than previously possible with available resources, and to infer substitution patterns in a large majority of the genomic sequence. From the full alignment we extracted chromosomal alignments of all species and ancestral nodes with zebra finch (which has chromosomes assembled) as reference. We mapped the 2856 autosomal hotspots that have previously been identified in zebra finch onto the chromosomes, to investigate patterns of substitutions along the chromosomes in general and in hotspots in particular. All hotspots in a species were considered jointly when studying composition. Around 10% less sequence is aligned in hotspots compared to flanks for any branch, which likely represents the faster evolving and therefore more diverged sequence composition in hotspots.

- Substitution inference / ancestral sequence from cactus. We make a set both with and without CpG sites.
- Sustitution counts are divided by the TENT branch length

## gBGC
- GCflux, is calculated as the AT to GC over GC to AT substitution rate. The equilibrium GC content resulting from this bias, GC*, is calculated as GCflux/(1 + GCflux).

Assuming recombination hotspots evolve under the influence of gBGC, one would expect increased GC content because of the inherent long term increased WS substitution bias. All species have increased GC content, consistent with ancient presence of hotspots with gBGC. They also have increased WS substitution rate in hotspots (notable exception PICPU), consistent with current hotspots with ongoing gBGC. These observations meet the basic requirements of gBGC and support the stability of hotspots and presence of gBGC throughout the phylogeny.

### Hotspot sharing
 
With basic requirements for gBGC met, we also investigated whether the hotspots displayed the hallmark of a higher GC* than the flanks. Similar to previous findings, we observe a bias that decreases within a few kb of hotspot centers, driven by the increased WS substitution rate. This observation supports stable locations of recombination hotspots in the absence of PRDM9.
        	The only species without increased WS rate (and therefore GC*) is PICPU, which has increased presence of TEs where recombination happens. This could have started early along that branch, and thus no WS substitutions accumulated. Additionally, three additional species (STRCA, APTFO, CATAU) show a simultaneous increase in both WS and SW rate and thus no bias. These species are scatted across the phylogeny and seem to represent independent losses of evidence of hotspots. Both substitution rates increased would indicate a generally increased but unbiased substitution rate in hotspots[KMT1] . Generally increased substitution rate could possibly be explained by misalignment, and increased SW rate by a substitution pattern reverting composition back to basic GC content. This could be because of increased CpG-site formation, which have an increased substitution rate back to weak nucleotides. [KMT2] 
To compare the power to detect an increased GC* in different species, we performed a power analysis to identify above which threshold we could detect an increase. This revealed a similar power in all species, and an average detection limit of 4% increase and above. Figure 1 depicts the phylogeny along with the power to detect hotspots and representations of different levels of substitution biases around them.
 
Figure 2 depicts the branching and substitution pattern of the two penguins in the dataset. The ancestral branch displays the same bias as seen generally across the phylogeny. While the Adelie penguin (PYGAD) also display the bias, the emperor penguin (APTFO) does not. The other three species without increased GC* either have very long branches (PICPU), basal origin (STRCA) or lack close relatives (CATAU). However, the penguins have the opposite; short branches, terminal to a clade, and closely related. These factors make them ideal for looking into what is underlying the apparent lack of substitution bias in hotspots. Closer inspection of these branches may reveal factors behind the different substitution patterns[KMT3] . Assuming that common evolutionary explanations underlie the four independent events of bias loss, any identified events could be interrogated for their existence in the other three species as well.
        	The unique placement of the penguins in the phylogeny narrows down the loss of bias to a well-defined event on a specific branch. It is also unlikely that the difference is caused by some alignment artefact, as the two penguins are treated the same by the aligner due to their co-occurrence. Furthermore, they are both sequenced to a depth of 60x, which is higher than a majority of the samples, and unlikely represent poor quality sequence.
            
    - **Figure 1**
- The magnitude of the GCstar peak varies dramatically between birds. This is in part determined by the long-term species Ne.
- The woodpecker and ostrich show no or almost no GCstar peaks. That could be due to extremely small long-term Ne. However, in "Temporal Dynamics of Avian Populations during Pleistocene Revealed by Whole-Genome Sequences" these two species do not seem to show any inherrent tendency for such small population sizes. Another possible reason could be that the alignment is so poor for these species that the gBGC signal is "swamped" by false positive substitutions. However, if this was the case, then the hotspot which shows the fewest aligned bases should show a peak in all rates - which is does not.
- In fact, whereas the alignment quality does not seem to affect estimated rates, it does seem to be natural consequence of a higher recombination rate: more recombination will produce more structural variation that is harder to align. We analyze the dependency on alignmnet quality below.
- WS rate is increased in all species but PICPU. Additionally, SW rate is increased in APTFO, CATAU, and STRCA, (and some others…) but decreased in TAEGU, (and some others…). Increased WS rate is caused by gBGC. Increased or decreased SW rate is caused by (increased mutation rates around hotspots) (???).
- Some species show no sharing.
    - **GC* across hotspots for selected species (Zebra Finch, Bald Eagle, Two penguins, Woodpecker and Ostrich)**
    - SOM: GC* across hotspots for each species
- Other species show change in sharing over short branches.
- Stability of hotspots allow us to investiate gBGC substitution patterns.
- Signatures suggest that the degree of hotspot sharing does not decay with distance from TAEGU.
    - **Signatures**
    - SOM: All signatures

Sorting hotspots by GC* ratio of center to flanks, gives unique but similar signatures within each species, but sorting by average ratio across species largely retains this similarity. The species previously identified with deviating substitution patterns are less similar to the others. There is no particular phylogenetic ordering seen in this data.

The signatures of hotspot strengths show no decay with increasing distance to TAEGU, suggesting proportion of shared hotspots are not a function of phylogenetic distance.

While locations of hotspots largely remain stable across the phylogeny, the strengths of hotspots can vary independently between lineages or in a systematic manner.
If strengths of hotspots vary independently between lineages, a correlation with divergence would be expected as the strengths change over time. Pairwise co-variations between species were recorded and reported together with estimated pairwise nucleotide distances in Figure 3. [KMT4] The distinct patterns from the two measurements suggest there is no correlation between divergence and hotspot usage.
If, on the other hand, strengths of hotspots remain stable across lineages, a co-variance of hotpot strengths is expected between species. For each hotspot in each species we recorded the relative GC* compared to the flanks. We used the relative GC* values to infer a signature of hotspot usage per species, which is presented in Figure 4. These signatures indicate how the strength of hotspots co-varies between species. The four species displaying no substitution bias in the hotspots are specifically marked in the figure. Apart from an overall low level of substitution bias[KMT5] , they also show an overall low co-variation in hotspot usage to the other species[KMT6] .
The correlation of hotspot strengths across lineages suggests that both location and strength of hotspots remain stable. Simultaneously, the lack of such correlation in the four species lacking bias opens for a possibility that hotspots in those species moved elsewhere, and re-subjected the former hotspots to background substitution forces, slowly degenerating the traces of previous hotspots.

## Contributions to GC*
- Transversions contribute more strongly
- The background level in flanks of GCstar differs dramatically between transversion and transitions across species. That must be because transversions can be more of less GC-biased than transitions in each species. I.e. it varies accross species how much transitions and transversion contribute to equilibrium GC content.
    - **GC* ratio boxplot**
- CpG mutations do not seem to drive this.
    - SOM: GC* ratio boxplot including CpG
    
## Strength fo gBGC - B value
- Compute population scaled gBGC selection coeficient following box 1 in C. F. Mugal et al.: GC-biased gene conversion links the recombination landscape and demography to genomic base composition.
- B is estimated to 0.3, R is estimated to 1.5

## CGI, TSS, Promoters
- Confirm location close to CPG, TSS and promoters (as shown by Molly)
    - SOM: CGI, TSS, promoter proximity
- GC* ratio for Zebra finch is smaller in non-CGI hotspots.
    - **GC* ratio for GCI and non-GCI hotspots for selected species**
    - SOM: GC* ratio for GCI and non-GCI hotspots for all species
- This is also seen in other species, suggesting lower heat or lower sharing.
- Some species that share Finch hotspots (Flamingo, Crane) do not show this pattern, suggesting that a relatively higher sharing of non-CGI Finsh hotspots.
- Woodpecker even seems to show the opposite pattern, suggesting maybe that CGI hotspots are completely abandoned and that the the minor sharing is non-CGI hotspots.

## Substitution rates
- gBGC is show elevated substutition rates for substitutions except for GC to TA.
    - **Substitution ratio boxplot**
    - **Substitution rates for Bald Eagle and Downy Woodpecker.**
    - SOM: Subsitution rates across hotspot for all species.
- Effect of coverage: Note the difference in y-axis in the plots above. It seems to be the windows with fewer than 900 bases aligned (300-900) are the ones responsible for the large peak right at the center. This is probably a biological signal: windows with higher recombination have more structural variation. What is more important is that the AT conservative substututions do not seem to be affected. This suggests that the lower number of aligned bases in some windows is not due to misalignment as this would inflate all the rates at the hotspot center where there are fewest aligned bases.

## Replication orgins
- Substitutions rates mutation bias characteristic of replication origins.
- We konw CGI are are enriched for S-jumps show locatiosn are exactly the same but S-jumps reveal a coincidende within few thousand bases.
    - **S-jump for Bald Eagle, Downy Woodpecker, Ostrich and Zebra Finch.**
- GC* is not correlated with strand bias.
- Likely just two processes both relying on open chromatin. Use as replication origin remains in species where hotspots are not used.
- Replication-included mutation could also contribute in this region.

All species have an asymmetrically skewed substitution pattern around the hotspots. Upstream there is an increasing incorporation of A and C, and downstream there is an increasing incorporation of G and T. These skews are directed towards the hotspot center, at which they flip strand. All substitutions are skewed, but the main drivers are A>G and T>C substitutions.
Replication origins are known to create this kind of skew, due to different exposure of leading and lagging strands, yielding different mutation rates. There is also some evidence that recombination induced mutations are biased in a similar fashion.

Entirely separate from a GC-substitution bias inherent in recombination hotspots, we first observe a more basic bias in the nucleotide composition. When considering the 3000 hotspots jointly, there is a clear AC over GT bias decreasing to the left mirrored by a GT over AC bias decreasing to the right of the hotspot center (Figure X). This bias makes a narrow and drastic switch right at the hotspot center. The same analysis on 30,000 CGIs reveals a bias of the same direction and magnitude (Figure X), suggesting a common source more widespread than recombination.  This source is likely replication, that is known to cause such strand asymmetric biases in many species and is linked to creation of CGIs. Replication origins, ORIs, are also conserved over large evolutionary scales and would maintain such compositional biases in divergent genomes. Thus, ORIs could provide a parallel source of target sites for recombination along PRDM9, but be the only remaining source once that gene is not there. (If they are spaced every 1-2Mb there should only be around 1000 though, so all CGIs could not be from there).
 

 
# Materials and Methods

## Recombination hotspots

 
## Genome alignments and ancestral reconstruction 
Genomic sequences for the 48 species of birds from the ordinal level of the bird10k project serve as the basis for our analyses. A phylogenetic tree (TENT) is available from Jarvis et al. 2014, as well as a MultiZ alignment in galGal3 coordinates which we converted to taeGut1 coordinates with mafTools.
We used the phylogenetic tree from Jarvis et al. 2014 as a guide tree to the Cactus alignment software to simultaneously obtain alignments of all the 48 genomes and reconstruction of ancestral genomes, which is possible due to a progressive alignment of sequences in a bottom-up fashion.  The resulting alignment was converted to MAF format with HAL tools, excluding paralogous edges with the --noDupes option. The MAF files were further manipulated with custom scripts to extract information in suitable formats for downstream analyses.
 
## Composition extraction
Each sequence had their total sequence composition, aligned sequence composition and substitution pattern recorded in 1kb non-overlapping bins. Total sequence composition applies to sequences and refers to the number of A, C, G, T, N and – (gaps) in a sequence in the alignment, whereas aligned sequence composition is a subset that applies to branches and refers to the number of A, C, G and T in a sequence where the ancestor also has an A, C, G or T. Substitution patterns were inferred from the aligned sequence composition and classified into S2W and W2S substitutions. Unless otherwise stated we always refer to the aligned sequence composition.
Sequences in the multiZ alignment gets no aligned sequence composition recorded, as that is hard to define in a regular MSA without ancestral sequences. Instead, we only record the total sequence composition and use the entire alignment to infer substitutions. For substitution inference we require 50% of the sequences to align and polarizes substitutions from major to minor allele of biallelic sites.
 
## Bias investigation
Across the entire alignment we extracted sequence composition in bins in a region around each hotspot. We superimposed these regions per sequence and calculated the GC* value for each superimposed bin. The regions were also bootstrapped 1000 times per sequence to obtain 95% confidence intervals for the GC* values. In order to determine whether the hotspot displayed a higher bias than the flanks, we checked for non-overlapping confidence intervals (or with a paired t-test?) of the bootstrapped GC* values for the hotspots and their flanks.
 
## Power analysis
In addition to investigating the substitution bias in hotspots, we also performed a conservative power analysis to determine how large effect was needed to observe a significant difference. We did this by skewing the number of different substitutions in the hotspots in each of the bootstrapped records, while maintaining the total number of substitutions, until their bias equaled the flanks. Then we stepwise skewed the substitution pattern back until the confidence intervals (again, paired t-test?) of the GC* values no longer overlapped and recorded this as the detection limit.
 
Let GC* be the equilibrium GC content and WS and SW the respective substitution rates. Let further b and h denote the background or hotspot for each record. Let finally p be the proportion of WS substitutions that needs to change polarity to equate the hotspot GC* with the background GC*. This procedure also works for negative p
 
## Signatures of hotspot usage
We recorded the relative GC* in the 1kb center of hotspots compared to the 40kb left and right flanks of hotspots for each species. For each hotspot location these values were averaged across species, sorted in descending order, and used to sort the hotspots of each species in the same order. For each species, a rolling average across 500 hotspots was applied to obtain the smoothed ‘signature’ of hotspot usage.

 
## Discussion
With a recent and actively developed alignment strategy of the Cactus aligner, we improve on the mapping contiguity of a previous MultiZ alignment of the 48 birds from the ordinal level of the b10k project (Fig S1). Proportion of aligned nucleotides between two genomes increase from 28% to 67%, making it more suitable for regions that evolve faster and aligns worse. As the MultiZ alignment was generated by aligning sequences to the chicken genome, which aligns worst to the others, this further limits the usefulness of that approach. In contrast, Cactus aligns to the closest genome, which improves that figure further when investigating terminal branches. This was even impossible with the previous alignment, and enables completely different kind of analyses.
 
As seen with the finches, our analysis of recombination in the entire phylogeny reveals that hotspots are stable on an even larger scale. We expand the time frame from 20 to 100 million years of separation. With almost an order of magnitude longer time scale, this implies a very lasting force behind the location of hotspots. Despite varying evolutionary distance, we see no clear effect on estimates of evolutionary patterns. A power analysis reveals no large difference in the power to detect a bias either. GC* in hotspots is around 10% higher than in the flanks, which means a bias of strength x.
 
All species except for PICPU meet the basic requirements for gBGC, including increased WS substitution rate. PICPU does not show increased WS substitution rate, and do therefore not have evidence of hotspots in the same regions. Together with three additional species, (APTFO, CATAU, and STRCA), PICPU has increased SW substitution rate. These three species have simultaneously increased both substitution rates, and do therefore not display an increased GC*. However, we cannot rule out the existence of hotspots in these three species, as the presence of another force increasing SW substitution rate could be present simultaneously.
 
PICPU has the longest branch, which could indicate more problematic alignment. This means that the lack of observed bias could be an artefact of the dataset. It is also known that PICPU has peculiar GC content and many TEs that could affect recombination location. Therefore, it is also possible that recombination is actually not stable in PICPU, and instead is related to TEs. The recent completion of family level assemblies in the b10k should increase resolution along the branch and give insights in what has happened.
 
The lack of apparent structure in the placement of the four species with deviating substitution patterns in the phylogeny, indicates that whatever causes the increased SW bias has happened independently. Seemingly there are multiple events with the same outcome on substitution pattern, which suggests that it is a common force that could be explained and possibly well defined. Unlikely is that it is caused by any particular alignment issue, because of the seemingly random or unsystematic events.
 
APTFO is the branch best suited for further analyses of the deviating patterns, because it is short, and has a close relative on the same clade. We show that the change happened on that branch rather than the ancestral one, which still display the same pattern as the majority of the other terminal branches, including the closely related PYGAD. However, to really disentangle what is going on, recombination maps need to be inferred.
 
Alongside the GC-skewed substitutions that are the hallmark of recombination hotspots, we observe a clear bidirectional asymmetric composition skew around the hotspots. Decreasing to the left is a GT over AC bias, which is mirrored by an AC over GT bias decreasing to the right, with a sudden switch at the center of the hotspot. This bias is observed around CGIs as well. It is likely caused by replication with different mutational biases on the leading and lagging strand, which proceeds on different strands originating at the initiation location. Thus, it seems like recombination targets regions unmethylated due to transcriptional activity just like replication, and that these processes create and maintains CGIs with their mutational profiles.
This strong connection to replication has not before been explicitly described for recombination, and could shed some new light on primitive targets for hotspots. Recombination requires unmethylated regions. We suggest that ORIs are favorable as sites for recombination and thus the biases inherent for each of them will overlap in these particular regions. PRDM9 is one way of providing this in a targeted fashion, and ORIs provide an alternative way. If PRDM9 is missing, ORIs will be the sole remaining target. Even in the presence of PRDM9 this mechanism is likely a parallel source of recombination target sites.
 
On top of the biases caused by gBGC and replication, recombination itself has proven to be highly mutagenic. It also decreases to the flanks and displays evidence of bidirectional composition biases. It is therefore not unlikely that recombination in itself contributes to a substitution profile that is asymmetric around the hotspots. Considering the differences in bias in males and females, it is more likely that recombination causes the bias than replication, as replication should not differ between sexes in the same way as recombination does. [JB7]  Testing hypotheses around the relative contribution of these forces, independent identification of recombination hotspots, replication origins and CGIs should be carried out in different genomes for comparative analyses. Also, replication is universal, and exist in species without recombination. Identifying ORIs in these and comparing biases to those with hotspots would contribute valuable insights into the effects of each. [JB8] 
 
 
Figure legends
 
FigureX
Similar asymmetric strand biases around hotspots and CGIs.
a) Composition bias around hotspots.
b) Composition bias around CGIs.
 
Figure1
Bias across the phylogeny with illustrative examples.
a) Avian phylogeny as in Jarvis et al. 2014
b) Relative increase of GC* in 1kb hotspot centers (red) in relation to 40kb left and right flanks (pink) for all species, normalized by GC* in flanks. Span shows 95% confidence intervals, vertical lines the mean, and dotted lines the detection limit from the power analysis.
c) zebra finch GC and GC* around hotspots, high bias.
d) crow GC and GC* around hotspots, low bias.
e) chicken GC and GC* around hotspots, medium bias.
f) ostrich GC and GC* around hotspots, absent bias.
 
Figure2
Bias on the penguin clade.
a) GC and GC* around hotspots of penguin ancestor.
b) Representation of penguin phylogeny.
c) GC and GC* around hotspots of Adelie penguin (PYGAD).
d) GC and GC* around hotspots of Emperor penguin (APTFO).
 
Figure3
Signatures of hotspot usage. Zebra finch and species below or close to significance limit are colored, which show little correlation in hotspot usage with the other species, indicated by largely flat signatures.
 
Figure4
Scatterplot of covariance of hotspot strengths and estimated average nucleotide diversity between species. No discernible correlation between covariance and divergence can be observed, which indicates a rather conserved signature of hotspot strengths.
 
FigureS1
Alignment proportion for each species genome to zebra finch by MultiZ (top) and Cactus (bottom). MultiZ aligns 28% of a genome to any other, while Cactus aligns between 60-85% depending on phylogenetic distance.
 

 [KMT1]I think this is the central observation. It would be nice if we could think of some plausible explanation.
 [KMT2]I guess that would require that bias was strong enough before to have accumulated CpG sites faster than they disappeared by mutation. I don’t know how like that is?
 [KMT3]I think you should elaborate on what this tells us. That we know that it happens on a specific branch. That it is unlikely to be any kind of artefact since the two penguins should be treated the same way by the alignment. Maybe show in more detail how the elevated SW rate contribute this this case, and what those rates are.
 [KMT4]Can you argume somehow that this is not just because there is a very large variance on the way you estimate hotspot strengths? I guess you can say that the “high” covariance between HALLE and HALAL suggest that you can do have the power to see that covariance is high when species are closely related (refer to the covariance figure and report covarainces).
 [KMT5]Maybe that suggests that the hotspots moved somewhere else?
 [KMT6]Some of the colored signatures (like HALAL and APTFO) do not decline monotonically like the black ones. Looks like many hotspot strenghts changed in some coordinated fashion. Maybe due to chromosomal rearrangements?
 [JB7]In Arabidopsis a similar mutational skew is observed, but seems to be offset by 300bp to the left of ORIs. Is this similar to the offset for hotspot centers relative to the bias switch? “Differences in firing efficiency, chromatin and transcription underlie the developmental plasticity of the Arabidopsis DNA replication origin”
 [JB8]And how do these biases look in human or dog hotspots? It is known that recombination relocates toward unmethylated regions like CGIs, but never explicitly showed that there is a compositional bias apart from gBGC induced.





