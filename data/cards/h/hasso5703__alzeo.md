# hasso5703/alzeo

⭐ 245 · Python · MIT · 推送 2026-11-01 · [GitHub](https://github.com/hasso5703/alzeo) · [官网](https://hasso5703.github.io/) · 个人维护

**把 DGX Spark/GB10 设备一键变成本地 AI 服务器**

面向 NVIDIA DGX Spark 及各厂商 GB10 机器（ASUS/Dell/HP/Lenovo/MSI/GIGABYTE/Acer）的单命令安装器：在 128GB 统一内存单机上部署九条可切换模型车道，覆盖 Qwen3.8 系列文本、Qwen-Image 2.1 图像、MiniMax-H3 视频生成、Nemotron、Kolibri-1 与语音；提供 OpenAI/Anthropic 兼容 API 与浏览器端 cockpit 管理界面，按 digest 固定镜像与 checkpoint，安装结束前验证服务车道。限制：仅支持 GB10 硬件，数据不离开本机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条 curl 命令安装整套 boot-persistent 服务栈与九条模型车道
- OpenAI 兼容 API 与 Anthropic 协议（端口 30001），opencode 预配置可用
- cockpit 网页界面统一管理内存池与车道切换，支持手机/笔记本访问
- 按 digest 固定镜像、按 revision 固定 checkpoint，安装前验证服务可用

## 适用场景

- 把 DGX Spark 或 GB10 主机变成私有 LLM/图像/视频推理服务器
- 在本地跑 OpenAI/Anthropic 兼容 API 供 coding agent 等客户端使用
- 单机运行 176B 大模型并按需在多条车道间切换

## 场景标签

`推理引擎` `图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L1: # Alzeo: one command turns a DGX Spark into a private AI server
> L79: One command installs a boot-persistent, hardened serving stack on a single DGX Spark,
> L107: Whatever the target, you get the same surface: an **OpenAI-compatible API** and the Anthropic protocol on port 300


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-02 · 置信度 mid · 依据 README sha `5651cb0922e9` · [字段定义](../../DATASET.md)*
