#!/usr/bin/env python3
"""
CLAUDE.md 規則驗證器
檢查 CLAUDE.md 文件是否包含必要的規則和結構
"""

import re
from typing import List, Dict, Any, Optional

class RuleValidator:
    """CLAUDE.md 規則驗證器"""
    
    def __init__(self):
        # 必須包含的關鍵規則
        self.required_rules = [
            "RULE ACKNOWLEDGMENT REQUIRED",
            "ABSOLUTE PROHIBITIONS",
            "MANDATORY REQUIREMENTS",
            "PRE-TASK COMPLIANCE CHECK"
        ]
        
        # 必須包含的禁止項目
        self.required_prohibitions = [
            "NEVER create new files in root directory",
            "NEVER use git commands with -i flag",
            "NEVER create duplicate files",
            "NEVER create multiple implementations"
        ]
        
        # 必須包含的要求項目
        self.required_requirements = [
            "COMMIT after every completed task",
            "GITHUB BACKUP",
            "USE TASK AGENTS",
            "TODOWRITE for complex tasks",
            "READ FILES FIRST"
        ]
    
    def validate_structure(self, content: str) -> Dict[str, Any]:
        """
        驗證 CLAUDE.md 文件結構
        
        Args:
            content: 文件內容
            
        Returns:
            驗證結果
        """
        results = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'missing_rules': [],
            'missing_prohibitions': [],
            'missing_requirements': []
        }
        
        # 檢查必要規則
        for rule in self.required_rules:
            if rule not in content:
                results['missing_rules'].append(rule)
                results['valid'] = False
        
        # 檢查禁止項目
        for prohibition in self.required_prohibitions:
            if prohibition not in content:
                results['missing_prohibitions'].append(prohibition)
                results['valid'] = False
        
        # 檢查要求項目
        for requirement in self.required_requirements:
            if requirement not in content:
                results['missing_requirements'].append(requirement)
                results['valid'] = False
        
        # 檢查標題結構
        if not self._check_title_structure(content):
            results['errors'].append("缺少必要的標題結構")
            results['valid'] = False
        
        # 檢查規則確認系統
        if not self._check_acknowledgment_system(content):
            results['errors'].append("缺少規則確認系統")
            results['valid'] = False
        
        return results
    
    def _check_title_structure(self, content: str) -> bool:
        """檢查標題結構"""
        required_titles = [
            "CRITICAL RULES - READ FIRST",
            "RULE ACKNOWLEDGMENT REQUIRED",
            "ABSOLUTE PROHIBITIONS",
            "MANDATORY REQUIREMENTS"
        ]
        
        for title in required_titles:
            if title not in content:
                return False
        
        return True
    
    def _check_acknowledgment_system(self, content: str) -> bool:
        """檢查規則確認系統"""
        acknowledgment_text = "✅ CRITICAL RULES ACKNOWLEDGED"
        return acknowledgment_text in content
    
    def validate_safety_rules(self, content: str) -> Dict[str, Any]:
        """
        驗證安全規則
        
        Args:
            content: 文件內容
            
        Returns:
            驗證結果
        """
        results = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        # 檢查是否有危險的規則放寬
        dangerous_patterns = [
            r'(?i)allow.*root.*files',
            r'(?i)skip.*backup',
            r'(?i)ignore.*safety',
            r'(?i)disable.*validation'
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, content):
                results['errors'].append(f"發現可能危險的規則: {pattern}")
                results['valid'] = False
        
        return results
    
    def suggest_improvements(self, content: str) -> List[str]:
        """
        建議改進項目
        
        Args:
            content: 文件內容
            
        Returns:
            改進建議列表
        """
        suggestions = []
        
        # 檢查是否有版本控制資訊
        if "Documentation Version" not in content:
            suggestions.append("建議添加文檔版本資訊")
        
        # 檢查是否有最後更新時間
        if "Last Updated" not in content:
            suggestions.append("建議添加最後更新時間")
        
        # 檢查是否有專案描述
        if "Project" not in content and "Description" not in content:
            suggestions.append("建議添加專案描述")
        
        # 檢查是否有常用命令
        if "COMMON COMMANDS" not in content:
            suggestions.append("建議添加常用命令章節")
        
        # 檢查是否有工作流程指南
        if "WORKFLOW" not in content:
            suggestions.append("建議添加工作流程指南")
        
        return suggestions
    
    def check_completeness(self, content: str) -> Dict[str, Any]:
        """
        檢查文件完整性
        
        Args:
            content: 文件內容
            
        Returns:
            完整性檢查結果
        """
        results = {
            'completeness_score': 0,
            'total_checks': 0,
            'passed_checks': 0,
            'details': []
        }
        
        checks = [
            ("標題結構", self._check_title_structure(content)),
            ("規則確認系統", self._check_acknowledgment_system(content)),
            ("元數據", "Documentation Version" in content),
            ("專案描述", "Project" in content or "Description" in content),
            ("常用命令", "COMMON COMMANDS" in content),
            ("工作流程", "WORKFLOW" in content)
        ]
        
        for check_name, passed in checks:
            results['total_checks'] += 1
            if passed:
                results['passed_checks'] += 1
                results['details'].append(f"✅ {check_name}: 通過")
            else:
                results['details'].append(f"❌ {check_name}: 缺少")
        
        if results['total_checks'] > 0:
            results['completeness_score'] = (results['passed_checks'] / results['total_checks']) * 100
        
        return results