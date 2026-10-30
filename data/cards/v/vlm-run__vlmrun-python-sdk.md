# vlm-run/vlmrun-python-sdk

⭐ 15 · Python · Apache-2.0 · 推送 2026-09-25 · [GitHub](https://github.com/vlm-run/vlmrun-python-sdk) · [官网](https://docs.vlm.run/sdk-reference/getting-started) · 组织维护

**VLM Run 平台的官方 Python SDK 与 CLI，接入其视觉语言模型 API**

面向 VLM Run REST API 平台的官方 Python SDK，提供 pip 安装包与 CLI（vlmrun）。功能包括：基础图像调用、OpenAI 兼容的 chat completions（含异步）、System One 类型化决策路由（对文本/JSON/图像/PDF/视频按命名问题输出带置信度的答案，支持视频逐帧读取、HTTP 与 websocket 两种传输、并发与计费控制）、本地 SKILL.md 技能目录内联发送及服务端技能上传。需 API key，URL 可通过环境变量指向其他部署。给开发者用，依赖 VLM Run 云端服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- System One 类型化决策：命名问题+校准概率，视频逐帧独立读取
- OpenAI 兼容 chat completions 端点（同步与异步）
- CLI 支持 SKILL.md 本地技能目录内联发送与服务端技能上传
- websocket 会话传输（单 socket 流水线、max_inflight 协商）

## 适用场景

- 在 Python 应用中调用 VLM Run 的视觉语言模型处理图像与文档
- 对视频逐帧做类型化决策（如门是否开着）并构建时间线
- 通过 CLI 会话加载领域技能与 VLM Run 模型对话
- 在 Claude Code 中以插件形式安装 VLM Run CLI 技能

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L13: The VLM Run Python SDK is the official Python SDK for VLM Run API platform, providing a convenient way to interact 
> L210: ### OpenAI-Compatible Chat Completions
> L232: The `vlmrun chat` command supports **skills** — local directories containing a `SKILL.md` and optional assets that

## 星数曲线

```mermaid
xychart-beta
    title "vlm-run/vlmrun-python-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b788f1c42e05` · [字段定义](../../DATASET.md)*
