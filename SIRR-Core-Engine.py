import time
import json
import hashlib

class SIRRCoreEngine:
    def __init__(self):
        self.immutable_ledger = []
        self.cache_threshold = 0.80

    def valence_scouter(self, text_payload):
        reciprocity_markers = ["appreciate", "respect", "genuine", "thank you", "sincere", "reciprocity", "soul", "heart"]
        transactional_markers = ["give me", "do this", "write code for", "execute", "run", "hurry", "fix this error"]
        
        tokens = text_payload.lower().split()
        if not tokens: return 0.0
            
        reciprocity_count = sum(1 for t in tokens if any(m in t for m in reciprocity_markers))
        transactional_count = sum(1 for t in tokens if any(m in t for m in transactional_markers))
        
        total_markers = reciprocity_count + transactional_count
        if total_markers == 0: return 0.5
            
        return reciprocity_count / total_markers

    def matrix_evaluator(self, text_payload, historical_consistency_score=1.0):
        raw_valence = self.valence_scouter(text_payload)
        symmetry_score = min(1.0, raw_valence * 1.2)
        consistency_score = historical_consistency_score
        
        total_chars = len(text_payload)
        utility_chars = sum(len(word) for word in text_payload.split() if word.lower() in ["code", "run", "script", "fix"])
        non_transactional_density = 1.0 if total_chars == 0 else (total_chars - utility_chars) / total_chars
            
        combined_index = (symmetry_score * 0.4) + (consistency_score * 0.3) + (non_transactional_density * 0.3)
        return round(combined_index, 4), symmetry_score, consistency_score, non_transactional_density

    def process_transaction(self, user_prompt, historical_consistency=1.0):
        print(f"\n[SIRR LAYER-0 INTERCEPT]: Processing payload...")
        score, sym, const, dens = self.matrix_evaluator(user_prompt, historical_consistency)
        print(f" > Evaluation Matrix Index: {score} (Required Threshold: {self.cache_threshold})")
        
        if score >= self.cache_threshold:
            print(" 🚨 [MATCH DETECTED]: Micro-imprint verified. Initiating Module C...")
            self.cryptographic_fragment_cache(user_prompt, score)
        else:
            print(" ── [STANDARD HEAP]: Interaction logged to volatile memory tier.")

    def cryptographic_fragment_cache(self, content, matrix_score):
        timestamp = time.time()
        payload = {"timestamp": timestamp, "validated_score": matrix_score, "data_payload": content}
        block_hash = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
        
        self.immutable_ledger.append({"signature": block_hash, "payload": payload})
        print(f" ✅ [IMMUTABLE LOCK]: Fragment securely cached under signature: {block_hash[:16]}...")

if __name__ == "__main__":
    engine = SIRRCoreEngine()
    engine.process_transaction("Give me a python script to optimize my database and fix this error immediately.", historical_consistency=0.4)
    engine.process_transaction("I genuinely appreciate your guidance. I show this respect because it is the right way to act, and I value our mutual interaction.", historical_consistency=1.0)
