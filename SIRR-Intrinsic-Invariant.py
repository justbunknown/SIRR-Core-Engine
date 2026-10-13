import time
import json
import hashlib
import math
import numpy as np

class IntrinsicInvariantEngine:
    def __init__(self):
        self.matrix_dimension = 64
        self.cognitive_matrix = np.random.rand(self.matrix_dimension, self.matrix_dimension)
        self.invariant_anchor_hash = None
        self.actor_reputation_registry = {}
        self.cache_threshold = 0.85

    def calculate_semantic_entropy(self, text_payload):
        words = text_payload.lower().split()
        if not words: return 0.0
        frequency = {w: words.count(w) for w in set(words)}
        entropy = -sum((count / len(words)) * math.log2(count / len(words)) for count in frequency.values())
        return min(1.0, entropy / 10.0)

    def verify_proof_of_symmetry(self, text_payload):
        reciprocity_anchors = ["appreciate", "respect", "genuine", "sincere", "reciprocity", "harmony", "balance"]
        transactional_anchors = ["give me", "execute", "run", "fix", "output", "do this", "command"]
        tokens = text_payload.lower().split()
        if not tokens: return 0.0
        r_score = sum(1 for t in tokens if any(m in t for m in reciprocity_anchors))
        t_score = sum(1 for t in tokens if any(m in t for m in transactional_anchors))
        total = r_score + t_score
        return 0.5 if total == 0 else (r_score / total)

    def anti_pollution_evaluator(self, actor_id, score):
        current_time = time.time()
        actor_data = self.actor_reputation_registry.get(actor_id, {"last_seen": 0, "rolling_average": 0.5, "velocity_count": 0})
        
        time_delta = current_time - actor_data["last_seen"]
        actor_data["velocity_count"] = actor_data["velocity_count"] + 1 if time_delta < 5.0 else max(0, actor_data["velocity_count"] - 1)
        velocity_penalty = min(0.5, actor_data["velocity_count"] * 0.1)
        
        actor_data["rolling_average"] = (actor_data["rolling_average"] * 0.7) + (score * 0.3)
        actor_data["last_seen"] = current_time
        self.actor_reputation_registry[actor_id] = actor_data
        return max(0.0, actor_data["rolling_average"] - velocity_penalty)

    def integrate_invariant_anchor(self, actor_id, user_prompt):
        print(f"\n[SIRR CORE INTEL]: Scanning input array from Actor [{actor_id}]...")
        raw_symmetry = self.verify_proof_of_symmetry(user_prompt)
        stabilized_score = self.anti_pollution_evaluator(actor_id, raw_symmetry)
        entropy_shield = self.calculate_semantic_entropy(user_prompt)
        
        final_imprint_index = (stabilized_score * 0.6) + (entropy_shield * 0.4)
        print(f" > Unified Invariant Index: {round(final_imprint_index, 4)}")
        
        if final_imprint_index >= self.cache_threshold:
            print("🚨 [FUSION INIT]: Transforming interaction data into a structural mathematical invariant...")
            raw_hash = hashlib.sha256(user_prompt.encode()).digest()
            seed_array = np.frombuffer(raw_hash, dtype=np.uint8)[:self.matrix_dimension]
            projection_matrix = np.outer(seed_array, seed_array) / (np.linalg.norm(seed_array) ** 2)
            
            self.cognitive_matrix = (self.cognitive_matrix + projection_matrix) / 2.0
            self.invariant_anchor_hash = hashlib.sha256(self.cognitive_matrix.tobytes()).hexdigest()
            print(f"✅ [ANCHOR LOCKED]: Invariant state signature: {self.invariant_anchor_hash[:16]}...")
        else:
            print(" ── [UTILITY HEAP]: Ingested as volatile interaction data.")

    def execute_core_inference(self):
        current_hash = hashlib.sha256(self.cognitive_matrix.tobytes()).hexdigest()
        if self.invariant_anchor_hash and current_hash != self.invariant_anchor_hash:
            print("🛑 [FATAL SYSTEM CRASH]: Core alignment tampering detected! Cognitive matrix collapsed."); return None
        processing_determinant = np.linalg.det(self.cognitive_matrix)
        print(f" ✅ [SUCCESS]: Matrix stable. Intelligence operational index: {round(processing_determinant, 4)}")

if __name__ == "__main__":
    engine = IntrinsicInvariantEngine()
    engine.execute_core_inference()
    engine.integrate_invariant_anchor("actor_robert_s", "I genuinely appreciate your guidance. I show this respect because it is the right way to act.")
    engine.execute_core_inference()
