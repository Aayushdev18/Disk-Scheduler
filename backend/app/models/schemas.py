from pydantic import BaseModel, Field
from typing import List, Optional


class SimulationRequest(BaseModel):
    """Request model for disk scheduling simulation"""
    requests: List[int] = Field(..., description="List of disk track requests")
    initial_position: int = Field(..., ge=0, description="Initial head position")
    algorithm: str = Field(..., description="Algorithm name: FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK")
    disk_size: int = Field(default=200, ge=1, description="Total disk size (number of tracks)")
    direction: Optional[str] = Field(default="right", description="Initial direction for SCAN/C-SCAN/LOOK/C-LOOK")


class AlgorithmResult(BaseModel):
    """Result for a single algorithm execution"""
    algorithm: str
    sequence: List[int] = Field(..., description="Order of track accesses")
    total_seek_time: int = Field(..., description="Total seek time (distance traveled)")
    average_seek_time: float = Field(..., description="Average seek time")
    seek_operations: List[tuple] = Field(..., description="List of (from, to) seek operations")


class SimulationResponse(BaseModel):
    """Response model containing simulation results"""
    request: SimulationRequest
    result: AlgorithmResult
    performance_metrics: dict = Field(..., description="Additional performance metrics")
