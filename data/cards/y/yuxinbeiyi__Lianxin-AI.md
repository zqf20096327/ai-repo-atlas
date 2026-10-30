# yuxinbeiyi/Lianxin-AI

⭐ 15 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/yuxinbeiyi/Lianxin-AI) · 个人维护 · 中文 README

**Windows 桌面 AI 陪伴助手：带持久记忆与情绪连续性**

面向个人用户的 Windows 桌面 AI 陪伴应用，提供 PyQt5 与 React+Tauri 2 两套界面，通过 LiteLLM 接入 DeepSeek、OpenAI 兼容端点或本地 Ollama。核心机制包括分层 Prism 记忆（分类事实、五元组知识图谱、语义检索）、五轴情绪状态模型、可热切换的人设系统、定时与冷却控制下的主动行为，以及本地视觉（VisionLab）、语音（FunASR/Edge-TTS/GPT-SoVITS）与 QQ/微信桥接；附带自习室、时间胶囊等本地功能，数据存于本地 SQLite。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Prism 记忆：分类事实、五元组知识图谱与语义检索（RAG）
- 五轴情绪状态模型与人设热切换，记忆不作为指令权威
- 主动行为（定时聊天、桌面观察、B 站浏览）带暂停与冷却控制
- 本地视觉 VisionLab（人脸/手势/姿态）与本地 FunASR 语音识别

## 适用场景

- 想要有长期记忆和情绪连续性的桌面 AI 陪伴角色
- 通过 QQ/微信与 AI 伙伴保持联系
- 借助 AI 陪伴进行专注学习与日常记录

## 场景标签

 · 领域:桌面 AI 陪伴应用

## 证据(README 行号)

> L15: > A Windows desktop AI companion with persistent memory, emotional state, editable personas, and proactive behavior
> L17: It ships two desktop interfaces: the original **PyQt5** window and a newer **React + TypeScript + Vite + Tauri 2** 
> L35: |Model providers|DeepSeek, Agnes AI, OpenAI-compatible endpoints, and local Ollama models|

## 星数曲线

```mermaid
xychart-beta
    title "yuxinbeiyi/Lianxin-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2686daefcd41` · [字段定义](../../DATASET.md)*
