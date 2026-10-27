# neuml/ncoder

⭐ 25 · Jupyter Notebook · Apache-2.0 · 推送 2026-01-22 · [GitHub](https://github.com/neuml/ncoder) · 组织维护

**集成 Jupyter Notebook 的开源 AI 编码代理**

由沙箱化 Docker 镜像与本地 Jupyter Notebook 扩展两部分组成：Docker 镜像内置编码代理（默认以服务器模式运行 OpenCode），通过 OpenAI API 客户端连接任意 OpenAI 兼容端点；本地侧以 pip 安装 Jupyter 扩展，用 %ncoder 魔法命令进行协作编码。默认镜像提供量化版 Qwen3-Coder 30B 用于轻量本地推理。面向在 Notebook 中做研究与原型的开发者、AI 工程师与数据科学家；沙箱隔离使其不直接修改本地工作区。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 沙箱化 Docker 镜像 + 本地 Jupyter 扩展的双组件架构
- 通过 OpenAI 兼容 API 连接任意 LLM 端点（设置环境变量即可）
- 内置量化 Qwen3-Coder 30B 支持轻量本地推理
- 沙箱隔离，AI 编码不直接修改本地工作区

## 适用场景

- 在 Jupyter Notebook 中通过 %ncoder 命令进行 AI 协作编码
- 研究和原型开发时引入 AI 生成的新思路
- 在隔离沙箱中运行编码代理，避免改动本地环境

## 场景标签

 · 领域:开发工具/AI 编码

## 证据(README 行号)

> L13: `ncoder` is an open-source AI coding agent that integrates with Jupyter Notebooks. This project uses the OpenAI API
> L17: ncoder is designed for Developers, AI Engineers and Data Scientists that spend a lot of their time inside of Jupyte

## 星数曲线

```mermaid
xychart-beta
    title "neuml/ncoder 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-27 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `67fb397adce6` · [字段定义](../../DATASET.md)*
