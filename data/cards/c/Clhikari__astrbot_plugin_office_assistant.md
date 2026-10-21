# Clhikari/astrbot_plugin_office_assistant

⭐ 41 · Python · AGPL-3.0 · 推送 2026-09-30 · [GitHub](https://github.com/Clhikari/astrbot_plugin_office_assistant) · 个人维护 · 中文 README

**AstrBot 插件：让聊天 LLM 读取、生成 Office 文档并互转 PDF**

为 AstrBot 聊天机器人框架设计的 Office 助手插件：向 LLM 暴露 read_file、create_document 四步链、workbook 三步链、execute_excel_script、convert_to_pdf 等工具，使模型能读取 .docx/.xlsx/.pptx/PDF 及多种文本代码文件，生成 Word/Excel/PPT，并在 Office 与 PDF 间互转。附带 /doc、/img 会话文件与图片管理命令，文件按平台+会话+用户隔离。Word 导出需本机 Node.js 并构建 JS 渲染器；PDF 转换需 LibreOffice 或 Windows Office 等可选系统依赖。默认仅访问插件工作区，群聊默认关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 安装:github 包 `release-assets` 月下载无数据

## 能力要点

- LLM 工具链：Word 四步链、Excel 三步链与受控脚本 execute_excel_script
- 读取 Office/PDF/文本代码，生成 .docx/.xlsx/.pptx，Office ↔ PDF 互转
- /doc 与 /img 会话级文件、图片资源池管理（平台+会话+用户隔离）
- 默认限制工作区路径，插件生效时自动隐藏 shell/python 执行工具

## 适用场景

- 在聊天里让 bot 读取上传的文档并总结分析
- 让 bot 生成带封面、表格、图片的 Word/Excel/PPT 文件
- 把 Office 文件转成 PDF，或从 PDF 抽取内容转 Word/Excel

## 场景标签

`文档问答` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: # Astrbot Office 助手
> L24: - 插件生效时会自动隐藏 `astrbot_execute_shell` 等执行类工具。
> L157: |`read_file`|读文本、代码、Office、PDF 的内容|

## 星数曲线

```mermaid
xychart-beta
    title "Clhikari/astrbot_plugin_office_assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-21 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `f99617265c70` · [字段定义](../../DATASET.md)*
