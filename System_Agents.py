

import psutil
import time
from datetime import datetime


class SystemMonitorAgent:
    """
    An AI agent that autonomously monitors system resources and provides alerts.
    
    This agent demonstrates how AI agents can be used for system operations,
    providing continuous monitoring with configurable thresholds and automated
    alerting capabilities.
    
    Attributes:
        cpu_threshold (float): CPU usage percentage that triggers alerts
        check_interval (int): Time interval between monitoring checks
        is_monitoring (bool): Flag to control monitoring state
    """
    
    def __init__(self, cpu_threshold=75, check_interval=10):
        """
        Initialize the system monitoring agent with configurable parameters.
        
        Args:
            cpu_threshold (float): CPU usage percentage to trigger alerts (default: 75%)
            check_interval (int): Time interval between checks in seconds (default: 10)
        """
        self.cpu_threshold = cpu_threshold
        self.check_interval = check_interval
        self.is_monitoring = False
        
        print(f"SystemMonitorAgent initialized:")
        print(f"  - CPU Threshold: {cpu_threshold}%")
        print(f"  - Check Interval: {check_interval} seconds")

    def monitor_cpu(self):
        """
        Continuously monitor CPU usage and provide alerts when thresholds are exceeded.
        
        This method implements the core monitoring loop, demonstrating autonomous
        operation by continuously checking system metrics without human intervention.
        """
        self.is_monitoring = True
        print(f"Starting CPU monitoring (threshold: {self.cpu_threshold}%)...")
        print("Press Ctrl+C to stop monitoring")
        
        try:
            while self.is_monitoring:
                # Get current CPU usage over a 1-second interval
                cpu_usage = psutil.cpu_percent(interval=1)
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Evaluate CPU usage against threshold
                if cpu_usage > self.cpu_threshold:
                    self.alert_high_cpu(cpu_usage, current_time)
                else:
                    print(f"[{current_time}] CPU usage normal: {cpu_usage:.1f}%")
                
                # Wait for the specified interval before next check
                time.sleep(self.check_interval)
                
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user")
            self.is_monitoring = False
        except Exception as e:
            print(f"Error during monitoring: {e}")
            self.is_monitoring = False

    def alert_high_cpu(self, cpu_usage, timestamp):
        """
        Handle high CPU usage alerts with detailed information.
        
        This method demonstrates how AI agents can take action based on
        environmental conditions, providing immediate feedback and potential
        corrective actions.
        
        Args:
            cpu_usage (float): Current CPU usage percentage
            timestamp (str): Timestamp of the alert
        """
        print(f"\n{'='*60}")
        print(f"ALERT: High CPU Usage Detected!")
        print(f"Time: {timestamp}")
        print(f"CPU Usage: {cpu_usage:.1f}% (Threshold: {self.cpu_threshold}%)")
        print(f"Excess: {cpu_usage - self.cpu_threshold:.1f}% above threshold")
        print(f"{'='*60}\n")
        
        # Additional actions could be implemented here:
        # - Send email notifications
        # - Log to file
        # - Trigger automated responses
        # - Escalate to higher-level monitoring systems

    def monitor_memory(self):
        """
        Monitor and display current memory usage statistics.
        
        This method provides additional system monitoring capabilities,
        demonstrating how agents can monitor multiple system metrics.
        """
        memory = psutil.virtual_memory()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"[{current_time}] Memory Status:")
        print(f"  - Total: {memory.total / (1024**3):.1f} GB")
        print(f"  - Available: {memory.available / (1024**3):.1f} GB")
        print(f"  - Used: {memory.percent:.1f}%")
        print(f"  - Free: {memory.free / (1024**3):.1f} GB")

    def get_system_info(self):
        """
        Retrieve comprehensive system information for monitoring context.
        
        Returns:
            dict: System information including CPU, memory, and disk usage
        """
        cpu_count = psutil.cpu_count()
        cpu_freq = psutil.cpu_freq()
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        return {
            'cpu_count': cpu_count,
            'cpu_frequency': cpu_freq.current if cpu_freq else 'N/A',
            'memory_total': memory.total,
            'memory_available': memory.available,
            'disk_total': disk.total,
            'disk_free': disk.free
        }

    def stop_monitoring(self):
        """
        Stop the monitoring process gracefully.
        
        This method allows for controlled shutdown of the monitoring agent,
        demonstrating proper resource management in autonomous systems.
        """
        self.is_monitoring = False
        print("Monitoring agent stopped")

    def monitor_system(self):
        """
        Comprehensive system monitoring including both CPU and memory.
        
        This method demonstrates how agents can monitor multiple system aspects
        simultaneously, providing a complete view of system health.
        """
        print("Starting comprehensive system monitoring...")
        
        # Display initial system information
        system_info = self.get_system_info()
        print(f"System Information:")
        print(f"  - CPU Cores: {system_info['cpu_count']}")
        print(f"  - CPU Frequency: {system_info['cpu_frequency']} MHz")
        print(f"  - Total Memory: {system_info['memory_total'] / (1024**3):.1f} GB")
        print(f"  - Total Disk: {system_info['disk_total'] / (1024**3):.1f} GB")
        
        # Start monitoring
        self.monitor_cpu()


def main():
    """
    Main execution function that creates and runs the system monitoring agent.
    
    This function demonstrates the complete lifecycle of an autonomous monitoring
    agent, from initialization to continuous operation.
    """
    print("System Monitoring AI Agent")
    print("=" * 40)
    
    # Create the monitoring agent with custom thresholds
    # Note: Using a low threshold (5%) for demonstration purposes
    agent = SystemMonitorAgent(cpu_threshold=10, check_interval=10)
    
    # Start monitoring
    agent.monitor_system()


if __name__ == "__main__":
    main()