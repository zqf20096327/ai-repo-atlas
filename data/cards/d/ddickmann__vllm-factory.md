# ddickmann/vllm-factory

⭐ 87 · Python · Apache-2.0 · 推送 2026-07-06 · [GitHub](https://github.com/ddickmann/vllm-factory) · 个人维护

**以 vLLM 插件形式生产化部署编码器模型（ColBERT/GLiNER/ColPali 等）**

面向编码器类模型（嵌入、ColBERT 检索、GLiNER 命名实体识别、ColPali 多模态检索、实体链接）的推理部署框架：提供 12 个 vLLM 插件，以插件架构接入 vLLM 0.19+ 的连续批处理与显存管理，无需 fork vLLM。每个插件附带 IOProcessor 在服务端完成前后处理，客户端通过 JSON 请求 /pooling 端点。提供 vllm-factory-serve 多实例模式（beta）在单 GPU 上运行多 vLLM 实例。安装要求 Python 3.11+、vLLM 0.19+、Linux 与 CUDA；通过 PyPI、源码或 Docker 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 12 个编码器插件覆盖嵌入、ColBERT 检索、GLiNER NER、多模态检索与实体链接
- IOProcessor 在 vLLM 进程内完成前后处理，客户端发送结构化 JSON 即可
- 多实例服务（beta）：单 GPU 运行多 vLLM 实例，附异步请求分发
- 12/12 插件通过输出等价性校验（嵌入余弦相似度或 NER 实体召回）

## 适用场景

- 把 ColBERT/GLiNER 等编码器模型以 vLLM 服务形式部署上线
- 生产环境中对检索、NER 服务做连续批处理与流量调度
- 单 GPU 上通过多实例提升编码器吞吐

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: **Production inference for encoders, poolers, and structured prediction — as vLLM plugins.**
> L11: > **12 encoder plugins · IOProcessor pre/post-processing · continuous batching · zero vLLM forks**
> L82: **vLLM Factory bridges that gap.** Every bespoke encoder architecture — ColBERT, GLiNER, entity linking, multimodal

## 星数曲线

```mermaid
xychart-beta
    title "ddickmann/vllm-factory 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 85 --> 88
    line [86, 87, 87]
```

2026-10-18 86 → 2026-10-30 87（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d1ab236d95db` · [字段定义](../../DATASET.md)*
