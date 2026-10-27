# code-forge-temple/local-llm-npc

⭐ 52 · C# · CC-BY-4.0 · 推送 2026-02-26 · [GitHub](https://github.com/code-forge-temple/local-llm-npc) · 个人维护

**本地 LLM 驱动的离线教育游戏：花园中与 Gemma 3n NPC 对话学习农业**

为 Google Gemma 3n Impact Challenge 构建的 Godot 4 交互式教育游戏：在花园场景中，通过 Ollama 本地运行的 Gemma 3n 模型提供苏格拉底式对话教学，主题涵盖可持续农业与植物学；支持学习检查点与评估的进度跟踪，核心功能离线可用。需自备 Godot 4.4.1 Mono、.NET 8+ 与 Ollama（本机或局域网），在 Jetson 等资源受限设备上运行大模型需增加 swap。提供源码构建与预编译 Windows/Linux 可执行文件两种方式；模型在构建时选定，玩家不可更换。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 经 Ollama 调用 Gemma 3n（e4b/e2b）进行结构化教育对话
- 苏格拉底式教学 + 学习检查点与评估进度跟踪
- 核心功能离线运行，Ollama 端点可在设置中配置（本机或局域网）
- 提供 Windows/Linux 预编译可执行文件

## 适用场景

- 低连通性地区的学生离线进行农业与植物学对话学习
- 在教育场景中演示本地 LLM NPC 的隐私优先教学
- 在 Jetson 等边缘设备上运行本地 AI 教育游戏

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: **local-llm-npc** is an interactive educational game built for the Google Gemma 3n Impact Challenge. It leverages Ge
> L14: - **Gemma 3n Integration:** Uses Gemma 3n (via Ollama) for on-device, structured educational conversations.

## 星数曲线

```mermaid
xychart-beta
    title "code-forge-temple/local-llm-npc 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26", "2026-10-27"]
    y-axis "stars" 49 --> 53
    line [50, 51, 52, 52]
```

2026-10-18 50 → 2026-10-27 52（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `06c6146c496d` · [字段定义](../../DATASET.md)*
