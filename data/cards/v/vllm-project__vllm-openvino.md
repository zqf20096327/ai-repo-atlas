# vllm-project/vllm-openvino

⭐ 61 · Python · Apache-2.0 · 推送 2026-09-14 · [GitHub](https://github.com/vllm-project/vllm-openvino) · 组织维护

**为 vLLM 提供 OpenVINO 后端的推理插件，支持 Intel CPU/GPU**

vLLM 的 OpenVINO 后端插件，在支持 AVX2 的 x86-64 CPU 以及 Intel 集成/独立 GPU 上运行支持的 decoder-only 因果语言模型，提供离线文本生成与 OpenAI 兼容服务。基于 vLLM V1 引擎，支持 chunked prefill 与 prefix caching；可通过环境变量调节 KV cache 大小与精度、启用 8 位/4 位权重量化。无预编译 wheel 与镜像，需从源码构建 wheel 或 Docker 镜像；不支持 LoRA 服务、异步调度、多模态与并行策略。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 Intel CPU（AVX2）与集成/独立 GPU 上运行 vLLM 文本生成
- 基于 vLLM V1 引擎，支持 chunked prefill 与 prefix caching
- KV cache 大小/精度可调，支持 8 位与 4 位权重压缩
- 提供版本中性的离线回归基准脚本

## 适用场景

- 在没有独立 GPU 的 Intel CPU 服务器上部署 vLLM 推理服务
- 利用 Intel GPU 运行 OpenAI 兼容的文本生成服务
- 对比插件新旧版本的性能回归测试

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L1: # vLLM OpenVINO Plugin
> L3: The vLLM OpenVINO plugin provides text generation for supported decoder-only

## 星数曲线

```mermaid
xychart-beta
    title "vllm-project/vllm-openvino 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-26 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `80859e11d154` · [字段定义](../../DATASET.md)*
