# jdaln/dgx-spark-inference-stack

⭐ 52 · JavaScript · AGPL-3.0 · 推送 2026-10-11 · [GitHub](https://github.com/jdaln/dgx-spark-inference-stack) · 个人维护 · 中文 README

**单台 DGX Spark 上的 LLM 推理服务栈：OpenAI 兼容 API 按需启停模型**

面向单台 NVIDIA DGX Spark（GB10）的自托管推理栈：nginx 网关接收请求，校验 API key 后由 waker 服务按需启动对应的 vLLM 模型容器，模型独占 GPU、闲置 20 分钟后停止，另可常驻一个小型工具模型。GPU 被占用时返回 HTTP 429 并附释放信息。通过 docker compose 部署，需本地构建模型镜像、预先下载权重（每个 2-80GB），支持 Qwen、Gemma、GPT-OSS 等 10 个模型。限单机，双节点未测试，属爱好项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 请求驱动的模型启停：首次请求启动模型，闲置 20 分钟后停止
- nginx 网关 + 校验器 + waker 架构，GPU 被占时返回 HTTP 429 附释放信息
- 10 个模型基于 vLLM 运行，含常驻工具模型与多语言/图像模型
- 模型容器无网络访问，含 seccomp 与容器加固文档

## 适用场景

- 在家用 DGX Spark 上自托管 OpenAI 兼容的 LLM API
- 按需启停模型以在单卡上轮流服务多个模型
- 与 ComfyUI 共享 GPU 的本地推理环境

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L6: Serves LLMs from one NVIDIA DGX Spark over an OpenAI-compatible API. A model starts on the
> L14: An nginx gateway on port `8009` takes every request. A request validator checks the API
> L61: docker build -t vllm-node-mxfp4 -f custom-docker-containers/vllm-node-mxfp4/Dockerfile .

## 星数曲线

```mermaid
xychart-beta
    title "jdaln/dgx-spark-inference-stack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-29 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f99643ef2440` · [字段定义](../../DATASET.md)*
