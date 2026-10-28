# maheshvaikri-code/snapllm

⭐ 42 · C++ · NOASSERTION · 推送 2026-09-27 · [GitHub](https://github.com/maheshvaikri-code/snapllm) · 个人维护

**本地多模型 LLM 推理引擎：常驻多模型免重载切换**

基于 llama.cpp 与 stable-diffusion.cpp 的本地推理服务器，支持同时加载并管理多个模型，在模型保持常驻的情况下切换而无需重新加载权重；提供 GPU/CPU 混合分层、KV 缓存持久化（vPID L1/L2 缓存与 HOT/WARM/COLD 三级内存）、OpenAI 兼容 API、React Web UI 与桌面应用。支持文本 LLM、视觉模型（Gemma 3 Vision、Qwen-VL、LLaVA）与 Stable Diffusion 系扩散模型。从源码编译安装（C++17、CMake 3.18+，CUDA 为可选 GPU 加速），提供 Docker Compose 与 Docker Hub CPU/CUDA 镜像。README 明确声明不对端到端延迟做保证，需自行基准测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型常驻与免重载切换（vPID 架构）
- OpenAI 兼容 API（/v1/chat/completions 等）
- LLM、视觉模型与 Stable Diffusion 图像生成多模态支持
- KV 缓存持久化与上下文预计算（contexts/ingest + 索引查询）

## 适用场景

- 在同一服务中并行挂载多个 GGUF 模型并按需切换
- 用 OpenAI 兼容接口做本地聊天、视觉分析与文生图
- 预计算文档 KV 缓存后基于缓存上下文提问

## 场景标签

`推理引擎` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L35: SnapLLM is a local inference engine built on llama.cpp and
> L70: |**OpenAI-Compatible API**|Drop-in replacement for OpenAI API|

## 星数曲线

```mermaid
xychart-beta
    title "maheshvaikri-code/snapllm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-28 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `e961fb930dcf` · [字段定义](../../DATASET.md)*
