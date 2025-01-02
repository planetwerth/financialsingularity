use std::time::{SystemTime, UNIX_EPOCH};

pub struct Block {
    index: u32,
    previous_hash: String,
    timestamp: u64,
    data: String,
    hash: String,
}

impl Block {
    pub fn new(index: u32, previous_hash: String, data: String) -> Block {
        let timestamp = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();
        let hash = Block::calculate_hash(&index, &previous_hash, &timestamp, &data);
        Block {
            index,
            previous_hash,
            timestamp,
            data,
            hash,
        }
    }

    pub fn calculate_hash(index: &u32, previous_hash: &str, timestamp: &u64, data: &str) -> String {
        let combined = format!("{}{}{}{}", index, previous_hash, timestamp, data);
        format!("{:x}", md5::compute(combined))
    }
}
