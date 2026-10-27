# DeVenLucaz/llamdrop

⭐ 12 · Python · NOASSERTION · 推送 2026-06-19 · [GitHub](https://github.com/DeVenLucaz/llamdrop) · [官网](https://devenlucaz.github.io/DevLuz/llamdrop/) · 个人维护

**让低端 Android/Linux 设备一键运行本地 LLM 的工具**

面向低端或预算硬件用户的本地 AI 运行工具：自动读取设备 CPU/RAM/GPU/平台，按 5 档分级（Micro 到 High）选择后端（Termux pkg/Vulkan/CPU），从验证模型目录或 HuggingFace 下载匹配 RAM 的 GGUF 量化版本并运行。提供聊天界面（上下文裁剪、会话保存、文件上下文、导出）、RAM/电池监控、Doctor 自修复与自更新。支持 Android(Termux)/Linux/树莓派等 ARM64 设备；v0.10.0 起放弃 macOS/Windows，不支持 iOS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 安装:github 包 `release-assets` 月下载无数据

## 能力要点

- 硬件自动检测与 5 档分级，自动选择后端与量化（Q4/Q2/Q5/IQ）
- 验证模型目录按 RAM 分层（<1GB 到 12-24GB，含 SmolLM2/Qwen3/DeepSeek R1 等）
- HuggingFace 实时搜索与 GGUF 全盘扫描、断点续传与 SHA-256 校验
- Doctor 自修复、引擎独立更新、自更新与多语言 TUI

## 适用场景

- 在旧安卓手机（Termux）上无 PC 运行本地 LLM 聊天
- 树莓派/单板机/旧笔记本上按硬件规格自动选模型
- 低预算、无订阅场景下离线体验开源模型

## 场景标签

`推理引擎` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L13: llamdrop is a **free, open-source** tool that lets anyone run a local AI model on whatever device they own — an And
> L73: - 🤖 **Ollama backend** — auto-detected on Linux/desktop, hardware-aware auto-tuning
> L74: - 💬 **Stable chat** — automatic context trimming prevents out-of-memory crashes. First exchange always preserved.

## 星数曲线

```mermaid
xychart-beta
    title "DeVenLucaz/llamdrop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 11 --> 13
    line [12, 12]
```

2026-10-18 12 → 2026-10-27 12（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `0c8f458451dd` · [字段定义](../../DATASET.md)*
