# ADT109119/llamacpp-distributed-inference

⭐ 95 · JavaScript · Apache-2.0 · 推送 2026-08-23 · [GitHub](https://github.com/ADT109119/llamacpp-distributed-inference) · 个人维护 · 中文 README

**基于 llama.cpp 的局域网分布式 LLM 推理桌面应用**

基于 Electron 的跨平台桌面应用，通过本机 llama.cpp API 服务器与远程 RPC 节点在局域网内多台电脑间协同执行 GGUF 模型推理。提供 mDNS 自动节点发现与手动添加、GGUF 模型扫描与 GPU 层数（-ngl）调整、并行请求数设置、多标签实时日志，并暴露 OpenAI 兼容 API（localhost:8080）。面向单机显存不足但想运行较大模型的个人用户。RPC 通信未加密且无身份验证，README 明确要求仅在可信内网使用，且声明不适用于生产环境、商业与公共服务；生产部署建议改用 vLLM 等方案。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本机 API 服务器 + 远程 RPC 节点的分布式推理（端口 8080/50052）
- mDNS 自动节点发现（每30秒）与手动添加节点
- GGUF 模型管理，支持 GPU 层数（-ngl）与并行请求数（-np）调整
- 提供 OpenAI 兼容 API 与可选 API Key

## 适用场景

- 单机显存不够时，用家里多台电脑合起来跑大模型
- 在家庭内网做 LLM 实验和学习分布式推理
- 快速搭建概念验证或原型开发环境

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L9: - ⚡ **高效分佈式推理**: 本機API伺服器 + 遠程RPC節點協同計算
> L348: - **推理引擎**: llama.cpp
> L369: ### 🎯 **適用場景**

## 星数曲线

```mermaid
xychart-beta
    title "ADT109119/llamacpp-distributed-inference 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-30 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e2d354e2f8a9` · [字段定义](../../DATASET.md)*
