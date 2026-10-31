# huggingface/huggingface-inference-toolkit

⭐ 98 · Python · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/huggingface/huggingface-inference-toolkit) · [官网](https://ui.endpoints.huggingface.co/) · 组织维护

**在容器中部署 Transformers/Diffusers/Sentence-Transformers 模型的服务工具包**

Hugging Face 维护的推理服务工具包：为 Transformers、Diffusers、Sentence-Transformers 模型提供容器内默认的预处理、预测与后处理流程，用户可通过 handler.py 自定义推理逻辑。通过环境变量（HF_MODEL_ID/HF_TASK/HF_MODEL_DIR 等）指定 Hub 上的模型或本地模型目录，用 uvicorn 本地运行或构建 CPU/GPU Docker 镜像部署；支持 Vertex AI 自定义容器与 AWS Inferentia2（Neuron 编译）部署，是 Inference Endpoints 的默认选项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Transformers/Diffusers/Sentence-Transformers 模型的容器化服务与默认推理流程
- 自定义 handler.py 覆盖推理逻辑并附加依赖
- 支持 Vertex AI 自定义容器与 AWS Inferentia2（Neuron 编译）部署
- WORKERS/UNLOAD_IDLE/IDLE_TIMEOUT 等环境变量控制多 worker 与按需加载

## 适用场景

- 把 Hub 上的模型打包成 CPU/GPU 容器对外提供推理 API
- 在 Vertex AI 或 SageMaker 上以自定义容器部署 HF 模型
- 通过自定义 handler 部署自己的模型产物

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Hugging Face Inference Toolkit is for serving 🤗 Transformers models in containers. This library provides default pre
> L75: The Hugging Face Inference Toolkit is also supported on Vertex AI, based on Custom container requirements for predi
> L118: ### AWS Inferentia2 Support

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/huggingface-inference-toolkit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 96 --> 99
    line [97, 98, 98]
```

2026-10-18 97 → 2026-10-31 98（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `3cd3742c60b6` · [字段定义](../../DATASET.md)*
