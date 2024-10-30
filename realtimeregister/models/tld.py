from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from datetime import datetime

@dataclass
class TLD:
    name: str
    status: str
    launch_phase: str
    idn_scripts: List[str]
    min_period: int
    max_period: int
    grace_period: int
    transfer_period: int
    created_date: datetime
    updated_date: Optional[datetime]
    properties: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TLD':
        return cls(
            name=data['name'],
            status=data['status'],
            launch_phase=data['launchPhase'],
            idn_scripts=data['idnScripts'],
            min_period=data['minPeriod'],
            max_period=data['maxPeriod'],
            grace_period=data['gracePeriod'],
            transfer_period=data['transferPeriod'],
            created_date=datetime.fromisoformat(data['createdDate']),
            updated_date=datetime.fromisoformat(data['updatedDate']) if data.get('updatedDate') else None,
            properties=data.get('properties')
        )

    def to_dict(self) -> Dict[str, Any]:
        result = {
            'name': self.name,
            'status': self.status,
            'launchPhase': self.launch_phase,
            'idnScripts': self.idn_scripts,
            'minPeriod': self.min_period,
            'maxPeriod': self.max_period,
            'gracePeriod': self.grace_period,
            'transferPeriod': self.transfer_period,
            'createdDate': self.created_date.isoformat()
        }

        if self.updated_date:
            result['updatedDate'] = self.updated_date.isoformat()
        if self.properties:
            result['properties'] = self.properties

        return result