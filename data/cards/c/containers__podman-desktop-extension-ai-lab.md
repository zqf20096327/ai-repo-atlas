# containers/podman-desktop-extension-ai-lab

⭐ 302 · TypeScript · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/containers/podman-desktop-extension-ai-lab) · [官网](https://podman-desktop.io/extensions/ai-lab) · 组织维护

**Podman Desktop 扩展：在本地容器中运行 LLM 并提供示例应用目录**

面向 Podman Desktop 用户的开源扩展，用于在本地环境运行 LLM：提供精选开源模型目录（支持 GGUF、Pytorch、Tensorflow 格式），下载后可在容器中启动推理服务并以通用 chat API 暴露端点；内置 Playground 供对话实验与参数调优；附带 Recipes Catalog，覆盖聊天机器人、代码生成、文本摘要等用例的示例应用（以容器组合运行）。要求 Podman Desktop 1.8.0+ 与 Podman 4.9.0+，兼容 Windows/macOS/Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 精选开源模型目录，支持 GGUF/Pytorch/Tensorflow 格式
- 容器内推理服务并通过通用 chat API 暴露端点
- 内置 Playground 用于模型实验与参数调优
- Recipes Catalog 提供聊天机器人/代码生成/文本摘要等示例应用

## 适用场景

- 在本机容器里下载并运行 LLM 推理服务
- 通过 Playground 对比和调参多个模型
- 按示例目录快速搭建聊天机器人或文本摘要应用

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Podman AI Lab is an open source extension for Podman Desktop to work with LLMs (Large Language Models) on a local en
> L11: Podman AI Lab uses Podman machines to run inference servers for LLM models and AI applications.
> L22: Once a model is downloaded, a model service can be started. A model service is an inference server that is running 

## 星数曲线

```mermaid
xychart-beta
    title "containers/podman-desktop-extension-ai-lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 300 --> 303
    line [301, 302]
```

2026-10-18 301 → 2026-10-25 302（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a85b81439026` · [字段定义](../../DATASET.md)*
