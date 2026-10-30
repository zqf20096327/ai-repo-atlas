# Verenu/Verenu

⭐ 18 · Rust · MIT · 推送 2026-10-29 · [GitHub](https://github.com/Verenu/Verenu) · [官网](https://verenu.com) · 组织维护

**跨平台开源 AI 听写桌面应用：按住热键说话即得整理文本**

基于 Tauri/Svelte/Rust/SQLite 构建的 Windows/macOS/Linux 桌面听写应用：按住全局热键录音，本地或云端转录后经所选模型清理语气、标点与格式，最终文本回填到原焦点应用。支持按应用/网站配置上下文（语气、清理规则、词汇表、片段），API 密钥存于系统凭据管理器，历史记录保存在本地 SQLite。可选本地 Parakeet V3 转录与本地 LLM 清理实现完全离线，亦可接入 Groq/OpenAI/Google/AssemblyAI/OpenRouter/xAI 等 BYOK 云端方案。自称是 Wispr Flow 的免费开源替代。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按住热键听写，清理后的文本注入任意焦点应用
- 本地 Parakeet V3 转录 + 本地 LLM 清理可实现完全离线
- 按应用/网站分组配置语气、清理规则、词汇表与片段
- API 密钥存系统凭据管理器，历史与设置仅存本地 SQLite

## 适用场景

- 在任意应用中用语音输入并自动整理成规范文本
- 按不同应用/网站使用不同的语气与格式规则听写
- 全程本地模型离线听写，音频文本不出设备

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3:  Free, open-source AI dictation for Windows, macOS, and Linux. Hold a hotkey, talk, release, and cleaned-up text is 
> L21: - Provider choice for transcription and cleanup, including fully local Parakeet V3 transcription and local LLM clea
> L71: 3. If cleanup is enabled, it sends the resulting raw text to your chosen cleanup model so filler words, punctuation

## 星数曲线

```mermaid
xychart-beta
    title "Verenu/Verenu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `fb1ad903d38e` · [字段定义](../../DATASET.md)*
