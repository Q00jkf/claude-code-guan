# Claude 編輯修整工具使用指南

## 🎯 工具概述

Claude 編輯修整工具是一個專門用於修改和優化其他專案的 CLAUDE.md 文件的工具。它提供了完整的工作流程，包括備份、驗證、修改和優化功能。

## 🚀 快速開始

### 1. 基本工作流程

```bash
# 1. 創建備份
cp source_CLAUDE.md backup_CLAUDE_$(date +%Y%m%d_%H%M).md

# 2. 使用工具分析
python examples/basic_usage.py

# 3. 根據分析結果進行修改

# 4. 驗證修改結果
python -m src.validators.rule_validator
```

### 2. 核心功能

#### 文件處理 (FileHandler)
- ✅ **自動備份** - 創建帶時間戳的備份文件
- ✅ **安全讀寫** - 使用 UTF-8 編碼處理文件
- ✅ **元數據管理** - 提取和更新文件元數據
- ✅ **Markdown 驗證** - 基本的 Markdown 語法檢查

#### 規則驗證 (RuleValidator)
- ✅ **結構驗證** - 檢查必要的規則和章節
- ✅ **安全檢查** - 防止危險的規則修改
- ✅ **完整性評分** - 計算文件完整性分數
- ✅ **改進建議** - 提供優化建議

## 📋 使用場景

### 場景 1: 新專案 CLAUDE.md 創建
```python
from src.utils.file_handler import FileHandler
from src.validators.rule_validator import RuleValidator

# 使用基本模板
handler = FileHandler()
template = handler.read_file("src/templates/basic_template.md")

# 替換專案資訊
new_content = template.replace("[PROJECT_NAME]", "My Project")
new_content = new_content.replace("[DATE]", "2025-07-17")
new_content = new_content.replace("[PROJECT_DESCRIPTION]", "My awesome project")

# 保存新文件
handler.write_file("output/new_CLAUDE.md", new_content)
```

### 場景 2: 現有文件優化
```python
# 讀取現有文件
content = handler.read_file("existing_CLAUDE.md")

# 創建備份
backup_path = handler.create_backup("existing_CLAUDE.md")

# 驗證結構
validator = RuleValidator()
result = validator.validate_structure(content)

# 根據驗證結果進行修改
if not result['valid']:
    print("需要添加缺少的規則:")
    for rule in result['missing_rules']:
        print(f"- {rule}")
```

### 場景 3: 批量處理
```python
import os
from pathlib import Path

# 批量處理多個 CLAUDE.md 文件
claude_files = Path(".").glob("**/CLAUDE.md")

for file_path in claude_files:
    # 創建備份
    backup_path = handler.create_backup(str(file_path))
    
    # 讀取和驗證
    content = handler.read_file(str(file_path))
    result = validator.validate_structure(content)
    
    # 生成報告
    print(f"\n📄 {file_path}:")
    print(f"  - 結構驗證: {'✅' if result['valid'] else '❌'}")
    print(f"  - 備份位置: {backup_path}")
```

## 🔧 進階功能

### 自訂驗證規則
```python
class CustomRuleValidator(RuleValidator):
    def __init__(self):
        super().__init__()
        # 添加自訂規則
        self.required_rules.append("CUSTOM_RULE")
        self.required_prohibitions.append("NEVER do custom thing")
    
    def validate_custom_rules(self, content: str) -> Dict[str, Any]:
        # 自訂驗證邏輯
        pass
```

### 模板客製化
```python
# 創建專案特定模板
template_content = """
# CLAUDE.md - {project_name}

> **Project Type**: {project_type}
> **Tech Stack**: {tech_stack}

## 🚨 CRITICAL RULES - READ FIRST
{standard_rules}

## 🎯 PROJECT SPECIFIC RULES
{custom_rules}
"""

# 使用模板
custom_template = template_content.format(
    project_name="My AI Project",
    project_type="AI/ML",
    tech_stack="Python, TensorFlow, Docker",
    standard_rules=standard_rules,
    custom_rules=custom_rules
)
```

## 🔍 驗證規則詳解

### 必須包含的規則
1. **RULE ACKNOWLEDGMENT REQUIRED** - 規則確認系統
2. **ABSOLUTE PROHIBITIONS** - 絕對禁止項目
3. **MANDATORY REQUIREMENTS** - 必須遵守的要求
4. **PRE-TASK COMPLIANCE CHECK** - 預任務檢查清單

### 安全檢查項目
- ❌ 不允許放寬根目錄文件創建限制
- ❌ 不允許跳過備份程序
- ❌ 不允許忽略安全驗證
- ❌ 不允許禁用重要驗證

### 完整性評分
工具會根據以下項目計算完整性分數：
- 標題結構 (20%)
- 規則確認系統 (20%)
- 元數據完整性 (15%)
- 專案描述 (15%)
- 常用命令 (15%)
- 工作流程指南 (15%)

## 📈 最佳實踐

### 1. 修改前準備
```bash
# 總是創建備份
cp original_CLAUDE.md backup_CLAUDE_$(date +%Y%m%d_%H%M).md

# 理解原始結構
python -c "
from src.utils.file_handler import FileHandler
h = FileHandler()
content = h.read_file('original_CLAUDE.md')
metadata = h.extract_metadata(content)
print('原始元數據:', metadata)
"
```

### 2. 逐步修改
```python
# 分階段進行修改
stages = [
    "更新元數據",
    "添加缺少的規則",
    "優化現有內容",
    "驗證最終結果"
]

for stage in stages:
    print(f"🔄 執行階段: {stage}")
    # 執行對應修改
    # 驗證修改結果
    # 如有需要，回滾到上一個狀態
```

### 3. 驗證循環
```python
def validate_and_fix(content: str, max_iterations: int = 5) -> str:
    """迭代驗證和修復"""
    for i in range(max_iterations):
        result = validator.validate_structure(content)
        if result['valid']:
            break
        
        # 根據驗證結果修復
        content = fix_issues(content, result)
        print(f"🔄 修復迭代 {i+1}")
    
    return content
```

## 🚨 注意事項

1. **始終備份** - 修改任何文件前都要創建備份
2. **保持安全規則** - 不要移除或弱化安全相關規則
3. **維持一致性** - 確保修改後的格式和結構一致
4. **測試驗證** - 修改後務必運行完整驗證
5. **文檔更新** - 記錄所有重要修改

## 🔗 相關資源

- [CLAUDE.md 規則指南](../CLAUDE.md)
- [基本使用範例](../examples/basic_usage.py)
- [模板文件](../src/templates/)
- [驗證工具](../src/validators/)