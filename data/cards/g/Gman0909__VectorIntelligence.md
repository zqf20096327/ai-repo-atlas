# Gman0909/VectorIntelligence

⭐ 16 · Python · MIT · 推送 2026-06-11 · [GitHub](https://github.com/Gman0909/VectorIntelligence) · 个人维护

**给 Vector 机器人用户：本地自托管 AI 大脑，识人记事全离线**

为 Anki/Digital Dream Labs Vector 机器人提供自托管的完整 AI 技术栈：多用户人脸识别与按人记忆（SQLite）、对话摘要、视觉场景描述、持久情绪与自主行为，全部运行在本地。架构为单一 supervisor 进程管理 Wire-Pod（chipper，机器人侧服务器）、vector-ai 服务（Python）、Ollama 运行 gemma3:12b 与 llama3.2:3b、GPU Whisper 语音识别。需约 8GB VRAM 与 18GB 磁盘，支持 Windows 10/11 与 Debian 系 Linux（x64/ARM64），通过安装脚本构建 Wire-Pod 与 Whisper。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多用户人脸识别与按人分离的持久记忆档案
- 本地 Ollama 运行 gemma3:12b 多模态模型，Whisper GPU 语音识别，无云端
- 单一 supervisor 进程自愈管理全栈（断链、休眠、IP 变化）
- 人格由单个可编辑 persona.txt 文件定义，改动可在重装后保留

## 适用场景

- 让家里每个成员被 Vector 叫出名字并各自保留记忆
- 离线运行不外传数据的桌面机器人 AI 伴侣
- 通过修改 persona.txt 自定义机器人性格

## 场景标签

`人脸识别` `语音识别` `多模态` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: Turn an Anki / Digital Dream Labs **Vector** robot into a genuinely smart
> L121: - **Ollama** running **`gemma3:12b`** — the local, multimodal language model
> L124: - **Whisper** — GPU-accelerated speech-to-text.

## 星数曲线

```mermaid
xychart-beta
    title "Gman0909/VectorIntelligence 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ffac00234249` · [字段定义](../../DATASET.md)*
