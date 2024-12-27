def to_rna(dna_strand):
    result = ""
    for nuc in dna_strand:
        match (nuc): 
            case 'G':
                result += 'C'
            case 'C':
                result += 'G'
            case 'T':
                result += 'A'
            case 'A':
                result += 'U'
            case default:
                result += ''
    return result
