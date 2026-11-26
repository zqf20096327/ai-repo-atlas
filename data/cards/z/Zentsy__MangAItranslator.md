# Zentsy/MangAItranslator

⭐ 11 · TypeScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/Zentsy/MangAItranslator) · [官网](https://zentsy.github.io/MangAItranslator/) · 个人维护

**面向扫描汉化组的漫画 AI 辅助翻译桌面应用**

基于 Tauri 的 Windows 桌面应用，工作流为导入章节、生成 AI 翻译草稿、逐块人工审校、导出 .txt/.docx。提供批量翻译队列、项目级术语表（SQLite 存储并注入提示词）、跨页短期记忆、日文 Raw→PT-BR 专用预设与 PT-BR 流畅度二次润色。支持 Gemini、Groq、OpenRouter 免费通道及 LM Studio/Ollama 本地模型，API 密钥经系统 keyring 加密保存。无安装包平台仅限 Windows x64，未签名安装器触发 SmartScreen 提示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多引擎接入：Gemini、Groq、OpenRouter 与 LM Studio/Ollama 本地模型
- 批量翻译队列与实时进度监视
- 项目术语表持久化到 SQLite 并注入提示词
- API 密钥经操作系统 keyring 加密隔离

## 适用场景

- 日文漫画 Raw 扫描稿翻译为 PT-BR 并逐块审校
- 翻译团队维护统一的专有名词与招式术语表
- 批量处理整章页面并导出 .txt/.docx 成稿

## 场景标签

 · 领域:内容本地化/桌面工具

## 证据(README 行号)

> L5: Desktop app para localização assistida de mangá e quadrinhos. Conheça a demonstração visual e recursos no Website Of
> L23: O MangAI Translator ajuda você a importar um capítulo, gerar um rascunho com IA, revisar bloco por bloco e exportar
> L59: - **Multi-Provedores de IA**: suporte nativo a Google Gemini, OpenRouter (Auto-Free inteligente), Groq Cloud e mode

## 星数曲线

```mermaid
xychart-beta
    title "Zentsy/MangAItranslator 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-25", "2026-11-26"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-11-08 10 → 2026-11-26 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `48a1cf7774de` · [字段定义](../../DATASET.md)*
