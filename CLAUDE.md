# CLAUDE.md - Claude 編輯修整工具

> **Documentation Version**: 1.0  
> **Last Updated**: 2025-07-17  
> **Project**: Claude 編輯修整工具  
> **Description**: 專門用於修改和優化其他專案的 CLAUDE.md 文件的工具

## 🚨 CRITICAL RULES - READ FIRST

### 🔄 **RULE ACKNOWLEDGMENT REQUIRED**
> **Before starting ANY task, Claude Code must respond with:**  
> "✅ CRITICAL RULES ACKNOWLEDGED - I will follow all prohibitions and requirements listed in CLAUDE.md"

### ❌ ABSOLUTE PROHIBITIONS
- **NEVER** modify original CLAUDE.md files without creating backup
- **NEVER** ignore existing project structure and conventions
- **NEVER** remove critical safety rules from source files
- **NEVER** create inconsistent markdown formatting
- **NEVER** delete important project-specific information
- **NEVER** modify file permissions or sensitive configurations

### 📝 MANDATORY REQUIREMENTS
- **BACKUP** original CLAUDE.md files before modification
- **VALIDATE** markdown syntax and formatting
- **PRESERVE** project-specific critical rules and context
- **MAINTAIN** consistent formatting and structure
- **DOCUMENT** all changes made to source files
- **FOLLOW** markdown best practices and conventions

## 🎯 PROJECT OVERVIEW

此工具用於：
- 接收其他專案的 CLAUDE.md 文件
- 根據用戶需求進行內容修改和優化
- 確保符合用戶的工作流程和環境需求
- 維持文件的結構完整性和可讀性

## 🏗️ PROJECT STRUCTURE

```
claude-md-editor/
├── src/
│   ├── templates/          # 模板文件
│   ├── utils/             # 工具函數
│   └── validators/        # 驗證器
├── docs/                  # 文檔說明
├── examples/              # 範例文件
├── tests/                 # 測試文件
└── CLAUDE.md             # 此文件
```

## 🚀 COMMON COMMANDS

```bash
# 創建備份
cp source_CLAUDE.md backup_CLAUDE_$(date +%Y%m%d_%H%M).md

# 驗證 markdown 語法
markdownlint CLAUDE.md

# 檢查文件差異
diff -u original_CLAUDE.md modified_CLAUDE.md

# 格式化 markdown
prettier --write CLAUDE.md
```

## 📋 WORKFLOW GUIDELINES

### 處理流程
1. **備份原文件** - 建立時間戳記備份
2. **分析結構** - 理解現有內容和規則
3. **需求確認** - 明確修改目標和範圍
4. **逐步修改** - 保持結構完整性
5. **驗證測試** - 確保語法和邏輯正確
6. **交付說明** - 記錄所有變更

### 修改類型
- **結構優化** - 重新組織章節和層級
- **內容更新** - 修改規則、命令、說明
- **格式統一** - 標準化 markdown 語法
- **環境適配** - 調整為符合特定工作環境
- **規則強化** - 增加或修改安全規則

## 🔧 EDITING STANDARDS

### Markdown 格式要求
- 使用標準 CommonMark 語法
- 保持一致的標題層級
- 使用適當的代碼塊語法高亮
- 確保清單和表格格式正確

### 內容處理原則
- 保留原有的關鍵安全規則
- 維持專案特定的重要資訊
- 確保修改後的邏輯性和可讀性
- 適應用戶的工作流程需求

## 🎯 RULE COMPLIANCE CHECK

Before starting ANY task, verify:
- [ ] ✅ I acknowledge all critical rules above
- [ ] Original file has been backed up
- [ ] Modification requirements are clear
- [ ] Markdown validation tools are available
- [ ] Project context is understood