# DominikBucko/glm53-flash-2x3090

⭐ 3 · Python · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/DominikBucko/glm53-flash-2x3090) · [官网](https://huggingface.co/albucino/GLM-5.3-Flash-EXL3-3.05bpw) · 个人维护

**在 2×RTX 3090 上运行 GLM-5.3-Flash 的本地推理运行时**

提供在两块 24 GB GPU 与 128 GB 系统内存上服务 320B 参数 MoE 模型 GLM-5.3-Flash（EXL3 3.05 bpw 量化）的运行时：路由专家存放于系统内存，GPU 缓存活跃专家，CPU 线程池在解码期间计算冷专家。基于固定版本 vLLM 镜像与补丁版 ExLlamaV3，以 Docker 部署，监听 OpenAI 兼容 API，支持工具调用与推理，含 262,144 token 上下文与 agent 配置（限定思考预算、保留推理内容）。仅在一台机器上验证，单请求串行处理。

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

- CPU 专家卸载：路由专家驻留系统内存，2×24 GB GPU 服务 117 GiB 权重
- OpenAI 兼容 API，支持工具调用与 reasoning_effort 映射
- agent 默认配置：4,096 token 思考预算与最近 4 轮推理内容回填
- 提供 prefill/agent/实验性三种配置档

## 适用场景

- 在消费级双 GPU 工作站上本地运行大上下文 MoE 模型
- 为 agent 循环提供本地工具调用推理服务
- 处理 131K+ token 长提示的一次性 prefill 任务

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L9: with 18B active parameters, 288 routed experts per layer and a 262,144-token context. This runtime serves
> L14: The serving code is a pinned vLLM image plus the GLM-5.3 support of
> L77: listens on `http://127.0.0.1:8000/v1` (OpenAI-compatible, model `GLM-5.3-Flash`, tool calling and reasoning

## 星数曲线

```mermaid
xychart-beta
    title "DominikBucko/glm53-flash-2x3090 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-25"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-08 3 → 2026-11-25 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `001751689081` · [字段定义](../../DATASET.md)*
