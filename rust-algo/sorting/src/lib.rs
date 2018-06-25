pub mod selection {

    pub fn sort<T: PartialOrd>(v: &mut [T]) {
        
        for i in 0..v.len() {
            let j = get_min(i, v);
            v.swap(j, i);
        }
    }

    fn get_min<T: PartialOrd>(i: usize, v: &[T]) -> usize {

        let mut min_index = i;
        let mut current_min = &v[i];

        for j in i..v.len() {    

            if v[j] < *current_min { 
                current_min = &v[j];
                min_index = j; 
            }
        }
        min_index
    }
}

pub mod insertion {

    pub fn sort<T: PartialOrd>(v: &mut [T]) {

        for i in 0..v.len() {
            for j in (1..=i).rev() {
                if v[j] >= v[j - 1] { break; }               
                v.swap(j, j - 1);
            } 
        }
    }
}
