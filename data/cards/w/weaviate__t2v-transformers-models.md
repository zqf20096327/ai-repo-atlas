# weaviate/t2v-transformers-models

⭐ 63 · Python · BSD-3-Clause · 推送 2026-09-23 · [GitHub](https://github.com/weaviate/t2v-transformers-models) · 组织维护

**Weaviate 文本向量化模块的模型推理容器镜像集**

为 Weaviate text2vec-transformers 模块提供推理容器的仓库：以 Docker 镜像形式发布，内含多个 Hugging Face transformers 模型（sentence-transformers、BGE、DPR、flan-t5 等，部分含 ONNX 版本），用于语义搜索场景的向量化推理。用户可直接拉取 Docker Hub 预构建镜像，或用两行 Dockerfile 从 Hugging Face Hub 或本地私有模型构建自定义镜像，部署于 Docker/Kubernetes。镜像 tag 可按 git 版本固定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 30 余个预构建 Docker 镜像，覆盖 sentence-transformers/BGE/DPR/flan-t5 等模型
- 支持任意 Hugging Face 或本地私有模型的 Two-line Dockerfile 自定义构建
- 部分模型提供 ONNX 版本镜像
- 镜像 tag 可按仓库 git tag 固定版本

## 适用场景

- 为 Weaviate 语义搜索配置 text2vec-transformers 向量化模型
- 将私有或未收录的 transformers 模型打包为 Weaviate 推理容器
- 在 Kubernetes 中部署模型推理服务供 Weaviate 调用

## 场景标签

`语义搜索` `推理引擎` · 领域:知识与检索

## 证据(README 行号)

> L3: This is the the inference container which is used by the Weaviate
> L4: `text2vec-transformers` module. You can download it directly from Dockerhub

## 星数曲线

```mermaid
xychart-beta
    title "weaviate/t2v-transformers-models 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-29 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d1c5bdfaf100` · [字段定义](../../DATASET.md)*
