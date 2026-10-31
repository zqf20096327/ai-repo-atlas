# Olcmyk/Meowth-GBA-Translator

⭐ 47 · Python · MIT · 推送 2026-03-25 · [GitHub](https://github.com/Olcmyk/Meowth-GBA-Translator) · 个人维护 · 中文 README

**用 LLM 全自动翻译宝可梦 GBA ROM 的工具**

面向 ROM 爱好者的 GBA 宝可梦 ROM 翻译工具，将文本提取、LLM 批量翻译、ROM 回写构建整合为一键流水线，提供 GUI 与 CLI 双界面。支持 11 家 LLM 提供商（DeepSeek/OpenAI/Gemini/Claude 等），覆盖英/中/法/德/意/西六种目标语言，中文翻译会自动注入字库补丁。已在 Pokémon Gaia 等 3 个改版上测试，其他改版可能需调整；中文仅支持二进制补丁 ROM。分发方式含 macOS/Windows 安装包与 pip 包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Extract → Translate → Build 单命令流水线
- 11 家 LLM 提供商可选，含自定义 API 端点
- 中文翻译自动注入字库补丁
- GUI 与 CLI 双界面，macOS/Windows/Linux 跨平台

## 适用场景

- 把英文宝可梦 GBA 改版 ROM 翻译成中文或其他语言
- 批量翻译多个 ROM 文件
- 不熟悉命令行的用户用 GUI 完成整个翻译流程

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L9: An intelligent GBA Pokémon ROM translator powered by LLM with both GUI and CLI interfaces
> L18: - **AI Translation**: Support for 11+ LLM providers (OpenAI, DeepSeek, Google Gemini, etc.)
> L321: ### Phase 2: Translation (meowth translate)

## 星数曲线

```mermaid
xychart-beta
    title "Olcmyk/Meowth-GBA-Translator 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26", "2026-10-29", "2026-10-31"]
    y-axis "stars" 43 --> 48
    line [44, 45, 46, 47, 47]
```

2026-10-18 44 → 2026-10-31 47（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `be801aafaf7b` · [字段定义](../../DATASET.md)*
