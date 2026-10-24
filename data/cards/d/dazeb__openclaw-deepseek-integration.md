# dazeb/openclaw-deepseek-integration

⭐ 95 · Shell · MIT · 推送 2026-02-05 · [GitHub](https://github.com/dazeb/openclaw-deepseek-integration) · 个人维护

**OpenClaw 的 DeepSeek API 接入配置与插件集成**

为 OpenClaw 增加 DeepSeek API Platform 支持的集成项目：通过 openclaw.json 配置或环境变量设置 API key，接入 DeepSeek Chat（V3.2，非思考模式，128K 上下文）与 DeepSeek Reasoner（思考模式，128K 上下文，最大输出 65,536）。基于 DeepSeek 的 OpenAI 兼容 API，提供按 token 的成本跟踪、可选的 auth profile 持久化存储脚本，以及实验性的 npm 插件安装方式。使用需自备 DeepSeek API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接入 DeepSeek Chat 与 Reasoner (V3.2)，均支持 128K 上下文
- 支持 openclaw.json 手动配置、环境变量与 auth profile 三种接入方式
- 按 token 计价的成本跟踪（含缓存读写）
- 附带实验性 OpenClaw 插件（npm 构建）

## 适用场景

- 让 OpenClaw agent 使用 DeepSeek 模型执行任务
- 为 OpenClaw 配置思考模式的 DeepSeek Reasoner
- 持久化存储 DeepSeek API key 免去每次设置环境变量

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: # DeepSeek API Platform Integration for OpenClaw
> L8: This integration adds DeepSeek API Platform support to OpenClaw, allowing you to use DeepSeek's state-of-the-art lan

## 星数曲线

```mermaid
xychart-beta
    title "dazeb/openclaw-deepseek-integration 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-24 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `d5cb01f10a2e` · [字段定义](../../DATASET.md)*
