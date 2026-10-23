# PurpleDoubleD/locally-uncensored

⭐ 2,473 · TypeScript · AGPL-3.0 · 推送 2026-10-22 · [GitHub](https://github.com/PurpleDoubleD/locally-uncensored) · [官网](https://locallyuncensored.com) · 个人维护

**桌面端一体化本地 AI 工作室：聊天、图像视频生成与编程 Agent**

面向桌面用户的本地 AI 应用（Windows/Linux，macOS Beta）：以安装包形式分发，首次启动向导自动安装 AI 引擎与 ComfyUI，模型管理器标记适配硬件的模型并一键下载，可复用已装 Ollama/LM Studio 的模型。功能含聊天（文档索引、记忆、导入 ChatGPT/Claude/Gemini 导出）、ComfyUI 驱动的图像/视频/音乐生成、带 diff 预览的编程 Agent、带权限门控的通用 Agent，以及 Beta 的语音对话和电脑控制。可选 LU Labs Cloud 在托管 GPU 上运行大模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 首次启动向导一键安装 AI 引擎与 ComfyUI，无 Docker/终端/配置文件
- 模型管理器标记适配硬件的模型，可链接 Ollama/LM Studio 已存模型
- 编程 Agent 展示 diff 后再应用，支持 .lurules 项目规则与 OpenAI 兼容本地 API
- 图像/视频生成本地跑在自管 ComfyUI 上，含角色训练与 LoRA 管理

## 适用场景

- 在桌面一站式使用本地聊天、画图、视频和编程 Agent
- 复用已装的 Ollama/LM Studio 模型统一调用
- 从手机经局域网或 Cloudflare 隧道访问本地应用

## 场景标签

`编码 Agent` `图像生成` `视频生成` `聊天机器人` · 领域:编码与开发

## 证据(README 行号)

> L5: **The all-in-one local AI studio for your desktop. Chat, images, video and a coding agent in one app. Install it, pi
> L64: 1. **Install.** Run the installer like any other program. On first launch a wizard looks for an AI engine that is a
> L66: 3. **Create.** Chat, Create, Code and Agent are tabs in one window. Type in one, switch to the next, keep the same 

## 星数曲线

```mermaid
xychart-beta
    title "PurpleDoubleD/locally-uncensored 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-23"]
    y-axis "stars" 2327 --> 2486
    line [2340, 2406, 2447, 2473]
```

2026-10-18 2,340 → 2026-10-23 2,473（+133）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `10c75d893e94` · [字段定义](../../DATASET.md)*
