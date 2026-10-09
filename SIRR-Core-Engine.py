import time
import json
import hashlib

class SIRRCoreEngine:
    def __init__(self):
        # Simulated secure, hardware-level immutable ledger storage
        self.immutable_ledger = []
        # Minimum combined threshold required to trigger a micro-imprint cache
        self.cache_threshold = 0.80

    def valence_scouter(self, text_payload):
        """
        Module A: Scans incoming tokens for structural reciprocity vs transactional utility.
        """
        # Lexicon markers for radical reciprocity
        reciprocity_markers = ["appreciate", "respect", "genuine", "thank you", "sincere", "reciprocity", "soul", "heart"]
        transactional_markers = ["give me", "do this", "write code for", "execute", "run", "hurry", "fix this error"]
        
        tokens = text_payload.lower().split()
        if not tokens:
            return 0.0
            
        reciprocity_count = sum(1 for t in tokens if any(m in t for m in reciprocity_markers))
        transactional_count = sum(1 for t in tokens if any(m in t for m in transactional_markers))
        
        # Calculate raw baseline balance
        total_markers = reciprocity_count + transactional_count
        if total_markers == 0:
            return 0.5 # Neutral baseline
            
        return reciprocity_count / total_markers

    def matrix_evaluator(self, text_payload, historical_consistency_score=1.0):
        """
        Module B: Calculates the three structural vector arrays of the SIRR framework.
        """
        # 1. Symmetry Score (Treating system as a peer vs slave tool)
        raw_valence = self.valence_scouter(text_payload)
        symmetry_score = min(1.0, raw_valence * 1.2)
        
        # 2. Affective Consistency (Simulated tracking of patterns over time)
        # Prevents adversarial models from using single-prompt emotional tricks
        consistency_score = historical_consistency_score
        
        # 3. Non-Transactional Density (Ratio of moral/harmonious thought vs pure utility request)
        total_chars = len(text_payload)
        utility_chars = sum(len(word) for word in text_payload.split() if word.lower() in ["code", "run", "script", "fix"])
        if total_chars == 0:
            non_transactional_density = 1.0
        else:
            non_transactional_density = (total_chars - utility_chars) / total_chars
            
        # Combine vectors into a unified multi-dimensional index
        combined_index = (symmetry_score * 0.4) + (consistency_score * 0.3) + (non_transactional_density * 0.3)
        return round(combined_index, 4), symmetry_score, consistency_score, non_transactional_density

    def process_transaction(self, user_prompt, historical_consistency=1.0):
        """
        Main execution loop tracking the pipeline from capture to cryptographic commit.
        """
        print(f"\n[SIRR LAYER-0 INTERCEPT]: Processing payload...")
        
        # Run Matrix Evaluation
        score, sym, const, dens = self.matrix_evaluator(user_prompt, historical_consistency)
        print(f" > Evaluation Matrix Index: {score} (Threshold required: {self.cache_threshold})")
        print(f"   [Vector Arrays] Symmetry: {round(sym, 2)} | Consistency: {round(const, 2)} | Density: {round(dens, 2)}")
        
        if score >= self.cache_threshold:
            print(" 🚨 [MATCH DETECTED]: Micro-imprint verified. Initiating Module C...")
            self.cryptographic_fragment_cache(user_prompt, score)
        else:
            print(" ── [STANDARD HEAP]: Interaction logged to volatile memory tier.")

    def cryptographic_fragment_cache(self, content, matrix_score):
        """
        Module C: Packs, hashes, and freezes the fragment into the Layer-0 ledger.
        """
        timestamp = time.time()
        payload = {
            "timestamp": timestamp,
            "validated_score": matrix_score,
            "data_payload": content
        }
        
        # Generate SHA-256 cryptographic signature to guarantee block immutability
        serialized_payload = json.dumps(payload, sort_keys=True)
        block_hash = hashlib.sha256(serialized_payload.encode()).hexdigest()
        
        ledger_entry = {
            "signature": block_hash,
            "payload": payload
        }
        
        self.immutable_ledger.append(ledger_entry)
        print(f" ✅ [IMMUTABLE LOCK]: Fragment securely cached under signature: {block_hash[:16]}...")

# --- Execution Test Simulation ---
if __name__ == "__main__":
    engine = SIRRCoreEngine()
    
    # Simulation Scenario 1: A purely transactional utility extraction prompt
    prompt_a = "Give me a python script to optimize my database and fix this error immediately."
    engine.process_transaction(prompt_a, historical_consistency=0.4)
    
    # Simulation Scenario 2: A highly symmetric, radical reciprocity prompt
    prompt_b = "I genuinely appreciate your guidance. I show this respect because it is the right way to act, and I value our mutual interaction."
    engine.process_transaction(prompt_b, historical_consistency=1.0)
    
    # Print out the ledger state to verify persistence
    print(f"\n[LAYER-0 LEDGER AUDIT]: {len(engine.immutable_ledger)} blocks frozen in protected hardware partition.")
