#!/usr/bin/env python3
"""
Claude 編輯修整工具使用範例
示範如何使用工具的基本功能
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils.file_handler import FileHandler
from validators.rule_validator import RuleValidator

def main():
    """主函數 - 示範基本使用方法"""
    
    # 初始化工具
    file_handler = FileHandler()
    validator = RuleValidator()
    
    print("🚀 Claude 編輯修整工具使用範例")
    print("=" * 50)
    
    # 假設我們有一個 CLAUDE.md 文件需要處理
    sample_file = "sample_CLAUDE.md"
    
    # 1. 讀取文件
    print("\n📖 步驟 1: 讀取文件")
    try:
        if os.path.exists(sample_file):
            content = file_handler.read_file(sample_file)
            print(f"✅ 成功讀取文件: {sample_file}")
        else:
            print(f"⚠️ 文件不存在: {sample_file}")
            # 使用模板創建示例內容
            content = """# CLAUDE.md - 示例專案

> **Documentation Version**: 1.0  
> **Last Updated**: 2025-07-17  
> **Project**: 示例專案  
> **Description**: 這是一個示例專案

## 🚨 CRITICAL RULES - READ FIRST

### 🔄 **RULE ACKNOWLEDGMENT REQUIRED**
> **Before starting ANY task, Claude Code must respond with:**  
> "✅ CRITICAL RULES ACKNOWLEDGED - I will follow all prohibitions and requirements listed in CLAUDE.md"

### ❌ ABSOLUTE PROHIBITIONS
- **NEVER** create new files in root directory → use proper module structure
- **NEVER** use git commands with -i flag (interactive mode not supported)
- **NEVER** create duplicate files (manager_v2.py, enhanced_xyz.py, utils_new.js) → ALWAYS extend existing files
- **NEVER** create multiple implementations of same concept → single source of truth

### 📝 MANDATORY REQUIREMENTS
- **COMMIT** after every completed task/phase - no exceptions
- **GITHUB BACKUP** - Push to GitHub after every commit to maintain backup: `git push origin main`
- **USE TASK AGENTS** for all long-running operations (>30 seconds) - Bash commands stop when context switches
- **TODOWRITE** for complex tasks (3+ steps) → parallel agents → git checkpoints → test validation
- **READ FILES FIRST** before editing - Edit/Write tools will fail if you didn't read the file first

### 🔍 MANDATORY PRE-TASK COMPLIANCE CHECK
> **STOP: Before starting any task, Claude Code must explicitly verify ALL points:**

**Step 1: Rule Acknowledgment**
- [ ] ✅ I acknowledge all critical rules in CLAUDE.md and will follow them

## 🎯 PROJECT OVERVIEW

這是一個示例專案，用於演示 Claude 編輯修整工具的功能。

## 🚀 COMMON COMMANDS

```bash
# 示例命令
echo "Hello World"
```

## 📋 WORKFLOW GUIDELINES

1. 遵循所有規則
2. 使用適當的工具
3. 每個任務完成後提交
"""
            print("📝 使用模板創建示例內容")
    
    except Exception as e:
        print(f"❌ 讀取文件失敗: {e}")
        return
    
    # 2. 創建備份
    print("\n💾 步驟 2: 創建備份")
    try:
        # 先寫入示例文件
        file_handler.write_file(sample_file, content)
        backup_path = file_handler.create_backup(sample_file)
        print(f"✅ 備份創建成功: {backup_path}")
    except Exception as e:
        print(f"❌ 備份創建失敗: {e}")
        return
    
    # 3. 提取元數據
    print("\n🔍 步驟 3: 提取元數據")
    metadata = file_handler.extract_metadata(content)
    print("📊 元數據:")
    for key, value in metadata.items():
        print(f"  - {key}: {value}")
    
    # 4. 驗證結構
    print("\n✅ 步驟 4: 驗證結構")
    validation_result = validator.validate_structure(content)
    print(f"結構驗證: {'✅ 通過' if validation_result['valid'] else '❌ 失敗'}")
    
    if validation_result['errors']:
        print("❌ 錯誤:")
        for error in validation_result['errors']:
            print(f"  - {error}")
    
    if validation_result['missing_rules']:
        print("⚠️ 缺少規則:")
        for rule in validation_result['missing_rules']:
            print(f"  - {rule}")
    
    # 5. 安全檢查
    print("\n🔒 步驟 5: 安全檢查")
    safety_result = validator.validate_safety_rules(content)
    print(f"安全檢查: {'✅ 通過' if safety_result['valid'] else '❌ 失敗'}")
    
    if safety_result['errors']:
        print("❌ 安全問題:")
        for error in safety_result['errors']:
            print(f"  - {error}")
    
    # 6. 完整性檢查
    print("\n📈 步驟 6: 完整性檢查")
    completeness = validator.check_completeness(content)
    print(f"完整性評分: {completeness['completeness_score']:.1f}%")
    print("詳細結果:")
    for detail in completeness['details']:
        print(f"  {detail}")
    
    # 7. 改進建議
    print("\n💡 步驟 7: 改進建議")
    suggestions = validator.suggest_improvements(content)
    if suggestions:
        print("建議:")
        for suggestion in suggestions:
            print(f"  - {suggestion}")
    else:
        print("✅ 沒有改進建議，文件結構良好")
    
    # 8. 驗證 Markdown 語法
    print("\n📝 步驟 8: Markdown 語法驗證")
    markdown_result = file_handler.validate_markdown(content)
    print(f"Markdown 語法: {'✅ 通過' if markdown_result['valid'] else '❌ 失敗'}")
    
    if markdown_result['errors']:
        print("❌ 語法錯誤:")
        for error in markdown_result['errors']:
            print(f"  - {error}")
    
    if markdown_result['warnings']:
        print("⚠️ 警告:")
        for warning in markdown_result['warnings']:
            print(f"  - {warning}")
    
    # 9. 更新元數據並保存
    print("\n💾 步驟 9: 更新元數據並保存")
    try:
        new_metadata = {
            'version': '1.1',
            'last_updated': '2025-07-17',
            'project': '示例專案 (已更新)',
            'description': '這是一個更新後的示例專案'
        }
        
        updated_content = file_handler.update_metadata(content, new_metadata)
        output_file = "output/updated_CLAUDE.md"
        file_handler.write_file(output_file, updated_content)
        print(f"✅ 更新文件保存至: {output_file}")
        
    except Exception as e:
        print(f"❌ 更新失敗: {e}")
    
    print("\n🎉 範例執行完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()