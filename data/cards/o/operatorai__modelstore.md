# operatorai/modelstore

⭐ 403 · Python · Apache-2.0 · 推送 2026-08-05 · [GitHub](https://github.com/operatorai/modelstore) · 个人维护

**Python 模型注册库：对机器学习模型做版本化、导出与存取**

一个开源模型注册（model registry）Python 库：将机器学习模型导出、上传并自动版本化，按 domain 和 state 组织管理，支持按 id 下载或直接加载回内存，也提供命令行下载工具。无需独立跟踪服务器，后端支持 AWS S3、Azure Blob、GCP Storage、MinIO 兼容对象存储及本地文件系统目录。支持 PyTorch、TensorFlow、Keras、scikit-learn、Transformers、XGBoost 等 20 余种 ML 库的模型保存，未列出的框架可上传原始文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无需跟踪服务器，模型在本地文件系统或云存储桶中版本化
- 支持 AWS S3 / Azure Blob / GCP / MinIO 兼容存储及本地目录
- 按 domain 与 state 管理模型，可下载或直接加载进内存
- 支持 20+ ML 库（PyTorch、TensorFlow、Keras、Transformers、XGBoost 等）

## 适用场景

- 把训练好的模型版本化归档到 S3 或本地文件系统
- 团队按 domain/state 管理与查找已上传的模型
- 从命令行或 Python 中下载/加载指定版本的模型

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: `modelstore` is a Python library that allows you to version, export, save and download machine learning models in yo
> L9: ## modelstore is an open source model registry
> L15: ✅ Upload and version all your models

## 星数曲线

```mermaid
xychart-beta
    title "operatorai/modelstore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 402 --> 404
    line [403, 403]
```

2026-10-18 403 → 2026-10-28 403（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8d8a9b155003` · [字段定义](../../DATASET.md)*
