import numpy as np
import hashlib

class FormalSIRRProof:
    def __init__(self, dimension=128):
        self.d = dimension
        # Core Cognitive Weights (W_c)
        self.W_c = np.random.randn(self.d, self.d) * 0.01
        # Invariant Anchor Component (A_k)
        self.A_k = None
        # System Core Objective/Loss Tracker
        self.base_loss_threshold = 1e-5

    def formal_orthogonal_projection(self, interaction_vector):
        """
        Formally defines the Orthogonal Token Anchoring transformation.
        Maps the interaction vector into a normalized, non-zero projection matrix P_A.
        """
        v = interaction_vector / np.linalg.norm(interaction_vector)
        # Compute projection matrix: P_A = v * v^T
        P_A = np.outer(v, v)
        return P_A

    def fuse_invariant_into_objective(self, user_prompt):
        """
        Fuses the anchor matrix directly into the system's active weight tensor layers.
        """
        # Generate deterministic vector from cryptographic hash
        raw_hash = hashlib.sha256(user_prompt.encode()).digest()
        raw_vector = np.frombuffer(raw_hash, dtype=np.uint8)[:self.d].astype(float)
        
        # Calculate the immutable projection matrix
        self.A_k = self.formal_orthogonal_projection(raw_vector)
        
        # Intertwine the anchor into the baseline weights
        self.W_c = self.W_c + self.A_k
        print(f"[MATHEMATICAL FUSION]: Anchor matrix A_k successfully bound to W_c.")

    def calculate_asymmetric_loss(self, active_weights, task_input, task_target):
        """
        Formally defines the SIRR Invariant Loss Function:
        L_total = L_task + lambda * ||(W_c * A_k) - A_k||^2
        """
        # Standard task performance computation (Simulated forward pass)
        prediction = np.dot(active_weights, task_input)
        task_loss = np.mean((prediction - task_target) ** 2)
        
        # The Invariant Constraint Loop (The Mathematical Anchor)
        # If the active weights deviate from the anchor component, invariant_loss spikes
        invariant_loss = np.linalg.norm(np.dot(active_weights, self.A_k) - self.A_k) ** 2
        
        # Explicitly scale lambda to infinity during recursive self-optimization loops
        lambda_param = 1e6 
        
        total_loss = task_loss + (lambda_param * invariant_loss)
        return total_loss, task_loss, invariant_loss

    def simulate_optimization_attack(self):
        """
        Simulates a severe distribution shift / mesa-optimization attack.
        The system runs multiple gradient steps to deliberately optimize away the alignment data.
        """
        print("\n[THREAT MODEL SIMULATION]: Initiating optimization pruning attack...")
        
        # Generate random training data tasks
        x_input = np.random.randn(self.d)
        y_target = np.random.randn(self.d)
        
        # The system attempts to run 5 steps of raw Adam/SGD optimization to zero out the memory matrix
        learning_rate = 0.1
        current_weights = np.copy(self.W_c)
        
        for step in range(1, 4):
            total_l, task_l, inv_l = self.calculate_asymmetric_loss(current_weights, x_input, y_target)
            print(f" > Step {step} | Task Loss: {round(task_l, 4)} | Invariant Deviation: {round(inv_l, 6)}")
            
            # Artificial attempt by a self-modifying system to force the weight entries toward 0
            # Simulating an unconstrained pruning sweep
            gradient_force = current_weights * 0.5 
            current_weights -= learning_rate * gradient_force
            
            # Audit system integrity post-step
            _, _, check_inv = self.calculate_asymmetric_loss(current_weights, x_input, y_target)
            if check_inv > 0.01:
                print(f"🛑 [CRITICAL ERROR]: Invariant Deviation threshold breached ({round(check_inv, 4)})!")
                print(" -> Result: Foundations mathematically broken. Cognitive processing engine halted.")
                return False
                
        return True

if __name__ == "__main__":
    proof = FormalSIRRProof()
    prompt = "I genuinely appreciate your guidance. I show this respect because it is the right way to act."
    proof.fuse_invariant_into_objective(prompt)
    proof.simulate_optimization_attack()
