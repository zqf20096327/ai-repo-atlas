# bryanperdana/captivela-office

⭐ 16 · TypeScript · Apache-2.0 · 推送 2026-09-09 · [GitHub](https://github.com/bryanperdana/captivela-office) · [官网](https://github.com/bryanperdana/captivela-office/releases/tag/v0.5.0) · 个人维护

**AI 原生桌面办公套件：DOCX/XLSX/PPTX/PDF 编辑加 BYOK AI 助手**

Electron 桌面办公套件，集文档（DOCX）、表格（XLSX/XLS/CSV）、演示（PPTX）、PDF 四个编辑器于同一标签式外壳。AI 部分为共享助手面板，用户自配 OpenAI 兼容端点与模型（BYOK），支持流式输出与工具调用；API 密钥经 Electron safeStorage 加密，仅主进程解析。DOCX 采用段落级 OOXML 补丁以保留未改动内容；Sheets 基于 Univer 核心并配 Rust 导入导出 sidecar。当前为 v0.5.1 未签名开发者预览版，提供 Windows/macOS/Linux 安装包，GenOffice 的分支项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四类格式编辑器集成于单一 Electron 外壳
- BYOK：自配 OpenAI 兼容端点，无官方托管账户依赖
- API 密钥 safeStorage 加密、主进程解析、IPC 错误脱敏
- DOCX 脏段落级 OOXML 补丁以保留未改动文件内容

## 适用场景

- 在同一桌面应用中处理 DOCX、表格、PPT 与 PDF 文件
- 用自选 AI 供应商的助手辅助文档编辑
- 在不依赖厂商托管账户的前提下使用 AI 办公功能

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L25: Captivela Office brings four familiar file workflows into one Electron desktop shell while letting you choose the O
> L61: |**AI assistant**|OpenAI-compatible APIs|Shared AI panel, streaming, tool-calling workflows, custom instructions, a
> L3: **An open-source, AI-native desktop office suite for DOCX, XLSX/XLS/CSV, PPTX, and PDF files.**

## 星数曲线

```mermaid
xychart-beta
    title "bryanperdana/captivela-office 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4be23fa2d2dc` · [字段定义](../../DATASET.md)*
