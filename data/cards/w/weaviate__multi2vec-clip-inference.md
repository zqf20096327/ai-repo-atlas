# weaviate/multi2vec-clip-inference

⭐ 10 · Python · BSD-3-Clause · 推送 2026-02-09 · [GitHub](https://github.com/weaviate/multi2vec-clip-inference) · 组织维护

**为 Weaviate multi2vec-clip 模块提供 CLIP 多模态向量的推理容器**

Weaviate multi2vec-clip 模块对应的推理服务代码：通过 Docker 构建推理容器，加载指定的多语言文本模型与 CLIP 图像模型，生成向量供 Weaviate 使用；提供测试脚本与模型下载脚本，并说明在 NVIDIA Jetson 设备上运行所需的 JetPack 版本（仅支持 JetPack 6，JetPack 7 支持标注为即将到来）与依赖安装步骤，最后可用 uvicorn 启动推理服务并运行冒烟测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Docker 构建脚本可配置文本与 CLIP 模型名称
- 提供模型下载、服务启动与冒烟测试脚本
- 支持在 NVIDIA Jetson 设备（JetPack 6）上以 CUDA 运行

## 适用场景

- 为 Weaviate 部署 multi2vec-clip 模块的向量化推理服务
- 在 NVIDIA Jetson 边缘设备上运行 CLIP 嵌入模型
- 自行构建包含指定 CLIP 模型的推理容器

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L2: The inference container for the clip module
> L8: ## Build Docker container

## 星数曲线

```mermaid
xychart-beta
    title "weaviate/multi2vec-clip-inference 星数(近 2 点)"
    x-axis ["2026-10-21", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-21 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `9fff436bc8bc` · [字段定义](../../DATASET.md)*
