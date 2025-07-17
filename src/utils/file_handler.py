#!/usr/bin/env python3
"""
CLAUDE.md 文件處理工具
負責文件的讀取、寫入、備份和驗證
"""

import os
import datetime
import shutil
from pathlib import Path
from typing import Optional, Dict, Any

class FileHandler:
    """處理 CLAUDE.md 文件的核心類別"""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def create_backup(self, file_path: str) -> str:
        """
        創建文件備份
        
        Args:
            file_path: 原始文件路徑
            
        Returns:
            備份文件路徑
        """
        source_path = Path(file_path)
        if not source_path.exists():
            raise FileNotFoundError(f"源文件不存在: {file_path}")
        
        # 生成帶時間戳的備份文件名
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        backup_name = f"backup_{source_path.stem}_{timestamp}{source_path.suffix}"
        backup_path = self.output_dir / backup_name
        
        # 複製文件
        shutil.copy2(source_path, backup_path)
        
        return str(backup_path)
    
    def read_file(self, file_path: str) -> str:
        """
        讀取文件內容
        
        Args:
            file_path: 文件路徑
            
        Returns:
            文件內容
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            raise Exception(f"讀取文件失敗: {e}")
    
    def write_file(self, file_path: str, content: str) -> None:
        """
        寫入文件內容
        
        Args:
            file_path: 文件路徑
            content: 文件內容
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            raise Exception(f"寫入文件失敗: {e}")
    
    def validate_markdown(self, content: str) -> Dict[str, Any]:
        """
        驗證 Markdown 語法
        
        Args:
            content: Markdown 內容
            
        Returns:
            驗證結果
        """
        results = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        lines = content.split('\n')
        
        # 基本驗證
        for i, line in enumerate(lines, 1):
            # 檢查標題格式
            if line.startswith('#'):
                if not line.startswith('# ') and line != '#':
                    results['errors'].append(f"Line {i}: 標題後應有空格")
                    results['valid'] = False
            
            # 檢查代碼塊
            if line.startswith('```'):
                if len(line) > 3 and not line[3:].strip().isalnum():
                    results['warnings'].append(f"Line {i}: 代碼塊語言標識符可能不正確")
        
        return results
    
    def extract_metadata(self, content: str) -> Dict[str, str]:
        """
        提取 CLAUDE.md 文件的元數據
        
        Args:
            content: 文件內容
            
        Returns:
            元數據字典
        """
        metadata = {}
        lines = content.split('\n')
        
        for line in lines:
            if '**Documentation Version**:' in line:
                metadata['version'] = line.split(':', 1)[1].strip()
            elif '**Last Updated**:' in line:
                metadata['last_updated'] = line.split(':', 1)[1].strip()
            elif '**Project**:' in line:
                metadata['project'] = line.split(':', 1)[1].strip()
            elif '**Description**:' in line:
                metadata['description'] = line.split(':', 1)[1].strip()
        
        return metadata
    
    def update_metadata(self, content: str, metadata: Dict[str, str]) -> str:
        """
        更新 CLAUDE.md 文件的元數據
        
        Args:
            content: 原始內容
            metadata: 新的元數據
            
        Returns:
            更新後的內容
        """
        lines = content.split('\n')
        updated_lines = []
        
        for line in lines:
            if '**Documentation Version**:' in line and 'version' in metadata:
                updated_lines.append(f"> **Documentation Version**: {metadata['version']}")
            elif '**Last Updated**:' in line and 'last_updated' in metadata:
                updated_lines.append(f"> **Last Updated**: {metadata['last_updated']}")
            elif '**Project**:' in line and 'project' in metadata:
                updated_lines.append(f"> **Project**: {metadata['project']}")
            elif '**Description**:' in line and 'description' in metadata:
                updated_lines.append(f"> **Description**: {metadata['description']}")
            else:
                updated_lines.append(line)
        
        return '\n'.join(updated_lines)